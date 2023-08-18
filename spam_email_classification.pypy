import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download stopwords corpus from NLTK
nltk.download('stopwords')

# Load the CSV file with email subjects
email_data = pd.read_csv('email_subjects.csv')
email_subjects = email_data['Subject'].tolist()

# Preprocess the email text
stop_words = set(stopwords.words('english'))
processed_texts = [' '.join([word for word in email.split() if word.lower() not in stop_words]) for email in email_subjects]

# Create a CountVectorizer to convert text into a matrix of token counts
vectorizer = CountVectorizer()

# Fit and transform the processed texts into a matrix of token counts
X_counts = vectorizer.fit_transform(processed_texts)

# Load the trained Multinomial Naive Bayes classifier
classifier = MultinomialNB()

# Replace the 'actual_labels' list with labels "spam" and "not spam"
actual_labels = ["spam", "not spam", "spam", "not spam", "spam", "not spam", "spam", "not spam", "spam", "not spam"]

# Fit the classifier
classifier.fit(X_counts, actual_labels)

# Function to classify email subjects
def classify_emails(email_texts):
    email_counts = vectorizer.transform(email_texts)
    predictions = classifier.predict(email_counts)
    return predictions

# Classify email subjects
classified_results = classify_emails(processed_texts)

# Create a results DataFrame
results_df = pd.DataFrame({'Email Subject': email_subjects, 'Classification': classified_results})

# Print the results
print(results_df)
