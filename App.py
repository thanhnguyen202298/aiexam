from openai import OpenAI
from datasets import load_dataset
import os

import asyncio
import pandas as pd
import json
from datetime import datetime
from core import aicore

########################################
#########TODO 1  #######################
########################################
########################################

filename = "BTC.csv"

def connectDataFile(file):
    df = None
    if file != None:
        df = pd.read_csv(f"raw_data/{file}")
    else:
         df = pd.read_csv(f"raw_data/{filename}")
    return df


def row2Q(date):
    dateval = datetime.strptime(date, "%Y-%m-%d").date()
    return {
        "role": "user",
        "content": f"how price is BTC in {dateval.strftime('%d %B, %Y')}?",
    }

def row2A(datef, low, high, open, close):
    dateval = datetime.strptime(datef, "%Y-%m-%d").date()
    return {
        "role": "assistant",
        "content": f"""BTC's price in {dateval.strftime('%d %B, %Y')} is:\n 
        open: {open}
        close: {close}
        high: {high}
        low: {low}
        """,
    }

#df = connectDataFile()

##########################
##########################
####### CSV TO QUESTION ##
########### ANSWER #######
##########################

def data2QA():
    dataset = []
    size = len(df.date)
    for i in range(0, size):
        d = df.date[i]
        dataset.append(row2Q(d))
        dataset.append(row2A(d, df.low[i], df.high[i], df.open[i], df.close[i]))

    return dataset

client = OpenAI()

def convertRawData2QA(non_qa_data):
    response = client.completions.create(
        model="text-davinci-002",  # Hoặc sử dụng engine phù hợp
        prompt=non_qa_data,
        max_tokens=150,
    )
    print(response.choices[0].text.strip())
    return response.choices[0].text.strip()


###########################################
###########################################
############ create data question answer ##
###########################################
###########################################

def data2file(data):

    with open(f"json/{filename[0:-4]}{datetime.now().strftime('%f')}.json", "w") as output:
        output.write(data)

def createDataQuestionJsonAI():
    data = data2QA()

    objectdata = json.dumps(data, indent=4)

    with open(f"json/{filename[0:-4]}.json", "w") as output:
        output.write(objectdata)


richData = []


def repeatQuestionGetMoreAnswer(indexQ, data):
    richData.append(data[indexQ])
    df


############################################
############################################
############ Make Rich Data question #######
############################################
############################################
def makeGrowDataRich():
    with open(f"json/{filename[0:-4]}.json", "r") as objectFile:
        data = json.load(objectFile)
        size = len (data)
        for i in range(0,-2,2):
            
