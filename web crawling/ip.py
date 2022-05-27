from ast import alias
import requests as req

res = req.get("http://api.ipify.org/", headers={"fast": "campus"})
print(res.text)
print(res.raw)
print(res.elapsed)
print(res.headers)
print(res.request.method)

