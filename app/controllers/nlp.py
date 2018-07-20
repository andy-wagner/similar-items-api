import nltk, string


def stem_tokens(tokens):
    """
    NlP helper method that helps stemming tokens
    :param tokens:
    :return: stemmed tokens
    """
    stemmer = nltk.stem.porter.PorterStemmer()
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    """
    Normalizer
    :param text:
    :return:
    """
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


def cosine_sim(text1, text2, vectorizer):
    """
    Calculates Cosine Similarity between two strings
    :param text1:
    :param text2:
    :param vectorizer:
    :return: measure of similarity in 0-1 scale where 1 is most similar
    """
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]
