import mlflow
import mlflow.sklearn
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

from data_ingestion import load_data
from preprocess import preprocess

df = load_data()

X,y = preprocess(df)

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

pipeline = Pipeline([
    ("tfidf",TfidfVectorizer()),
    ("model",MultinomialNB())
])

mlflow.start_run()

pipeline.fit(X_train,y_train)

acc = pipeline.score(X_test,y_test)

mlflow.log_param("model","NaiveBayes")
mlflow.log_metric("accuracy",acc)

joblib.dump(pipeline,"models/model.pkl")

mlflow.sklearn.log_model(pipeline,"model")

mlflow.end_run()

print("Accuracy:",acc)