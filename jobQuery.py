import json

def processJobs():

    # load jobs directly from file
    jobdump = json.loads(open("jobdump.json").read())

    for job in jobdump:
        
        # sample data
        print(f"{job['title']} at {job['company_name']} ({'location'})")
        print(f"icon: {job['thumbnail']}")
        print(job['description']) # pass this into cohere
        
        for key, value in job['detected_extensions']:
            print(f"{key}: {value}")

        pass

processJobs()