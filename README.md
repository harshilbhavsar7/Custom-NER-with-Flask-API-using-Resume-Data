# Custom-NER-with-Flask-API-using-Resume-Data
This project is all about the developing custom NER model using Resume data. I have also developed the Flask API which consumes the model and gives output by using the frontend. 


Our goal was to build a webform in Flask in which we provide raw text, for example, a person’s data (or any article) as input and our trained custom model will then identify and extract the named entities such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc. 

The overwhelming amount of unstructured text data available today provides a rich source of information if the data can be structured. Named-entity Recognition (NER)(also known as Named-entity Extraction) is one of the first steps to build knowledge from semi-structured and unstructured text sources.

Firstly, We have developed the NER model using Spacy in python. And then developed the API using the Flask. Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. 

Spacy is an open-source Natural Language Processing library that can be used for various tasks. It has built-in methods for Named Entity Recognition. Spacy has a fast statistical entity recognition system.

We can use spacy very easily for NER tasks. Though often we need to train our own data for business-specific needs, the spacy model generally performs well for all types of text data.  

There are other libraries as well for performing NER task such as NLTK, coreNLP, Gensim and many more, but as spacy provides a quick and efficient solution to our problem statement, we have used that.

For training the model we have used Resume dataset from Kaggle which contains 220 annotated resume’s.The data contains text and entities with its start and end indexes in the text, which marks its belonging into the text. However, the annotated data is not in the format required in spacy training, so in the first step we have done the model preprocessing to convert the data into the suitable format.

For training our custom named entity model for resumes we first created a blank spacy model and created a pipeline for NER.

We will only train the ner component of the model in the model training, first we will create an example object with the document and annotations and update the model while calculating losses.

To build the custom ner webpage in Flask Framework, we will need to create two files.
1. ner_home.html which is our template for input and output.
2. app.py to handle the requests and return the output file.

Ner_home contains the webpage layout code. Which will show us the inference result generated by the ner model by calling the API which loads our custom model and runs the inference over the user input

Our app.py file is rather simple and easy to understand. It contains the main code that will be executed by the Python interpreter to run the Flask web application, it includes the spaCy code for recognizing named entities.

https://www.analyticsvidhya.com/blog/2021/06/nlp-application-named-entity-recognition-ner-in-python-with-spacy/
https://towardsdatascience.com/building-a-flask-api-to-automatically-extract-named-entities-using-spacy-2fd3f54ebbc6 
https://www.fullstackpython.com/flask.html 
https://www.kaggle.com/datasets/amarsharma768/dataset-for-resume-information-retrieval
