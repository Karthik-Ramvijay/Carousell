__author__ = 'karthikwitty'

from bottle import run,route,template,request,static_file

mydict={}
HOST='localhost'

@route('/static/<filepath>')
def server_static(filepath):
    return static_file(filepath, root='../Carousell')

@route('/')
def index():
   return template('index.tpl',rows=mydict)


if __name__ == '__main__':
    run(host=HOST,debug=True,reloader=True)