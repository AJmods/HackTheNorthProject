from serpapi import GoogleSearch
import os

print (os.environ)

def queryJobs(job_title, location, page):
    params = {
        "q" : job_title,
        "location" : location,
        "engine" : "google_jobs",
        "api_key" : os.environ['SERP_API_KEY'],
        "start" : page * 10 # pages counted in multiples of 10
    }

    search = GoogleSearch(params)
    return search.get_dict()

def processJobs(jobs_dict):
    for job in jobs_dict["jobs_results"]:
        print(f"{job['description']}") # feed this to cohere
        # print(f"{job['title']} at {job['company_name']} ({job['location']})")
        # job["thumbnail"] is available - can this be used for frontend?

jobs_dict = queryJobs("Internship", "Waterloo", 0)
processJobs(jobs_dict)