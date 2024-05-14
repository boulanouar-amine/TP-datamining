import streamlit as st
import nltk
from nltk import FreqDist
from nltk.stem import PorterStemmer
from nltk import bigrams, FreqDist
import pandas as pd

comments_df = pd.read_csv('cleaned_comments.csv')

# Tokenize the text into words
words = [word for comment in comments_df['comment'] for word in nltk.word_tokenize(comment)]

# Generate bigrams
bigram_list = list(bigrams(words))

# Create a frequency distribution of the bigrams
bigram_freq = FreqDist(bigram_list)

# Initialize the stemmer
stemmer = PorterStemmer()


def get_most_common_bigram_stemmed(text):
    # Stem the input text
    stemmed_text = ' '.join([stemmer.stem(word) for word in nltk.word_tokenize(text)])

    # Get the last word of the stemmed text
    last_word = stemmed_text.split()[-1]

    # Find all bigrams that start with the last word
    bigrams_starting_with_last_word = [bigram for bigram in bigram_list if stemmer.stem(bigram[0]) == last_word]

    # Create a frequency distribution of these bigrams
    bigram_freq_local = FreqDist(bigrams_starting_with_last_word)

    # Get the three most common bigrams
    most_common_bigrams = bigram_freq_local.most_common()

    # Extract the next word, the bigram, and the frequency for each bigram
    most_common_bigrams_df = [(stemmer.stem(bigram[0][1]), ' '.join(bigram[0]), bigram[1]) for bigram in
                              most_common_bigrams]

    # Create a DataFrame from the most common bigrams
    df = pd.DataFrame(most_common_bigrams_df, columns=['Next Word', 'Bigram', 'Frequency'])

    return df
# Streamlit code
st.title('Most Common Bigram Finder')

user_input = st.text_input("Enter your text here")

if user_input:
    result_df = get_most_common_bigram_stemmed(user_input)
    st.dataframe(result_df)