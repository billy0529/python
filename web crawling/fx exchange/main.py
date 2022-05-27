import requests as req

res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")

html = res.text
pos = html.split("<span class=\"value\">")[1].split("</span>")[0]
print(pos)

