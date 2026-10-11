from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
F=r"C:/Users/BYROND~1/AppData/Local/Temp/claude/G--Other-computers-Workstation-DELL-DELL-BYRONCUJANO-Escritorio-Eccentric-Inc-AiUDA-PROYECTOS-HIGGSFIELD/0a4bba30-b3f5-408b-80b9-95dfa18eb247/scratchpad/fonts/"
K=2  # render scale
base=Image.open("cerebro_base.png").convert("RGBA")
W,H=base.width*K,base.height*K
SC=1.32; CX,CY=680,720
bw,bh=int(base.width*SC*K),int(base.height*SC*K)
big=base.resize((bw,bh),Image.LANCZOS)
bg=Image.new("RGBA",(W,H),(5,12,40,255))
bg.alpha_composite(big,(int((CX-CX*SC)*K),int((CY-CY*SC)*K)))
LIME=(215,255,30,255); WHITE=(255,255,255,255); SOFT=(225,232,250,255); DIM=(185,200,235,255)
def anton(s): return ImageFont.truetype(F+"Anton-Regular.ttf",int(s*K))
def play(s,w=500):
    f=ImageFont.truetype(F+"PlayfairDisplay-Italic%5Bwght%5D.ttf",int(s*K))
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def inter(s,w=400):
    f=ImageFont.truetype(F+"Inter%5Bopsz,wght%5D.ttf",int(s*K))
    try: f.set_variation_by_axes([min(32,max(14,s)),w])
    except Exception: pass
    return f
d=ImageDraw.Draw(bg)
def tw(t,f,sp=0):
    return sum(d.textlength(c,font=f) for c in t)+sp*K*(len(t)-1) if sp else d.textlength(t,font=f)
def text(x,y,t,f,fill,sp=0,anchor="l"):
    w=tw(t,f,sp)
    if anchor=="c": x=x*K-w/2
    elif anchor=="r": x=x*K-w
    else: x=x*K
    if not sp: d.text((x,y*K),t,font=f,fill=fill); return w
    for c in t:
        d.text((x,y*K),c,font=f,fill=fill); x+=d.textlength(c,font=f)+sp*K
    return w
def line(x1,y1,x2,y2,fill,w=1): d.line((x1*K,y1*K,x2*K,y2*K),fill=fill,width=int(w*K))
d=ImageDraw.Draw(bg)
Wd=W//K; M=90
# darken lower half subtly for legibility
grad=Image.new("L",(1,H)); 
for y in range(H): grad.putpixel((0,y),int(max(0,min(1,(y/H-0.27)/0.20))*215))
shade=Image.new("RGBA",(W,H),(3,8,28,255)); shade.putalpha(grad.resize((W,H)))
bg.alpha_composite(shade)
# top vignette for header
tg=Image.new('L',(1,H))
for y in range(H): tg.putpixel((0,y),int(max(0,1-y/(300*K))*215))
ts=Image.new('RGBA',(W,H),(3,8,28,255)); ts.putalpha(tg.resize((W,H))); bg.alpha_composite(ts)
img=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(img)


# ---- header
logo=Image.open("logo_fenatrape_circulo.png").convert("RGBA")
ls=150*K; lg=logo.resize((ls,ls),Image.LANCZOS); ly=56
sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse(((M-6)*K,(ly+2)*K,(M+156)*K,(ly+164)*K),fill=(0,0,0,150))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14*K))); d=ImageDraw.Draw(img)
img.alpha_composite(lg,(M*K,ly*K)); d=ImageDraw.Draw(img)
tx=M+172
text(tx,ly+14,"ORGANIZA",inter(18,700),LIME,sp=4)
text(tx,ly+40,"FENATRAPE",inter(34,800),WHITE,sp=1)
text(tx,ly+88,"Federación Nacional de",inter(20,500),SOFT)
text(tx,ly+114,"Transporte Pesado del Ecuador",inter(20,500),SOFT)
text(Wd-M,ly+14,"TALLER",inter(20,800),LIME,sp=4,anchor="r")
text(Wd-M,ly+42,"PRESENCIAL",inter(20,800),LIME,sp=4,anchor="r")

