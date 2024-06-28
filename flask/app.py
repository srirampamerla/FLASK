from flask import Flask,render_template #This render_template is responsible in redirecting to that particular HTML page.
'''
It creates an instance of the Flask Class,
which will be your WSGI(Web Server Gateway Interface) application.'''

### WSGI Application
app = Flask(__name__) # Calling this function

@app.route("/index") #it is decorator / mean Home Page. It will call below function
def index(): 
    return render_template('index.html') #where it will look for the specific templates folder
    #if the folder is not present then we will get error as the Template not found
@app.route("/") #it is decorator / mean Home Page. It will call below function
def Welcome(): 
    return "<h1>Welcome to index page</h1>"
    
@app.route("/about") #it is decorator / mean Home Page. It will call below function
def about(): 
    return render_template('about.html')

if __name__=="__main__":  # Execution basically starts from Here
    app.run(host="0.0.0.0",debug=True,port=5002) # It will run with this
