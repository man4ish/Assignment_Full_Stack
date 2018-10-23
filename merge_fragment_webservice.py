from flask import Flask, render_template, make_response
from flask_restful import reqparse, abort, Api, Resource
from collections import defaultdict
from random import choice, shuffle
import urllib
import urllib.parse
import sys
from merge_fragment_assembler import *
from json2html import *

app = Flask(__name__)
api = Api(app)

TODOS= {}  

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('output',type=str)

class TodoList(Resource):
     def get(self):
         headers = {'Content-Type': 'text/html'} 
         return make_response(render_template('response.html',data=TODOS),200,headers)

     def post(self):
        fobj = fragaseemble()
        args = parser.parse_args()     
        fragments=args['output']
        lst = fragments.rstrip().split(" ")
        merged_text=fobj.get_output_string(lst) 
        TODOS['sample'] = {'output':merged_text} 
        print(merged_text)
        return {'output': args['output']}, 201

## Actually setup the Api resource routing here

api.add_resource(TodoList, '/todos')


if __name__ == '__main__':
    app.run(debug=True)
