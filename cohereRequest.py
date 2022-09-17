import cohere
import json
import math
import numpy as np
import re
import os

posPhrases = ["flexible hours"]
negPhrases = ["stressful environment"]

description = "You can work whenever you want.\nMust work under pressure \nOpportunities for promotion\nPython skills required.\n flexible hours. stressful environment"

def process(description, posPhrases, negPhrases, mode="euclidean", select="extreme"):
    #co = cohere.Client(os.environ['COHERE_API_KEY'])
    co = cohere.Client('w9AvvvtW3mawGpvlCrm5FXxxnWBEsDOLkQpSSfCN')
    descList = re.split(r"(?<!^)\s*[.\n]+\s*(?!$)", description)
    #print(descList)
    descResponse = co.embed(texts=descList)

    posResponse = co.embed(texts=posPhrases)
    negResponse = co.embed(texts=negPhrases)

    goodScores = []

    for i in range(len(descList)):
        if(select == "extreme"):
            minScore = 1E9
        else:
            minScore = 0
        for j in range(len(posPhrases)):
            if (mode == "euclidean"):
                curScore = np.linalg.norm(np.array(posResponse.embeddings[j]) - np.array(descResponse.embeddings[i]))
            else:
                curScore = np.dot(posResponse.embeddings[j], descResponse.embeddings[i])/(np.linalg.norm(posResponse.embeddings[j]) * np.linalg.norm(descResponse.embeddings[i]))

            if(select == "extreme" and curScore < minScore):
                minScore = curScore
            else:
                minScore += curScore
        if(select == "extreme"):
            goodScores.append(minScore)
        else:
            goodScores.append(minScore/(float)(len(posPhrases)))

    badScores = []

    for i in range(len(descList)):
        if(select == "extreme"):
            minScore = 1E9
        else:
            minScore = 0
        for j in range(len(negPhrases)):
            if(mode=="euclidean"):
                curScore = np.linalg.norm(np.array(negResponse.embeddings[j]) - np.array(descResponse.embeddings[i]))
            else:
                curScore = np.dot(negResponse.embeddings[j], descResponse.embeddings[i])/(np.linalg.norm(negResponse.embeddings[j]) * np.linalg.norm(descResponse.embeddings[i]))

            if(select == "extreme" and curScore < minScore):
                minScore = curScore
            else:
                minScore += curScore
        if(select == "extreme"):
            badScores.append(minScore)
        else:
            badScores.append(minScore/(float)(len(negPhrases)))

    #print(goodScores)
    #print(badScores)

    totalScore = 0

    sentenceScores = []

    for i in range(len(descList)):
        if(mode=="euclidean"):
            if(goodScores[i] < badScores[i] and (goodScores[i] < 100)):
                sentenceScores.append("good")
                totalScore += 1
            elif(badScores[i] < goodScores[i] and (badScores[i] < 100)):
                sentenceScores.append("bad")
                totalScore -= 1
            else:
                sentenceScores.append("neutral")
        else:
            if(goodScores[i] > badScores[i] and (goodScores[i] > 0.55)):
                sentenceScores.append("good")
                totalScore += 1
            elif(badScores[i] > goodScores[i] and (badScores[i] > 0.55)):
                sentenceScores.append("bad")
                totalScore -= 1
            else:
                sentenceScores.append("neutral")

    return sentenceScores, totalScore
    

#n
print(process(description, posPhrases, negPhrases, "euclidean", "avg"))
