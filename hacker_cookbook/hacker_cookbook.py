# -*- coding: utf-8 -*-
"""
  hacker_cookbook application

  :copyright: (c) by 
  :license: CCC 1.0
"""

# app.py

from flask import Flask, request, jsonify, render_template, redirect, render_template_string
import os
import json
from datetime import datetime

from flask_misaka import Misaka, markdown

app = Flask(__name__)
Misaka(app)

tree = {}
subfolders = {}

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
content = ""
with open('README.md', "r") as f:
  content = f.read()

def get_sections(path):
  subfolders = dict(name=path, children=[])
  try: lst = os.listdir(path)
  except OSError:
    pass #ignore errors
    # display 404
  else:
    for name in lst:
      fn = os.path.join(path, name)
      if os.path.isdir(fn):
        #subfolders['children'].append(get_sections(fn))
        subfolders['children'].append(name)
  #print ('DEBUG: ' + str(subfolders))
  return subfolders

@app.route('/')
def index():
  sections = get_sections('/app/hacker_cookbook/templates')
  print ('DEBUG: ' + str(sections))
  return render_template("index.html", html=markdown(content), sections=sections)

def make_tree(path):
  tree = dict(name=path, children=[])
  try: lst = os.listdir(path)
  except OSError:
    pass #ignore errors
    # display 404
  else:
    for name in lst:
      if (name != 'README.md' and name != '_section.md'):
        fn = os.path.join(path, name)
        if os.path.isdir(fn):
          tree['children'].append(make_tree(fn))
        else:
          tree['children'].append(dict(name=fn))
  
  return tree


  
@app.route('/<section>')
def list_recipes(section):
  my_section = CURR_DIR + "/templates/" + section
  # check if section exist
  if os.path.isdir(my_section):
    tree = make_tree(my_section)
    return render_template("sub.html", section=section, tree=tree )
  else:
    return render_template('404.html'), 404
  
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)