# -*- coding: utf-8 -*-
import os
import glob
import json

TARGET_FILE = 'static/liste-quizz.json'

os.remove(TARGET_FILE)

files = glob.glob("static/*.json")

res = []
for file in files:
    content = json.load(open(file))
    res.append({'title': content['title'], 'slug': content['slug']})

with open(TARGET_FILE, 'w') as f:
    json.dump(res, f)
