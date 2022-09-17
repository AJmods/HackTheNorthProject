from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

class Job:

    def __init__(self):
        pass
    def to_dict(self):
        self.rank = 1
        self.title = 'chef'
        self.company = 'lazees'
        self.description = "good shit (litterly)"
        self.pay = 9.99
        self.location = 'Waterloo, ON'
        self.apply = 'dont'

        return {
            'rank' : self.rank,
            'title' : self.title,
            'company' : self.company,
            'description' : self.description,
            'pay' : self.pay,
            'location' : self.location,
            'apply' : self.apply
        }
@app.route('/jobs')
def getJobData():
    return render_template("JobTable.html")

@app.route('/api/data/jobs')
def jobData():
    descs = [Job() for x in range(10)]
    # response
    ret = {
        'data' : [job.to_dict() for job in descs],
        'recordsFiltered': 0,
        'recordsTotal': 0,
        'draw': 0
    }
    print (ret)
    return ret

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
