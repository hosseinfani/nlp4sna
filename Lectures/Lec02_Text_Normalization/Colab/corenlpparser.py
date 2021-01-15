import os
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('universal_tagset')
#nltk.help.upenn_tagset()

text = "I made her duck."
text_tokens = word_tokenize(text)
text_pos = nltk.pos_tag(text_tokens, tagset='universal')

from nltk.parse.corenlp import CoreNLPServer
# The server needs to know the location of the following files:
#   - stanford-corenlp-X.X.X.jar
#   - stanford-corenlp-X.X.X-models.jar
STANFORD = os.path.join("./stanford-corenlp-4.2.0")

# Create the server
server = CoreNLPServer(
   os.path.join(STANFORD, "stanford-corenlp-4.2.0.jar"),
   os.path.join(STANFORD, "stanford-corenlp-4.2.0-models.jar"),
)
print(STANFORD)
print(os.path.join(STANFORD, "stanford-corenlp-4.2.0.jar"))
# Start the server in the background
server.start()

from  nltk.parse.corenlp  import CoreNLPParser
# parser = CoreNLPParser(url='http://nlp.stanford.edu:8080/')
parser = CoreNLPParser()
parse = next(parser.raw_parse("I put the book in the box on the table."))
print(parse)