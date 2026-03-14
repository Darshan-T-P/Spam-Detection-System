def preprocess(df):

    df.columns = df.columns.str.lower().str.strip()

    df = df.dropna()

    X = df["content"]
    y = df["class"]

    return X,y