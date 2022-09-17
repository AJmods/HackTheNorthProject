import json

def processJobs():

    # load jobs directly from file
    jobdump = json.loads(open("jobdump.json").read())

    des = []

    for job in jobdump:
        
        # sample data
        print(f"{job['title']} at {job['company_name']} ({'location'})")
        try:
            print(f"icon: {job['thumbnail']}")
        except:
            print("no thumbnail")
        try:
            des.append(job['description']) # pass this into cohere
        except:
            print('no des')
        
        # for key, value in job['detected_extensions']:
        #     print(f"{key}: {value}")

    print(des)

processJobs()