from flask import Flask, render_template, url_for, redirect
from flask import request
import csv
app = Flask(__name__)

print(__name__)

@app.route('/index.html')
def myHome():
    return render_template('index.html')


@app.route('/<string:pageName>')
def htmlPage(pageName):
    return render_template(pageName)


@app.route('/submitForm', methods=['POST', 'GET'])
def submitForm():
    
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            writeToFile(data)
            writeToCSV(data)
            return redirect('thankyou.html')
        except:
            return "Something Wrong has happened. Did not store to database."
    else:
        return 'Something went wrong. Try Again'
    

def writeToFile(data):
    with open('./database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email}, {subject}, {message}")

def writeToCSV(data):
    with open('./database.csv', mode='a') as databaseCSV:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csvWriter = csv.writer(databaseCSV,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow([email, subject, message])