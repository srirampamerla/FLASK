### Building url dynamically
from flask import Flask,request,render_template,redirect,url_for #This render_template is responsible in redirecting to that particular HTML page.
'''
It creates an instance of the Flask Class,
which will be your WSGI(Web Server Gateway Interface) application.'''

### WSGI Application
app = Flask(__name__) # Calling this function

### jinja2 Template Engine
''' 
{{ }} expressions to print the o/p in html
{%...%} conditions,for loops
{#...#} this is comments'''

@app.route('/successres/<int:score>') #it is decorator / mean Home Page. It will call below function
def successres(score): 
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp={'score':score,"res":res} #key value pair

    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>') #it is decorator / mean Home Page. It will call below function
def successif(score): 
    return render_template('result2.html',results=score)

@app.route('/fail/<int:score>') #it is decorator / mean Home Page. It will call below function
def fail(score): 
    return render_template('result2.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))

### Building url dynamically
@app.route('/success/<int:score>') #it is decorator / mean Home Page. It will call below function
def success(score): 
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',results=res)

if __name__=="__main__":  # Execution basically starts from Here
    app.run(host="0.0.0.0",debug=True,port=5002) # It will run with this
