# 📌 Import libraries
import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('wordnet')

# 📌 Load dataset
df = pd.read_csv("IMDB Dataset.csv")
print(df.head())

# 📌 Text cleaning function
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ''.join([i for i in text if not i.isdigit()])
    words = text.split()
    # Remove stopwords
    words = [w for w in words if w not in stop_words]
    # Apply stemming
    words_stemmed = [ps.stem(w) for w in words]
    # Apply lemmatization
    words_lemmatized = [lemmatizer.lemmatize(w) for w in words]
    return ' '.join(words_lemmatized)

# 📌 Apply cleaning
df['cleaned_review'] = df['review'].apply(clean_text)
df.to_csv("imdb_cleaned_reviews.csv", index=False)

# 📌 Word Frequency
all_words = []
df['cleaned_review'].apply(lambda x: all_words.extend(x.split()))
word_freq = Counter(all_words)
print(word_freq.most_common(10))

# 📌 WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("WordCloud of IMDB Reviews")
plt.show()