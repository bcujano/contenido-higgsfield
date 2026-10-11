from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
F=r"C:/Users/BYROND~1/AppData/Local/Temp/claude/G--Other-computers-Workstation-DELL-DELL-BYRONCUJANO-Escritorio-Eccentric-Inc-AiUDA-PROYECTOS-HIGGSFIELD/0a4bba30-b3f5-408b-80b9-95dfa18eb247/scratchpad/fonts/"
K=2
LIME=(215,255,30,255); WHITE=(255,255,255,255); SOFT=(225,232,250,255); DIM=(185,200,235,255); NAVY=(6,18,60,255)
BASE=Image.open("cerebro_base.png").convert("RGBA")
BRAIN_CX,BRAIN_TOP=650,230   # brain bbox reference in base art
LOGO=Image.open("logo_fenatrape_circulo.png").convert("RGBA")

def anton(s): return ImageFont.truetype(F+"Anton-Regular.ttf",int(s*K))
def play(s,w=600):
    f=ImageFont.truetype(F+"PlayfairDisplay-Italic%5Bwght%5D.ttf",int(s*K)); f.set_variation_by_axes([w]); return f
def inter(s,w=400):
    f=ImageFont.truetype(F+"Inter%5Bopsz,wght%5D.ttf",int(s*K)); f.set_variation_by_axes([min(32,max(14,s)),w]); return f

