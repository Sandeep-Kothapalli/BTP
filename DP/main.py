import nltk
# all codes are run in anaconda with python 3.8.1
# install nltk using pip
# uncomment the two lines below for the first time you run the code
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# from cgi import escape
from pprint import pprint
from nltk.treeprettyprinter import TreePrettyPrinter
from nltk.parse import CoreNLPParser
from nltk.parse.corenlp import CoreNLPDependencyParser
coreNLPurl = 'http://corenlp.run/'
localServer = 'http://localhost:9000'
# use local server with desired port number in case you cant use corenlp.run
dependencyParser = CoreNLPDependencyParser(url=coreNLPurl)
Parser = CoreNLPParser(url=coreNLPurl)
def tagging(sentences):
    # couldnt get raw_parse_sents to work
    # res = dependencyParser.raw_parse_sents(sentences)
    # # list(res)
    # # print(list(res))
    # for parsedSentence in res:
    #     print(item.treepositions() for item in parsedSentence)
    dependencyRelations = []
    for sentence in sentences:
        print(sentence)
        print()
        res, = dependencyParser.raw_parse(sentence)
        next(Parser.raw_parse(sentence)).pretty_print()
        # print(next(Parser.raw_parse(sentence)).height())
        dependencyRelations.append(res)
        for governor, dep, dependant in res.triples():
            print(governor,dep,dependant)
        print()

def main():
    reviewFile = "review-data.txt"
    reviewData = open(reviewFile)
    text = reviewData.readline();
    sentences = nltk.sent_tokenize(text);
    tagging(sentences)

if __name__ == "__main__":
    main()
