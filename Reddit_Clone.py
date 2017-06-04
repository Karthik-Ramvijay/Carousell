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

@route('/',method="POST")
def post():
        topic=request.POST.get('topictxt')
        if topic.strip():
            key=len(mydict)+1
            txt=topic.strip()
            label_count="count_"+str(key)
            mydict[key]=[txt,label_count]
            table_content="<tr>"\
                       "<td>"\
                        +txt+\
                        "</td>"\
                        "<td><input class=upbutton value=UP type=image  id="+label_count+" src=static/Picture1.png>"\
                        "</td>"\
                        "<td width=3 height=5><input name="+label_count+" id="+label_count+" value=0 size=3 readonly></input></td>"\
						"<td><input class=downbutton value=DOWN type=image  id="+label_count+"  src=static/Picture2.png>"\
						"</button></td>"\
						"</tr>"

            return table_content


if __name__ == '__main__':
    run(host=HOST,debug=True,reloader=True)