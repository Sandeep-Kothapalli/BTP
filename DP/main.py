import nltk
import re
# all codes are run with python 3.7
# pretty print function for visualisation of the tree cannot be used with python 3.8
# install nltk using pip
# uncomment the two lines below for the first time you run the code
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# from cgi import escape
from pprint import pprint
# from en import singular
# from pattern.text.en import singularize
from nltk.stem.snowball import SnowballStemmer
# stemmer is useful but not right now.
from nltk.treeprettyprinter import TreePrettyPrinter
from nltk.parse import CoreNLPParser
from nltk.parse.corenlp import CoreNLPDependencyParser
coreNLPurl = 'http://corenlp.run/'
localServer = 'http://localhost:9000'
# use local server with desired port number in case you cant use corenlp.run
dependencyParser = CoreNLPDependencyParser(url=coreNLPurl)
stemmer = SnowballStemmer("english")
Parser = CoreNLPParser(url=coreNLPurl)

def main():
    reviewFile = "review-data.txt"
    reviewData = open(reviewFile)
    text = reviewData.readline()
    sentences = nltk.sent_tokenize(text)
    # dependency graph contains the dep graph in triples for each sentence
    # for sentence in sentences:
    #     print()
    #     print(sentence)
    #     print()
    #     res, = dependencyParser.raw_parse(sentence)
    #     for a,b,c in res.triples():
    #         # print(a,b,c)
    #         print(a[0], a[1], b, c[0], c[1])

    print("=========================================================================")
    O = ["great"] #opinion wordd dictionary
    print("Initial Opinion Lexicon ")
    print(O)
    print("=========================================================================")
    O_Expanded = O  #expanded opinion lexicon
    F = [] #all possible features
    MR = ['mod', 'pnmod', 'subj', 's','obj', 'obj2' , 'desc', 'amod', 'nsubj']
    JJ = ['JJ', 'JJR', 'JJS']
    NN = ['NN', 'NNS', 'NNP']
    CONJ = ['conj']
    CC = ['CC']
    CoCONJ = ['cc']
    F_i = []
    O_i = []
    O_prime = []
    F_prime = []
    while(len(F_i) == 0 & len(O_i) == 0) :
        F_i = []
        O_i = []
        O_prime = []
        F_prime = []
        for sentence in sentences:
            res, = dependencyParser.raw_parse(sentence);
            for a,b,c in res.triples():
                # if (c[0] in O_Expanded) & (b in MR) & (a[1]in NN) & (a[0] not in F):
                if b in MR:
                    if((a[1] in NN) & (a[0] not in F)) :
                        F_i.append(a[0]) 
                    elif ((c[1] in NN) & (c[0] not in F)) :
                        F_i.append(c[0]) 
                    # print(a[0], a[1], b, c[0], c[1])
        F = F+F_i
        O_Expanded = O_Expanded+O_i
        # handled a case specifically for coordinating conjunctions
        for sentence in sentences:
            res, = dependencyParser.raw_parse(sentence)
            for a,b,c in res.triples():
                if(b in CoCONJ) :
                    for x,y,z in res.triples():
                        if(x[0]==a[0]) & (y in CONJ):
                            F_prime.append(z[0]) 
                            
                if (a[0] not in O_Expanded) & (a[1] in JJ) & (b in MR):
                    for f in F_i:
                        if(f.startswith(c[0]) or c[0].startswith(f)):
                            O_prime.append(a[0]) 
                            # break
        F_i = F_i+F_prime
        O_i = O_i+O_prime
        F = list(set(F+F_prime))
        O_Expanded = list(set(O_Expanded+O_prime))
    # remove plurals
    for feature in F:
        stemmer.stem(feature)
        # print(feature)
    F = list(set(F))
    print("All possible features are :")
    print(F)
    print("Expanded opinion lexicon is :")
    print(O_Expanded)
            
if __name__ == '__main__':
    main()
