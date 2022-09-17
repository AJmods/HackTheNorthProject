from flask import Flask
from flask import render_template, request
app = Flask(__name__)

positiveWords = []
negativeWords = []
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
@app.route('/jobs', methods = ["GET", "POST"])
def getJobData():
    print("hel")
    if request.method == "POST":
        positiveWords = list(request.form.to_dict(flat=False).values())[0][0].split(',')
        negativeWords = list(request.form.to_dict(flat=False).values())[1][0].split(',')
        print(positiveWords)
        print(negativeWords)
       # print(request)
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

if __name__ == '__main__':
    app.run()
