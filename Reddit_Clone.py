__author__ = 'karthikwitty'

from bottle import run,route,template

mydict={}
HOST='localhost'


@route('/')
def index():
   return template('index.tpl',rows=mydict)

if __name__ == '__main__':
    run(host=HOST,debug=True,reloader=True)