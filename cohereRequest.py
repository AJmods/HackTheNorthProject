import cohere
import json
import math
import numpy as np
from cohere.classify import Example
import re
posPhrases = ["flexible hours"]
negPhrases = ["stressful environment"]

description = "You can work whenever you want.\nMust work under pressure \nOpportunities for promotion\nPython skills required.\n flexible hours. stressful environment"

def process(description, posPhrases, negPhrases, mode="euclidean"):
    co = cohere.Client("E21STtXiw4cPKhx3a42WLxAllQ9hyT1ZwPtL5qok")
    descList = re.split(r"(?<!^)\s*[.\n]+\s*(?!$)", description)
    print(descList)
    descResponse = co.embed(texts=descList)

    posResponse = co.embed(texts=posPhrases)
    negResponse = co.embed(texts=negPhrases)

    goodScores = []

    for i in range(len(descList)):
        maxScore = -1E9
        for j in range(len(posPhrases)):
            if (mode == "euclidean"):
                curScore = np.linalg.norm(np.array(posResponse.embeddings[j]) - np.array(descResponse.embeddings[i]))
            else:
                curScore = np.dot(posResponse.embeddings[j], descResponse.embeddings[i])/(np.linalg.norm(posResponse.embeddings[j]) * np.linalg.norm(descResponse.embeddings[i]))
    ##        lst = posResponse.embeddings[j]
    ##        for k in range(len(lst)):
    ##            curScore += (lst[k]-descResponse.embeddings[i][k])**2
            if(curScore > maxScore):
                maxScore = curScore

        goodScores.append(maxScore)

    badScores = []

    for i in range(len(descList)):
        maxScore = -1E9
        for j in range(len(negPhrases)):
            if(mode=="euclidean"):
                curScore = np.linalg.norm(np.array(negResponse.embeddings[j]) - np.array(descResponse.embeddings[i]))
            else:
                curScore = np.dot(negResponse.embeddings[j], descResponse.embeddings[i])/(np.linalg.norm(negResponse.embeddings[j]) * np.linalg.norm(descResponse.embeddings[i]))
    ##        lst = negResponse.embeddings[j]
    ##        for k in range(len(lst)):
    ##            curScore += (lst[k]-descResponse.embeddings[i][k])**2
            if(curScore > maxScore):
                maxScore = curScore

        badScores.append(maxScore)

    print(goodScores)
    print(badScores)

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
    

print(process(description, posPhrases, negPhrases, "no"))