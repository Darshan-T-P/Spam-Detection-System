import pandas as pd
import zipfile

def load_data():

    z = zipfile.ZipFile("data/youtube+spam+collection.zip")

    psy=pd.read_csv(z.open("Youtube01-Psy.csv"))
    katy=pd.read_csv(z.open("Youtube02-KatyPerry.csv"))
    LMFAO=pd.read_csv(z.open("Youtube03-LMFAO.csv"))
    Eminem=pd.read_csv(z.open("Youtube04-Eminem.csv"))
    Shakira=pd.read_csv(z.open("Youtube05-Shakira.csv"))

    df = pd.concat([psy,katy,LMFAO,Eminem,Shakira])

    return df