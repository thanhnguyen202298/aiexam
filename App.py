import openai
from datasets import load_dataset
import os

import pandas as pd
import json
from datetime import datetime

########################################
#########TODO 1  #######################
########################################
########################################

filename = "BTC.csv"
def connectDataFile():
    df = pd.read_csv(f"raw_data/{filename}")
    return df

def row2Q(date):
    dateval = datetime.strptime(date, "%Y-%m-%d").date()
    return {
        "role": "user", "content": f"how price is BTC in {dateval.strftime('%d %B, %Y')}?"
    }


def row2A(datef, low, high, open, close):
    dateval = datetime.strptime(datef, "%Y-%m-%d").date()
    return {
        "role": "assistant", "content": f"""BTC's price in {dateval.strftime('%d %B, %Y')} is:\n 
        open: {open}
        close: {close}
        high: {high}
        low: {low}
        """
    }

def data2QA():
    df = connectDataFile()
    dataset = []
    size = len(df.date)
    for i in range(0, size):
        d = df.date[i]
        dataset.append(row2Q(d))
        dataset.append(row2A(d, df.low[i], df.high[i], df.open[i], df.close[i]))

    return dataset

def createDataQuestionJsonAI():

    data = data2QA()

    objectdata= json.dumps(data, indent=4)

    with open(f"json/{filename[0:-4]}.json", "w") as output:
        output.write(objectdata)

def makeGrowDataRich():
    with open(f"json/{filename[0:-4]}.json", "r") as objectFile:
        data = json.load(objectFile)
        print(type(data))

makeGrowDataRich()