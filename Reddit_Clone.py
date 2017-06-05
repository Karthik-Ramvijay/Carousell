__author__ = 'karthikwitty'

from bottle import run,route,template,request,static_file
from prettytable import PrettyTable

# Initializing Dictionary and Initializing host as local host
mydict={}
HOST='localhost'

# Routing through the Static path to take input Files locally by the System
@route('/static/<filepath>')
def server_static(filepath):
    return static_file(filepath, root='../Carousell')

# Routing into the home page
@route('/')
def index():
   return template('index.tpl',rows=mydict)

# Routing to the home page and Giving Request through Post Method
@route('/',method="POST")
def post():

        #Assiging the Topic variable from User input Text
        topic=request.POST.get('topictxt')
        if topic.strip(): # check whether the User input variable contains only space. (Double check)
            key=len(mydict)+1 # To assign the Id to the entered Topic
            txt=topic.strip()
            label_count="count_"+str(key) # labelling using the ID 
            mydict[key]=[txt,label_count] # Forming the dictionary Variable

            # Dynamically Creating the table on the fly according to the user entered Input Text
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

            return table_content # Returning the Table Content to the Ajax Post method which will be included in the Table

        else:
            output=template('index.tpl',rows=mydict)
            return output


# Impletementation for the Final Sorting Through Post Request
@route('/sorting',method=["POST"])
def sort():

        # Getting the Button Click Count for the Sorting
        id=int(request.POST.get('click'))

        # Getting the List of Topics from the Existing Table
        topic_list=list(mydict.values())
        total_topics=range(1,len(topic_list)+1)
        for topic_num,topic in zip(total_topics,topic_list):
            cur_vote=request.POST.get('count_'+str(topic_num))
            topic.append(int(cur_vote))
            mydict[topic_num]=topic

        # Creating our own Dictionary from the Data formed in Ajax Post call from the Existing Table
        name={}
        for key,value in request.forms.items():
            name[key]=int(value)

        del name['click'] # deleting the Click key from Request

        if id==1: # Implementation Logic for Button Click Count is 1

            new_list=mydict.values() # Get the Topic Values and Assigning to the Exising Keys
            for key in name.keys():
                for tem in new_list:
                    if key == tem[1]:
                        tem.append(name[key])

            my_list=sorted(new_list, key=lambda x:x[2],reverse=True) # Sorting in Descending Order
            table=PrettyTable()
            table.format=True
            table.border=True
            table.padding_width=2

            table.field_names=['Topic','Votes']

            for item in my_list[:20]:
                table.add_row([item[0],item[2]]) # Adding data to the Table

            table_html=table.get_html_string() # Getting the Data in HTML String and returning it to the User 
            return table_html

        elif id > 1: # Implementation Logic for Button Click Count is more than 1
            
            new_dict={} # To copy the Existing Element in exising dictionary to new dictionary

            for value in mydict.values(): # Getting The Value and Assign the Value as  key for the Newly formed Dictionary.
                try:
                    new_dict[value[1]]=[value[0],value[2]]
                except Exception:
                    new_dict[value[1]]=[value[0],name[value[1]]]

            for key in name.keys():  # matching the Keys from Two Dictionaries to assign the Correct vote for Each Topic
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