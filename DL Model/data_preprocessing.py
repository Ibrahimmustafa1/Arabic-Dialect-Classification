# data_preprocessing.py

import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')

arabic_stopwords = set(stopwords.words('arabic'))

def remove_emojis(text):
    emoji_pattern = re.compile(
        "["  # Start of the pattern
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002500-\U00002BEF"  # chinese char
        "\U00002702-\U000027B0"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\u3030"
        "\ufe0f"
        "\u2069"
        "\u2066"
        "\u200c"
        "\u2067"
        "\u2068"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", text)

def preprocess_text(text):
    text = remove_emojis(text)
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = re.sub(r'\s+', ' ', text)  # remove extra whitespace
    text = text.strip()
    return text

def preprocess_dataframe(df):
    df['text'] = df['text'].apply(preprocess_text)
    df = df.drop('id', axis=1)
    return df
