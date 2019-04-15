from flask import Flask,render_template,request
from main import startApp
import os,json
app = Flask(__name__,static_url_path='/static')

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/getData",methods=['GET', 'POST'])
def getData():
    if request.method == "POST":
        logFile = request.files['file']
        logPath = os.path.join(os.getcwd(),'logs',logFile.filename[:16])
        if os.path.exists(logPath) is False:
            os.mkdir(logPath)
        filename = os.path.join(logPath,logFile.filename)
        logFile.save(filename)
        issueTime = request.form['issueTime']
        searchSpan = request.form['searchSpan']
        print("File Uploaded successfully! Parsing logs..")
        jsList = startApp(filename,logPath,issueTime,searchSpan)
        
    #return ("success")    
    return render_template('browserUI.html',data=json.dumps(jsList))

if __name__ == "__main__":
    app.run(debug = True)