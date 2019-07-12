import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
input_str="Check for default view of Latam 10 Delta Global Page availability on product page when login as MA/Broker/Trader"
input_str=word_tokenize(input_str)
for word in input_str:
    print(lemmatizer.lemmatize(word))