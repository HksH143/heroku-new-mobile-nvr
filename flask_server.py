from flask import Flask,request,redirect,render_template, url_for
from markupsafe import re
from werkzeug.datastructures import ImmutableMultiDict
import os,sys 
from werkzeug.utils import secure_filename
app = Flask(__name__)

sys.setrecursionlimit(1500)
@app.route("/")
def hello_world():
    
    return "Hello, This is web server using flask library !"

@app.route("/signup",methods=['GET', 'POST'])
def send_configs():
    app.config['my_configs']="",""
    print("Successfully Entered the Configuration Page ")
    if request.method=="POST":
        my_name=request.form["nm"]
        password=request.form["pass"]
        app.config['my_configs']=my_name,password
        print("User entered Name: ",app.config['my_configs'][0] )
        print("User entered Password: ",app.config['my_configs'][1] )
        return f"sending name as {my_name} and password as {password}"
        # return redirect( url_for("get_configs",usr=my_name) )
    else:
        return render_template("config_form.html")
    # wifi_ssid="Synapsify"
    # wifi_pass="synapsify@321"
    
@app.route("/configs")
def get_configs():
    # usr_name,password=app.config['my_configs']
    # print("Received Name :",usr_name," Received password : ",password)
    # return f"Recieved name as {usr_name} and passowd as {password}"
    print("Received Name :",app.config['my_configs'][0]," Received password : ",app.config['my_configs'][1])
    return f"Recieved name as {app.config['my_configs'][0]} and passowd as {app.config['my_configs'][1]}"

@app.route("/info")
def print_info():
    root_dir=os.getcwd()
    save_path=root_dir+"/save_files"    
    app.config['UPLOAD_FOLDER']=save_path
    print("Listing current files in dir: ",save_path)
    print(os.listdir(save_path))
    files=os.listdir(save_path)

    for file in files:
        if file != '.gitignore':
            file_dir=save_path+"/"+file 
            file_size = os.path.getsize(file_dir) 
            print("File: ",file," Size: ",file_size/1000000, 'mb'," bytes : ",file_size)

        

    return "This route is used to print file system info!"

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
    
    save_path=root_dir+"/save_files"
    app.config['UPLOAD_FOLDER']=save_path

    if request.files:
        # my_img=request.files["img"]
        
        
        
        # print("File Name: ",my_img.filename)
        # my_img.save("/home/hdr/Desktop/cpr_project/save_files/test_video.mp4")
        my_vid=request.files["vid"]
        print("File Name: ",my_vid.filename)
        print("Saving Images to: ",save_path)
        filename = secure_filename(my_vid.filename)
        my_vid.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        print("file saved: ")
        print(os.listdir(save_path))

        files=os.listdir(save_path)

        for file in files:
            if file != '.gitignore':
                file_dir=save_path+"/"+file 
                file_size = os.path.getsize(file_dir) 
                print("File: ",file," Size: ",file_size/1000000, 'mb'," bytes : ",file_size)

        

        # return redirect(request.url)
        return "server has received the file "
    # return "server has received name: "



if __name__ == '__main__':
    app.run(debug=True)
