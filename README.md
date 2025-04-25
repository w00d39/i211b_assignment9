## i211b_assignment9


# Overview
This Python script performs text analysis on four different texts to extract features, named entities, and n-grams. It uses Natural Language Toolkit (NLTK) to process the texts and determine stylistic similarities between them. The primary goal is to identify the likely author of a fourth, unknown text (Text_4.txt) by comparing its features and n-grams with those of three known authors: Lovecraft, Martin, and Tolkien.

# Dependencies
The script relies on the following Python libraries:

nltk: For text processing, tokenization, lemmatization, stemming, and named entity recognition.
string: For handling punctuation.
FreqDist (from nltk.probability): For frequency distribution of tokens and n-grams.
Required NLTK Data
Before running the script, ensure the following NLTK data packages are downloaded:
- punkt
- stopwords
- wordnet
- maxent_ne_chunker
- words

# File Structure
Functions
1. extract_features(text)
Description: Extracts features from the text by removing stop words, punctuation, and applying lemmatization and stemming.
Input: A string of text.
Output: A list of processed tokens.
2. named_entities(text)
Description: Extracts named entities from the text using NLTK's ne_chunk.
Input: A string of text.
Output: A tree structure containing named entities.
3. ngrams(text, n=3)
Description: Generates n-grams from the text and returns the most common ones.
Input: A string of text and the value of n (default is 3 for trigrams).
Output: A list of the most common n-grams and their frequencies.
4. compare(ngram1, ngram2)
Description: Compares two sets of n-grams and calculates the overlap.
Input: Two lists of n-grams.
Output: The number of overlapping n-grams and the overlapping n-grams themselves.

# Workflow
Read Texts:

The script reads four text files: RJ_Lovecraft.txt, RJ_Martin.txt, RJ_Tolkien.txt, and Text_4.txt.
Feature Extraction:

Extracts features (tokens) from each text using extract_features.
Named Entity Recognition:

Extracts named entities from each text using named_entities.
N-Gram Analysis:

Generates trigrams (n=3) for each text using ngrams.
Comparison:

Compares the trigrams of Text_4.txt with those of the other texts using compare.
Authorship Attribution:

Determines the likely author of Text_4.txt based on the overlap of trigrams.

# How to Run the Script
Prepare the Text Files:

Place the following text files in the same directory as the script:
RJ_Lovecraft.txt
RJ_Martin.txt
RJ_Tolkien.txt
Martin.txt
Run the Script:

Execute the script in a Python environment:
python assignment9.py

# View the Results:

The script will output:
- frequency distributions for the first three texts
- named entities of the first three texts
- the overlapping ngrams for each text compared to the fourth text
- which has the most overlapping ngrams is the author of the text, but may also be inconclusive if all are 0

# Customization
Change n for N-Grams:

Modify the n parameter in the ngrams function to analyze bigrams (n=2), trigrams (n=3), or higher-order n-grams.
Adjust Output:

Use FreqDist.pformat(maxlen=20) to control the number of displayed n-grams.

# Limitations
Text Preprocessing:

The script assumes clean input text. Additional preprocessing may be required for noisy data.
Authorship Attribution:

The method relies on stylistic similarities in n-grams, which may not always be conclusive.
Named Entity Recognition:

NER accuracy depends on the quality of the input text and the NLTK model.
