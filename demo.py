from flask import Flask,render_template,request
 
app = Flask(__name__)

@app.route('/' )
def website():
 return render_template("index.html")
app.run()
          
