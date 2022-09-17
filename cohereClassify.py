import cohere
import re
from cohere.classify import Example

def classify(description):
    co = cohere.Client("E21STtXiw4cPKhx3a42WLxAllQ9hyT1ZwPtL5qok")
    descList = re.split(r"(?<!^)\s*[.\n]+\s*(?!$)", description)
    #print(descList)
    response = co.classify(inputs=descList, examples=[Example("Work uniform", "Company Culture"),
                                                    Example("Mandatory Party", "Company Culture"),
                                                       Example("Casual atmosphere", "Company Culture"),
                                                       Example("Fast-paced culture", "Company Culture"),
                                                       Example("Dynamic team", "Company Culture"),
                                                       Example("Competitive compensation", "Wages"),
                                                       Example("$20 hourly rate", "Wages"),
                                                       Example("Annual salary of $50000", "Wages"),
                                                       Example("$2000 sign-on bonus", "Wages"),
                                                       Example("Minimum wage", "Wages"),
                                                       Example("dental insurance", "Benefits"),
                                                       Example("No paid time off", "Benefits"),
                                                       Example("Paid statutory holidays", "Benefits"),
                                                       Example("3 days sick leave", "Benefits"),
                                                       Example("2 weeks paid vacation", "Benefits")])                                        
    classes = []
    for i in response:
        classes.append(i.prediction)
    #print(classes)
    return classes

classify("competitive wages \n paid holidays \n no sick leave \n opportunity for promotion\n $20 hourly rate.Pizza party.Dynamic atmosphere")
