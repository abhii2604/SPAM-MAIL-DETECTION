# -*- coding: utf-8 -*-
"""spammaildetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kiX66aMeegpIluVAeotmO-bGfw2w4Yxq
"""

!pip install pandas scikit-learn nltk

!wget https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip
!unzip smsspamcollection.zip
!mv SMSSpamCollection spam.csv

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import nltk
from nltk.corpus import stopwords
import string

# Load the dataset
df = pd.read_csv('spam.csv', sep='\t', header=None, names=['label', 'text'])

# Display the first few rows of the dataset
print(df.head())

# Download stopwords
nltk.download('stopwords')

# Define a function to preprocess the text
def preprocess_text(text):
    # Remove punctuation
    text = "".join([char for char in text if char not in string.punctuation])
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    text = " ".join([word for word in text.split() if word not in stopwords.words('english')])
    return text

# Apply the preprocessing function to the text column
df['processed_text'] = df['text'].apply(preprocess_text)

# Display the first few rows of the preprocessed dataset
print(df.head())

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the processed text data
X = vectorizer.fit_transform(df['processed_text'])

# Encode the labels as binary values
y = df['label'].map({'ham': 0, 'spam': 1})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Multinomial Naive Bayes model
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Display the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

# Display the classification report
class_report = classification_report(y_test, y_pred)
print('Classification Report:')
print(class_report)

# Install necessary libraries
!pip install pandas scikit-learn nltk

# Download the dataset
!wget https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip
!unzip smsspamcollection.zip
!mv SMSSpamCollection spam.csv

# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import nltk
from nltk.corpus import stopwords
import string

# Load the dataset
df = pd.read_csv('spam.csv', sep='\t', header=None, names=['label', 'text'])

# Display the first few rows of the dataset
print(df.head())

# Download stopwords
nltk.download('stopwords')

# Define a function to preprocess the text
def preprocess_text(text):
    # Remove punctuation
    text = "".join([char for char in text if char not in string.punctuation])
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    text = " ".join([word for word in text.split() if word not in stopwords.words('english')])
    return text

# Apply the preprocessing function to the text column
df['processed_text'] = df['text'].apply(preprocess_text)

# Display the first few rows of the preprocessed dataset
print(df.head())

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the processed text data
X = vectorizer.fit_transform(df['processed_text'])

# Encode the labels as binary values
y = df['label'].map({'ham': 0, 'spam': 1})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Multinomial Naive Bayes model
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Display the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

# Display the classification report
class_report = classification_report(y_test, y_pred)
print('Classification Report:')
print(class_report)