Instructions to execute and prerequisites.

Prerequisites;
  1. Python version 3.7 is required.(might work in lower versions but the core was run and tested in Python 3.7)
  2. Install NLTK using pip3 (pip if default python version is python 3.7)
  3. You can host a local corenlp server in your machine and execute the algorithm. For simplicity sake, the algorithm sends        CoreNLPDependencyParser API requests directly to corenlp.run hosted globally by Stanford. You can modify the code to send
     API requests to relevant server. Details are mentioned in the code.
  4. You need to have a file named review-data.txt in the working directory. For BTP purpose, initial opinion dictionary has        been hard-coded. If you want to test on a larger dataset, please modify the code.
  5. python(3) main.py should output the extracted features and expanded opinion word lexicon.
  
  Sample input (in review-data.txt):
  
   Canon G3 takes great pictures. The picture is amazing. You may have to get more storage to store high quality pictures and     recorded movies. The software is amazing. 
   
   O = ['great']
   
   Sample Output:
   
   =========================================================================
    Initial Opinion Lexicon 
    ['great']
    =========================================================================
    All possible features are :
    ['G3', 'picture', 'storage', 'movies', 'software', 'pictures']
    Expanded opinion lexicon is :
    ['amazing', 'great']
    
    Note:
    Picture and pictures being identified as two features is a bug that needs to be fixed.

