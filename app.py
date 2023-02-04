from flask import Flask,request,render_template
import spacy
from spacy.scorer import Scorer
from spacy.tokens import SpanGroup
import pandas as pd


app = Flask(__name__)

# @app.route("/")
# def hello_world():

#     return "Hello, World!"


@app.route('/')
def index():
    return render_template("ner_home.html")

@app.route("/process", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text= request.form["input_data"]
        # model = None
        resume_model = spacy.load(r'C:\Harshil\Study\Python Programming\Python_Project\resume_ner_model')
        doc= resume_model(text) 

        entities_data = [(ent.text, ent.label_) for ent in doc.ents]
        print(entities_data)
        num_of_results = len(entities_data)

    return render_template("ner_home.html",results=entities_data,num_of_results = num_of_results)

if __name__ == '__main__':
  # app.debug = True
  app.run(host='0.0.0.0', port=5000, debug=True)