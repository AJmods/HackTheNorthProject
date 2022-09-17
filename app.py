import json

from flask import Flask
from flask import render_template, request

from cohereRequest import process

app = Flask(__name__)

positiveWords = []
negativeWords = []



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

class Job:

    def __init__(self, rank=0, title='', company='', des='', pay='', location='', apply=''):
        self.rank = rank
        self.title = title
        self.company = company
        self.description = des
        self.pay = pay
        self.location = location
        self.apply = apply

    def to_dict(self):

        return {
            'rank' : self.rank,
            'title' : self.title,
            'company' : self.company,
            'description' : self.description,
            'pay' : self.pay,
            'location' : self.location,
            'apply' : self.apply
        }

def getJobs():
    jobs = []
    jobdump = json.loads(open("jobdump.json").read())

    for job in jobdump:
        j = Job(rank=0)
        try:
            j.title = job['title']
        except:
            j.title = ''
        try:
            j.company=job['company_name']
        except:
            j.company = ""
        try:
            j.description = job['description']
        except:
            continue # we don't want jobs with no description
        try:
            j.pay = job['pay']
        except:
            j.pay = -1
        try:
            j.location = job['location']
        except:
            j.location = ""
        jobs.append(j)

    return jobs

jobs = getJobs()

@app.route('/jobs', methods = ["GET", "POST"])
def getJobData():
    if request.method == "POST":
        print("POSTED")
        positiveWords = list(request.form.to_dict(flat=False).values())[0][0].split(',')
        negativeWords = list(request.form.to_dict(flat=False).values())[1][0].split(',')
        print(positiveWords)
        print(negativeWords)
        for i in range(0, 10): # len(jobs)
            print(i)
            cnt = process(jobs[i].description, positiveWords, negativeWords)
            jobs[i].rank = cnt * 10 # make it look better
            print("CNT:" + str(cnt))
       # print(request)
    return render_template("JobTable.html")

@app.route('/api/data/jobs')
def jobData():
    # try:
    #     jobs
    # except:
    #     print("Getting Ghting")
    #     jobs = getJobs()
#    print(type(jobs))
    # response
    ret = {
        'data' : [job.to_dict() for job in jobs],
        'recordsFiltered': 0,
        'recordsTotal': 0,
        'draw': 0
    }
    # print (ret)
    return ret

def rankdata():
    pass

if __name__ == '__main__':
    app.run()
