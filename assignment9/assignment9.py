import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import pos_tag, ne_chunk
import string


# download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('maxent_ne_chunker_tab')
# nltk.download('words')

def extract_features(text):
    """
    Extract features from the text by removing stop words, punctuation, and applying lemmatization and stemming.
    """
    stop_words = set(stopwords.words('english'))

    #punctuation removal
    text_no_punctuation = ''.join(char for char in text if char not in string.punctuation)

    #word tokenization
    words = word_tokenize(text_no_punctuation.lower())
    filtered_words = [word for word in words if word not in stop_words]


    #lemmatising
    lemmatizer = nltk.stem.WordNetLemmatizer()
    filtered_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    #stemming
    stemmer = nltk.stem.PorterStemmer()
    filtered_words = [stemmer.stem(word) for word in filtered_words]

    return filtered_words

def named_entities(text):
    """
    Extract named entities from the text.
    """
    # Tokenize the text
    stop_words = set(stopwords.words('english'))

    #punctuation removal
    text_no_punctuation = ''.join(char for char in text if char not in string.punctuation)

    #word tokenization
    words = word_tokenize(text_no_punctuation.lower())
    tokens = [word for word in words if word not in stop_words]
    
    # POS tagging
    pos_tags = pos_tag(tokens)
    
    # Named entity recognition
    named_entities = ne_chunk(pos_tags)
    
    return named_entities

def ngrams(text, n = 3,):
    """
    Generate n-grams from the text.
    """
    # Tokenize the text
    stop_words = set(stopwords.words('english'))

    #punctuation removal
    text_no_punctuation = ''.join(char for char in text if char not in string.punctuation)

    #word tokenization
    words = word_tokenize(text_no_punctuation.lower())
    filtered_words = [word for word in words if word not in stop_words]

     #lemmatising
    lemmatizer = nltk.stem.WordNetLemmatizer()
    filtered_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    #stemming
    stemmer = nltk.stem.PorterStemmer()
    filtered_words = [stemmer.stem(word) for word in filtered_words]


    # Generate n-grams
    n_grams = list(nltk.ngrams(filtered_words, n))

    freq_dist = FreqDist(n_grams)
    
    return freq_dist.most_common(30)

def compare(ngram1, ngram2):
    set1 = set(ngram for ngram, _ in ngram1) #this is the most common ngrams for the first text 
    set2 = set(ngram for ngram, _ in ngram2) #this is the most common ngrams for the second text
    common_ngrams = set1.intersection(set2) #this is the shared ngrams between the two texts
    return len(common_ngrams), common_ngrams #returns the number of common ngrams and the common ngrams themselves


#texts 1,2,3 
with open('RJ_Lovecraft.txt', 'r') as lovecraft_file: #reading the txt
    lovecraft = lovecraft_file.read()
    lovecraft_features = extract_features(lovecraft) #extracting the features from the text
    lovecraft_entities = named_entities(lovecraft) #extracting the named entities from the text
    lovecraft_ngrams = ngrams(lovecraft) #extracting the ngrams from the text

with open('RJ_Martin.txt', 'r') as martin_file: #reading the txt
    martin = martin_file.read()
    martin_features = extract_features(martin) #extracting the features from the text
    martin_entities = named_entities(martin) #extracting the named entities from the text
    martin_ngrams = ngrams(martin) #extracting the ngrams from the text

with open('RJ_Tolkein.txt', 'r') as tolkien_file: #reading the txt
    tolkien = tolkien_file.read()
    tolkien_features = extract_features(tolkien) #extracting the features from the text
    tolkien_entities = named_entities(tolkien) #extracting the named entities from the text
    tolkein_ngrams = ngrams(tolkien) #extracting the ngrams from the text

with open('martin.txt', 'r') as martin_file: #reading the 4th txt 
    txt4 = martin_file.read()
    txt4features = extract_features(txt4) #extracting the features from the text
    txt4_entities = named_entities(txt4) #extracting the named entities from the text
    txt4_ngrams = ngrams(txt4) #extracting the ngrams from the text
#



# Uncomment the following lines to see the frequency distribution of the features
# lovecraft_freq = FreqDist(lovecraft_features)
# print(lovecraft_freq.pformat(maxlen = 20))


# martin_freq = FreqDist(martin_features)
# print(martin_freq.pformat(maxlen = 20))


# tolkein_freq = FreqDist(tolkien_features)
# print(tolkein_freq.pformat(maxlen = 20))



#uncomment the following lines to see the named entities
#named entities
# print("Named Entities in Lovecraft's text:")
# print(lovecraft_entities)
# print("\nNamed Entities in Martin's text:")
# print(martin_entities)
# print("\nNamed Entities in Tolkien's text:")
# print(tolkien_entities)


#Comparing the ngrams to see the author of txt4

lovecraft_len_overlap, lovecraft_overlap = compare(lovecraft_ngrams, txt4_ngrams)
martin_len_overlap, martin_overlap = compare(martin_ngrams, txt4_ngrams)
tolkein_len_overlap, tolkein_overlap = compare(tolkein_ngrams, txt4_ngrams)

# Determine the likely author
print(lovecraft_len_overlap, lovecraft_overlap)
print(martin_len_overlap, martin_overlap)
print(tolkein_len_overlap, tolkein_overlap)