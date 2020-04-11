import nltk
from nltk.corpus import treebank
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from pprint import pprint
def tagging(sentences):
    tokens = []
    tagged = []
    for sentence in sentences:
        tokens.append(nltk.word_tokenize(sentence))
    for toks in tokens:
        tagged.append(nltk.pos_tag(toks))
    for taggedSentence in tagged:
        print (taggedSentence)
    
    
def main():
    reviewFile = "review-data.txt"
    reviewData = open(reviewFile)
    text = reviewData.readline();
    sentences = nltk.sent_tokenize(text)
    tagging(sentences)
    
if __name__ == "__main__":
    main()