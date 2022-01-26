from flask import Flask,request,redirect
from markupsafe import re
from werkzeug.datastructures import ImmutableMultiDict
import os 
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, This is web server using flask library !"

@app.route("/new_page")
def new_page():
    return "you have entered into a new page !"

@app.route("/query_example",methods=['GET', 'POST'])
def query_page():
    my_name=request.args.get('name')
    # my_name=request.args['name']
    return "your name is : {}".format(my_name)

@app.route("/my_form",methods=['GET', 'POST'])
def my_form():
    return '''   
    <form method="POST">
    Your Name <input type="text" name="name">
    <input type="submit" value="click submit">
    </form>    
    
    '''
@app.route("/json_example",methods=['GET', 'POST'])
def client_receive():
    # req_data=request.get_data()
    # my_name=req_data[0]
    # req_data=request.get_json()
    # my_name=req_data['name']
    data = dict(request.form)
    print(data["name"])
    return "server has received name: "


@app.route("/file_upload",methods=['GET', 'POST'])
def receive_file():
    root_dir=os.getcwd()
    path=root_dir+"/save_files"

    if request.files:
        # my_img=request.files["img"]
        
        
        
        # print("File Name: ",my_img.filename)
        # my_img.save("/home/hdr/Desktop/cpr_project/save_files/test_video.mp4")
        my_vid=request.files["vid"]
        print("File Name: ",my_vid.filename)
        print("Saving Images to: ",path)
        filename = secure_filename(my_vid.filename)
        my_vid.save(path,my_vid.filename)

        

        # return redirect(request.url)
        return "server has received the image "
    # return "server has received name: "



if __name__ == '__main__':
    app.run(debug=True)
