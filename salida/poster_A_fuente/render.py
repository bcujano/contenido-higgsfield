import subprocess, sys, os, re, json, html, pathlib
CH=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
f=pathlib.Path(sys.argv[1]).resolve(); out=str(pathlib.Path(sys.argv[2]).resolve())
url=f.as_uri()
base=[CH,"--headless=new","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files","--window-size=1080,1920","--force-device-scale-factor=1","--virtual-time-budget=5000"]
d=subprocess.run(base+["--dump-dom",url],capture_output=True,text=True,encoding='utf-8').stdout
m=re.search(r'<pre id="report"[^>]*>(.*?)</pre>',d,re.S)
if not m: print("NO REPORT"); print(d[:500]); sys.exit(1)
r=json.loads(html.unescape(m.group(1)))
print("ISSUES:", *(r['issues'] or ['none']), sep="\n  ")
print("subject",r['subject'],"ia",r['ia'])
for i in r['items']: print(i)
subprocess.run(base+["--screenshot="+out,url],capture_output=True)
print("saved",out, os.path.getsize(out))