# ---- title block
y=850
f=inter(30,800); t="TALLER DE PROMPTING"; w=tw(t,f,8)/K
text(Wd/2,y,t,f,LIME,sp=8,anchor="c")
line(M,y+20,Wd/2-w/2-26,y+20,(215,255,30,200),2); line(Wd/2+w/2+26,y+20,Wd-M,y+20,(215,255,30,200),2)
text(Wd/2,y+48,"Aprende a",play(112,600),WHITE,anchor="c")
fa=anton(176); t1="HABLAR CON LA "; t2="IA"
w1=tw(t1,fa,2);w2=tw(t2,fa,2); x0=(W-(w1+w2+2*K))/2/K
text(x0,y+178,t1,fa,WHITE,sp=2); text(x0+(w1+2*K)/K,y+178,t2,fa,LIME,sp=2)

# ---- info row
y2=1290
line(M,y2,Wd-M,y2,(255,255,255,90),1.5)
cols=[("FECHAS","21 · 22 · 23","OCTUBRE 2026"),("HORA","2:00 PM","3 HORAS DIARIAS"),("LUGAR","AUDITORIO","FENATRAPE")]
cw=(Wd-2*M)/3
for i,(k,a,b) in enumerate(cols):
    cx=M+cw*i+cw/2
    text(cx,y2+26,k,inter(19,800),LIME,sp=4,anchor="c")
    text(cx,y2+56,a,anton(58),WHITE,sp=1,anchor="c")
    text(cx,y2+136,b,inter(20,700),SOFT,sp=2,anchor="c")
    if i: line(M+cw*i,y2+26,M+cw*i,y2+166,(255,255,255,80),1.5)
line(M,y2+194,Wd-M,y2+194,(255,255,255,90),1.5)

# ---- price block
y3=1505
fp=anton(170); pw=tw("$65",fp,2)
gl=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(gl)
gd.text((M*K,(y3-10)*K),"$65",font=fp,fill=(215,255,30,110))
img.alpha_composite(gl.filter(ImageFilter.GaussianBlur(26*K))); d=ImageDraw.Draw(img)
text(M,y3-10,"$65",fp,LIME,sp=2)
px=M+pw/K+44
text(px,y3+18,"INVERSIÓN ÚNICA",inter(19,800),DIM,sp=4)
text(px,y3+48,"Los tres días · 9 horas",play(48,600),WHITE)
bx,by=px,y3+128; ft=inter(22,800); t="CERTIFICADO INCLUIDO"; tww=tw(t,ft,3)/K
d.rounded_rectangle((bx*K,by*K,(bx+tww+56)*K,(by+58)*K),radius=29*K,fill=LIME)
text(bx+28,by+15,t,ft,(6,18,60,255),sp=3)

# ---- bank panel
py=1735; ph=222
panel=Image.new("RGBA",(W,H),(0,0,0,0)); pd=ImageDraw.Draw(panel)
pd.rounded_rectangle((M*K,py*K,(Wd-M)*K,(py+ph)*K),radius=22*K,fill=(10,28,80,215),outline=(215,255,30,230),width=int(2*K))
img.alpha_composite(panel); d=ImageDraw.Draw(img)
ix=M+34
text(ix,py+26,"DATOS PARA DEPÓSITO O TRANSFERENCIA",inter(19,800),LIME,sp=3)
text(ix,py+62,"BANCO PICHINCHA · CUENTA DE AHORROS",inter(22,700),WHITE,sp=1)
text(ix,py+100,"4419572000",anton(76),WHITE,sp=3)
rx=Wd-M-34
text(rx,py+62,"TITULAR",inter(18,800),DIM,sp=3,anchor="r")
text(rx,py+90,"FAGAL Abogados",inter(28,800),WHITE,anchor="r")
text(rx,py+128,"Dr. Fabián Galarraga",inter(24,600),SOFT,anchor="r")
text(rx,py+164,"C.I. 1710443712",inter(24,700),SOFT,anchor="r")

# ---- footer
yf=1990
text(M,yf,"CUPO LIMITADO",inter(20,800),LIME,sp=5)
text(Wd-M,yf,"RESERVA TU LUGAR",inter(20,800),WHITE,sp=5,anchor="r")

sa=img.split()[3].filter(ImageFilter.GaussianBlur(10*K)).point(lambda v:min(255,int(v*0.85)))
shadow=Image.new("RGBA",(W,H),(0,4,20,255)); shadow.putalpha(sa)
bg.alpha_composite(shadow); bg.alpha_composite(img)
out=bg.convert("RGB")
out.save("poster_taller_prompting_premium_v3.png",optimize=True)
out.resize((W//3,H//3),Image.LANCZOS).save("_prev_poster.jpg",quality=90)
print(out.size)
