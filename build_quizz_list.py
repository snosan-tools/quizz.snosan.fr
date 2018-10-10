# -*- coding: utf-8 -*-
import glob
import json

files = glob.glob("static/*.json")

res = []
for file in files:
    content = json.load(open(file))
    res.append({'title': content['title'], 'slug': content['slug']})

with open('static/liste-quizz.json', 'w') as f:
    json.dump(res, f)
