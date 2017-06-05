__author__ = 'karthikwitty'

from bottle import run,route,template,request,static_file
from prettytable import PrettyTable

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

        else:
            output=template('index.tpl',rows=mydict)
            return output


@route('/sorting',method=["POST"])
def sort():
        id=int(request.POST.get('click'))
        print(id)
        topic_list=list(mydict.values())
        total_topics=range(1,len(topic_list)+1)
        for topic_num,topic in zip(total_topics,topic_list):
            cur_vote=request.POST.get('count_'+str(topic_num))
            topic.append(int(cur_vote))
            mydict[topic_num]=topic
        name={}
        for key,value in request.forms.items():
            name[key]=int(value)

        del name['click']

        if id==1:

            new_list=mydict.values()
            for key in name.keys():
                for tem in new_list:
                    if key == tem[1]:
                        tem.append(name[key])

            my_list=sorted(new_list, key=lambda x:x[2],reverse=True)
            table=PrettyTable()
            table.format=True
            table.border=True
            table.padding_width=2

            table.field_names=['Topic','Votes']

            for item in my_list[:20]:
                table.add_row([item[0],item[2]])

            table_html=table.get_html_string()
            return table_html

        elif id > 1:
            new_dict={}

            for value in mydict.values():
                try:
                    new_dict[value[1]]=[value[0],value[2]]
                except Exception:
                    new_dict[value[1]]=[value[0],name[value[1]]]

            for key in name.keys():
                new_dict[key][1]=name[key]

            my_list=sorted(new_dict.values(), key=lambda x:x[1],reverse=True)

            table=PrettyTable()
            table.format=True
            table.border=True
            table.padding_width=2

            table.field_names=['Topic','Votes']

            for item in my_list[:20]:
                table.add_row([item[0],item[1]])

            table_html=table.get_html_string()

            return table_html


if __name__ == '__main__':
    run(host=HOST,debug=True,reloader=True)