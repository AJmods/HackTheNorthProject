from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/jobs')
def getJobData():
    return render_template("JobTable.html")

@app.route('/api/data/jobs')
def jobData():
    descs = []
    # response
    return {
        'data' : [{'rank': 1,
          'title': "Job McJob face",
            'company': 'Lazees',
            'description': "good shit (litterly)",
            'pay': 'garlic',
            'location': 'waterloo, ON',
            'apply': 'dont'}],
        'recordsFiltered': 0,
        'recordsTotal': 0,
        'draw': 0
    }

def rankdata():
    pass
@app.route('/Products', methods=["GET", "POST"])
def displayProducts():
    return render_template('ProductsTable.html', title='Products Table', login=getEmail())

@app.route('/api/data/Products')
def Productdata():

    # response
    return {
        'data': [product.to_dict() for product in query],
        'recordsFiltered': 0,
        'recordsTotal': 0,
        'draw': 0,
    }


if __name__ == '__main__':
    app.run()
