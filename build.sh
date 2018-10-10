#!/usr/bin/env bash
rm -rf static/liste-quizz.json
python build_quizz_list.py

yarn run build