class Poster:
    def __init__(s,Wd,Hd,SC,bx,btop):
        s.Wd,s.Hd=Wd,Hd; s.W,s.H=Wd*K,Hd*K
        s.bg=Image.new("RGBA",(s.W,s.H),(5,12,40,255))
        big=BASE.resize((int(BASE.width*SC*K),int(BASE.height*SC*K)),Image.LANCZOS)
        s.bg.alpha_composite(big,(int((bx-BRAIN_CX*SC)*K),int((btop-BRAIN_TOP*SC)*K)))
        s.img=Image.new("RGBA",(s.W,s.H),(0,0,0,0)); s.d=ImageDraw.Draw(s.img)
    def shade_v(s,y0,y1,amax,top=False):
        g=Image.new("L",(1,s.H))
        for y in range(s.H):
            t=(y/K-y0)/(y1-y0); t=1-t if top else t
            g.putpixel((0,y),int(max(0,min(1,t))*amax))
        self_l=Image.new("RGBA",(s.W,s.H),(3,8,28,255)); self_l.putalpha(g.resize((s.W,s.H))); s.bg.alpha_composite(self_l)
    def shade_h(s,x0,x1,amax):
        g=Image.new("L",(s.W,1))
        for x in range(s.W):
            t=1-(x/K-x0)/(x1-x0); g.putpixel((x,0),int(max(0,min(1,t))*amax))
        l=Image.new("RGBA",(s.W,s.H),(3,8,28,255)); l.putalpha(g.resize((s.W,s.H))); s.bg.alpha_composite(l)
    def tw(s,t,f,sp=0):
        return sum(s.d.textlength(c,font=f) for c in t)+sp*K*(len(t)-1) if sp else s.d.textlength(t,font=f)
    def text(s,x,y,t,f,fill,sp=0,anchor="l"):
        w=s.tw(t,f,sp); x=x*K-(w/2 if anchor=="c" else w if anchor=="r" else 0)
        if not sp: s.d.text((x,y*K),t,font=f,fill=fill); return w/K
        for c in t: s.d.text((x,y*K),c,font=f,fill=fill); x+=s.d.textlength(c,font=f)+sp*K
        return w/K
    def line(s,x1,y1,x2,y2,fill,w=1): s.d.line((x1*K,y1*K,x2*K,y2*K),fill=fill,width=int(w*K))
    def comp(s,layer): s.img.alpha_composite(layer); s.d=ImageDraw.Draw(s.img)

    # ---- blocks
    def header(s,M,ly=56,right=True):
        ls=150; sh=Image.new("RGBA",(s.W,s.H),(0,0,0,0))
        ImageDraw.Draw(sh).ellipse(((M-6)*K,(ly+2)*K,(M+ls+6)*K,(ly+ls+14)*K),fill=(0,0,0,150))
        s.bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14*K)))
        s.comp(Image.new("RGBA",(s.W,s.H),(0,0,0,0)))
        s.img.alpha_composite(LOGO.resize((ls*K,ls*K),Image.LANCZOS),(M*K,ly*K)); s.d=ImageDraw.Draw(s.img)
        tx=M+172
        s.text(tx,ly+14,"ORGANIZA",inter(18,700),LIME,sp=4)
        s.text(tx,ly+40,"FENATRAPE",inter(34,800),WHITE,sp=1)
        s.text(tx,ly+88,"Federación Nacional de",inter(20,500),SOFT)
        s.text(tx,ly+114,"Transporte Pesado del Ecuador",inter(20,500),SOFT)
        if right:
            s.text(s.Wd-M,ly+14,"TALLER",inter(20,800),LIME,sp=4,anchor="r")
            s.text(s.Wd-M,ly+42,"PRESENCIAL",inter(20,800),LIME,sp=4,anchor="r")
    def kicker(s,x0,x1,y,center=True):
        f=inter(30,800); t="TALLER DE PROMPTING"; w=s.tw(t,f,8)/K
        if center:
            cx=(x0+x1)/2; s.text(cx,y,t,f,LIME,sp=8,anchor="c")
            s.line(x0,y+20,cx-w/2-26,y+20,(215,255,30,200),2); s.line(cx+w/2+26,y+20,x1,y+20,(215,255,30,200),2)
        else:
            s.text(x0,y,t,f,LIME,sp=8); s.line(x0+w+26,y+20,x1,y+20,(215,255,30,200),2)
    def headline_one(s,y):
        s.text(s.Wd/2,y,"Aprende a",play(112),WHITE,anchor="c")
        fa=anton(176); t1="HABLAR CON LA "; w1=s.tw(t1,fa,2); w2=s.tw("IA",fa,2); x0=(s.W-(w1+w2+2*K))/2/K
        s.text(x0,y+122,t1,fa,WHITE,sp=2); s.text(x0+(w1+2*K)/K,y+122,"IA",fa,LIME,sp=2)
    def info(s,x0,x1,y):
        s.line(x0,y,x1,y,(255,255,255,90),1.5)
        cols=[("FECHAS","21 · 22 · 23","OCTUBRE 2026"),("HORA","2:00 PM","3 HORAS DIARIAS"),("LUGAR","AUDITORIO","FENATRAPE")]
        cw=(x1-x0)/3
        for i,(k,a,b) in enumerate(cols):
            cx=x0+cw*i+cw/2
            s.text(cx,y+26,k,inter(19,800),LIME,sp=4,anchor="c")
            s.text(cx,y+56,a,anton(58),WHITE,sp=1,anchor="c")
            s.text(cx,y+136,b,inter(20,700),SOFT,sp=2,anchor="c")
            if i: s.line(x0+cw*i,y+26,x0+cw*i,y+166,(255,255,255,80),1.5)
        s.line(x0,y+194,x1,y+194,(255,255,255,90),1.5)
    def price_glow(s,x,y,f):
        gl=Image.new("RGBA",(s.W,s.H),(0,0,0,0)); ImageDraw.Draw(gl).text((x*K,y*K),"$65",font=f,fill=(215,255,30,110))
        s.comp(gl.filter(ImageFilter.GaussianBlur(26*K))); s.text(x,y,"$65",f,LIME,sp=2)
        return s.tw("$65",f,2)/K
    def pill(s,x,y):
        ft=inter(22,800); t="CERTIFICADO INCLUIDO"; w=s.tw(t,ft,3)/K
        s.d.rounded_rectangle((x*K,y*K,(x+w+56)*K,(y+58)*K),radius=29*K,fill=LIME); s.text(x+28,y+15,t,ft,NAVY,sp=3)
    def price_row(s,M,y3):
        pw=s.price_glow(M,y3-10,anton(170)); px=M+pw+44
        s.text(px,y3+18,"INVERSIÓN ÚNICA",inter(19,800),DIM,sp=4)
        s.text(px,y3+48,"Los tres días · 9 horas",play(48),WHITE)
        s.pill(px,y3+128)
    def panel(s,x0,y0,x1,y1):
        p=Image.new("RGBA",(s.W,s.H),(0,0,0,0))
        ImageDraw.Draw(p).rounded_rectangle((x0*K,y0*K,x1*K,y1*K),radius=22*K,fill=(10,28,80,215),outline=(215,255,30,230),width=int(2*K))
        s.comp(p)
    def bank_wide(s,M,py):
        s.panel(M,py,s.Wd-M,py+222); ix=M+34; rx=s.Wd-M-34
        s.text(ix,py+26,"DATOS PARA DEPÓSITO O TRANSFERENCIA",inter(19,800),LIME,sp=3)
        s.text(ix,py+62,"BANCO PICHINCHA · CUENTA DE AHORROS",inter(22,700),WHITE,sp=1)
        s.text(ix,py+100,"4419572000",anton(76),WHITE,sp=3)
        s.text(rx,py+62,"TITULAR",inter(18,800),DIM,sp=3,anchor="r")
        s.text(rx,py+90,"FAGAL Abogados",inter(28,800),WHITE,anchor="r")
        s.text(rx,py+128,"Dr. Fabián Galarraga",inter(24,600),SOFT,anchor="r")
        s.text(rx,py+164,"C.I. 1710443712",inter(24,700),SOFT,anchor="r")
    def footer(s,M,yf):
        s.text(M,yf,"CUPO LIMITADO",inter(20,800),LIME,sp=5)
        s.text(s.Wd-M,yf,"RESERVA TU LUGAR",inter(20,800),WHITE,sp=5,anchor="r")
    def save(s,name):
        sa=s.img.split()[3].filter(ImageFilter.GaussianBlur(10*K)).point(lambda v:min(255,int(v*0.85)))
        sh=Image.new("RGBA",(s.W,s.H),(0,4,20,255)); sh.putalpha(sa)
        s.bg.alpha_composite(sh); s.bg.alpha_composite(s.img)
        out=s.bg.convert("RGB"); out.save(name,optimize=True)
        out.resize((s.W//3,s.H//3),Image.LANCZOS).save("_prev_"+name.replace(".png",".jpg"),quality=88)
        print(name,out.size)

def stacked(Hd,ty,SC,name):
    # ty = y of "TALLER DE PROMPTING"; vertical rhythm compressed vs 2:3
    p=Poster(1360,Hd,SC,680,12); M=90
    p.shade_v(ty-300,ty+110,215); p.shade_v(0,300,215,top=True)
    p.header(M); p.kicker(M,p.Wd-M,ty); p.headline_one(ty+44)
    yi=ty+405; p.info(M,p.Wd-M,yi)
    y3=yi+212; p.price_row(M,y3)
    py=y3+222; p.bank_wide(M,py)
    p.footer(M,py+246); p.save(name)

def square(name):
    Wd=Hd=1600; M=80
    p=Poster(Wd,Hd,1.2,1210,160)
    p.shade_h(380,900,235); p.shade_v(760,1000,225); p.shade_v(0,260,200,top=True)
    p.header(M)
    # left column headline
    y=330; p.kicker(M,860,y,center=False)
    p.text(M,y+46,"Aprende a",play(104),WHITE)
    fa=anton(168)
    p.text(M,y+166,"HABLAR CON",fa,WHITE,sp=2)
    w=p.text(M,y+366,"LA ",fa,WHITE,sp=2); p.text(M+w+4,y+366,"IA",fa,LIME,sp=2)
    yi=945; p.info(M,Wd-M,yi)
    # price (left)
    y3=1175
    p.text(M,y3,"INVERSIÓN ÚNICA",inter(19,800),DIM,sp=4)
    pw=p.price_glow(M,y3+18,anton(160))
    p.text(M+pw+30,y3+64,"Los tres días",play(44),WHITE)
    p.text(M+pw+30,y3+118,"9 horas",play(44),WHITE)
    p.pill(M,y3+262)
    # bank (right)
    x0=720; py=1165; x1=Wd-M; p.panel(x0,py,x1,py+300); ix=x0+32
    p.text(ix,py+26,"DATOS PARA DEPÓSITO O TRANSFERENCIA",inter(18,800),LIME,sp=2)
    p.text(ix,py+60,"BANCO PICHINCHA · CUENTA DE AHORROS",inter(21,700),WHITE,sp=1)
    p.text(ix,py+96,"4419572000",anton(72),WHITE,sp=3)
    p.text(ix,py+200,"FAGAL Abogados · Dr. Fabián Galarraga",inter(22,800),WHITE)
    p.text(ix,py+238,"Titular  ·  C.I. 1710443712",inter(21,600),SOFT)
    p.footer(M,Hd-58); p.save(name)

if __name__=="__main__":
    which=sys.argv[1:] or ["1x1","3x4","4x5"]
    if "3x4" in which: stacked(1813,640,1.08,"poster_taller_prompting_3x4.png")
    if "4x5" in which: stacked(1700,560,1.0,"poster_taller_prompting_4x5.png")
    if "1x1" in which: square("poster_taller_prompting_1x1.png")
