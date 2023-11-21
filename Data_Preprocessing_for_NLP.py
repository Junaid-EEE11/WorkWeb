import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Remove HTML tags and unnecessary characters
    clean_text = re.sub('<.*?>', '', text)
    clean_text = re.sub(r'[^\w\s]', '', clean_text)

    # Tokenization
    tokens = word_tokenize(clean_text.lower())  # Convert to lowercase and tokenize

    # Normalization: Handle contractions and correct spelling (if needed)

    # Stopwords Removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return lemmatized_tokens
