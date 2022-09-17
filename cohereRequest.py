import cohere
import json
import math
import numpy as np
import re
import os
import sklearn
from sklearn.metrics import pairwise_distances

posPhrases_ = ["remote", "remote"]
negPhrases_ = ["stressful environment", "on site"]
description_ = "Sales Internship - Summer 2023.General Information* Ref #: 20220030567 Travel Amount Required: None Job Type: Intern-Full Time Location: Atlanta - Georgia - United States, Indianapolis - Indiana - United States, Lowell - Massachusetts - United States, USA - USA - Remote, Weston - Florida - United States.\n\nDescription & Qualifications* Description Program Dates: May 22nd - August 11th About the Program UKG's Intern Academy program is dedicated to helping college students jump start their business careers at a top-ranked technology company that cares about its people. Our interns work on enriching projects that have a significant business impact on the future of our company. In addition to your day-to-day work with your team, interns get to experience our award-winning culture through mentorship, learning programs, team-building activities, networking events, and more.\n\nWe have big ideas - and need big thinkers with diverse perspectives to help us realize them. About the Sales Track UKG... is looking for interns to join our sales teams for the summer of 2023! As an intern in our sales track, you will work in various aspects of a global technology sales organization and gain cross-functional experience. You will also be a part of an intern cohort and receive additional training and business skills exposure through our Wednesday Sales Series.\n\nOur interns are placed into a variety of teams, including business development, sales operations, sales analytics, account data governance, presales, inside sales, sales consulting, or even executive relationship management. Responsibilities could include: Producing briefings on prospective accounts, industry segments, and specific business issues that help Salespeople become more informed and effective in their deals Maintaining integrity of UKG customer and prospect data in UKG's CRM platform, Salesforce Identifying target prospects for new business opportunities in specific industries Assisting in the development and implementation of the company's go-to-market strategy Conducting competitive intelligence research and presenting discoveries to sales executives Helping create, document and maintain the Sandbox/Test Drive environment where prospective customers can get a positive exposure to the UKG solution Reviewing sales processes and uncovering opportunities for automation and greater efficiency Qualifications Currently pursuing a bachelor's degree - preference will be given to rising seniors Pursuing a major in business, sales, marketing, management information systems, or another related field Able to commit to a Full time internship for 12 weeks Working knowledge of Microsoft suite, with an emphasis in Excel Experience with CRM platforms and a quick learner with new software or computer applications Excellent writing, communication, and presentation skills Strong analytical and problem-solving capabilities Strong interpersonal skills and ability to engage and connect with internal and external teams Desire to work in sales/lead development long-term NOTE: There will be a requirement to travel twice during your internship to one of our corporate headquarters for intern events. Travel expenses will be covered by UKG.\n\nUKG is unable to sponsor a new applicant for employment authorization for our internship program, including students on temporary sponsorship through CPT. All applicants must be eligible to work in the US with no restrictions. Company Overview Here at UKG, Our Purpose Is People.\n\nUKG combines the strength and innovation of Ultimate Software and Kronos, uniting two award-winning, employee-centered cultures. Our employees are an extraordinary group of talented, energetic, and innovative people who care about more than just work. We strive to create a culture of belonging and an employee experience that empowers our people.\n\nUKG has more than 13,000 employees around the globe and is known for its inclusive workplace culture. Ready to be inspired? Learn more at.www.ukg.com/careers* EEO Statement.\n\nEqual Opportunity Employer* Ultimate Kronos Group is proud to be an equal opportunity employer and is committed to maintaining a diverse and inclusive work environment. All qualified applicants will receive considerations for employment without regard to race, color, religion, sex, age, disability, marital status, familial status, sexual orientation, pregnancy, genetic information, gender identity, gender expression, national origin, ancestry, citizenship status, veteran status, and any other legally protected status under federal, state, or local anti-discrimination laws. View The EEO is the Law poster (https://www.dol.\n\ngov/ofccp/regs/compliance/posters/ofccpost.htm) and its.supplement* . View the Pay Transparency Nondiscrimination Provision (https://www.dol.gov/sites/dolgov/files/ofccp/pdf/pay-transp\\_%20English\\_formattedESQA508c.\n\npdf) UKG participates in E-Verify. View the E-Verify posters here (https://www.e-verify.gov/sites/default/files/everify/posters/EVerifyParticipationPoster.pdf) .\n\nColorado Pay Law The pay range for this position in Colorado is $ x to x (or x), however, base pay offered may vary depending on skills, experience, job-related knowledge and location. This position is also eligible for a short-term incentive and a long-term incentive as part of total compensation. Information about UKG's comprehensive benefits can be reviewed on our careers site at https://www.ukg.com/careers .\n\nThis information is provided per the Colorado Equal Pay for Equal Work Act Disability Accommodation* For individuals with disabilities that need additional assistance at any point in the application and interview process, please email UKGCareers@ukg.com"

def process(description, posPhrases, negPhrases):
    co = cohere.Client(os.environ['COHERE_API_KEY'])
    descList = [description, description]
    descResponse = co.embed(texts=descList)
    testResponse = co.embed(texts=["remote", "remote"])

    posResponse = co.embed(texts=posPhrases)
    negResponse = co.embed(texts=negPhrases)

    goodScore = 0
    curScore = sklearn.metrics.pairwise.cosine_distances(np.array(posResponse.embeddings), np.array(descResponse.embeddings))
    goodScore = np.sum(curScore)
    goodScore = (goodScore/(float)(len(posPhrases)))

    badScore = 0

    curScore = sklearn.metrics.pairwise.cosine_distances(negResponse.embeddings, descResponse.embeddings)

    badScore = np.sum(curScore)
    badScore += badScore/(float)(len(negPhrases))


    totalScore = badScore - goodScore

    return totalScore
    

