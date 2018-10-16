from flask import Flask, render_template, make_response
from flask_restful import reqparse, abort, Api, Resource
from collections import defaultdict
from random import choice, shuffle
import urllib
import urllib.parse
import sys
from json2html import *

def overlap(frag1, frag2):
    """ get the maximum overlap between frag1 & frag2 and overlap start position """

    overlaps = []

    for i in range(len(frag2)):
        for j in range(len(frag1)):
            if frag1.endswith(frag2[:i + 1], j):
               if i > 2:
                  overlaps.append((i, j))

    return max(overlaps) if overlaps else (0, -1)


def get_output_string(fraglst):
    overlaps = defaultdict(list)
    while len(fraglst) > 1:
          overlaps.clear()

          for frag1 in fraglst:
              for frag2 in fraglst:
                  if frag1 == frag2:
                     continue

                  amount, start = overlap(frag1, frag2)
                  overlaps[amount].append((start, frag1, frag2))  # add key (amount of overlap) and value (start position between a and b)
                  

          maximum = max(overlaps)                         # pick maximum overlaps 
 

          if maximum == 0:                                # if maximum =0  then break
             break

          start, frag1, frag2 = overlaps[maximum][0]        

          fraglst.remove(frag1)
          fraglst.remove(frag2)
          fraglst.append(frag1[:start] + frag2)    
    merged_str = ''.join(fraglst)
    return (urllib.parse.unquote_plus(urllib.parse.unquote_plus(merged_str)))



app = Flask(__name__)
api = Api(app)

TODOS= {}
  

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('output',type=str)
# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
     def get(self):
         headers = {'Content-Type': 'text/html'} 
         return make_response(render_template('response.html',data=TODOS),200,headers)
         #return render_template('user.html',data=TODOS)  
         #return TODOS

     def post(self):
        args = parser.parse_args()     
        #print(args)
        fragments=args['output']
        #print(sys.argv)
        #print("fragements=",urllib.parse.quote_plus(fragments))
        lst = fragments.rstrip().split(" ")
        #lst=urllib.parse.quote_plus(lst)
        #print(lst)
        merged_text=get_output_string(lst) 
        TODOS['sample'] = {'output':merged_text} 
        #print(merged_text)
        #TODOS[1] = {'output':args['output']}
        return {'output': args['output']}, 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
#api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
