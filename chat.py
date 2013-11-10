# Natural Language Toolkit: Chatbot Utilities
#
# Authors: Steven Bird <sb@csse.unimelb.edu.au>
# URL: <http://www.nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <jez@jezuk.co.uk>.

import string
import re
import random
import nltk
import BeautifulSoup
import urllib2
import nltk


reflections = {
 "am"     : "are",
 "was"    : "were",
 "i"      : "you",
 "i'd"    : "you would",
 "i've"   : "you have",
 "i'll"   : "you will",
 "my"     : "your",
 "are"    : "am",
 "you've" : "I have",
 "you'll" : "I will",
 "your"   : "my",
 "yours"  : "mine",
 "you"    : "me",
 "me"     : "you"
}

class Chat(object):
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and
        responses.  Each
                 pattern is a regular expression matching the user's statement
        or question,
                 e.g. r'I like (.*)'.  For each such pattern a list of
        possible responses
                 is given, e.g. ['Why do you like %1', 'Did you ever dislike
        %1'].  Material
                 which is matched by parenthesized sections of the patterns
        (e.g. .*) is mapped to
                 the numbered positions in the responses, e.g. %1.

                 @type pairs: C{list} of C{tuple}
                 @param pairs: The patterns and responses
                 @type reflections: C{dict}
                 @param reflections: A mapping between first and second person
        expressions
                 @rtype: C{None}
        """

        self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
        self._reflections = reflections

     # bug: only permits single word expressions to be mapped
    def _substitute(self, str):
         """
         Substitute words in the string, according to the specified reflections,
         e.g. "I'm" -> "you are"

         @type str: C{string}
         @param str: The string to be mapped
         @rtype: C{string}
         """

         words = ""
         for word in string.split(string.lower(str)):
             if self._reflections.has_key(word):
                 word = self._reflections[word]
             words += ' ' + word
         return words

    def _wildcards(self, response, match):
         pos = string.find(response,'%')
         while pos >= 0:
             num = string.atoi(response[pos+1:pos+2])
             response = response[:pos] + \
                 self._substitute(match.group(num)) + \
                 response[pos+2:]
             pos = string.find(response,'%')
         return response

    #Passing type here to give relevant reponses back
    def respond(self, input, answer, type):
        """


        """
         # check each pattern
        for (pattern, response) in self._pairs:
            newinput = type+":"+input
            print "New Input %s" %(newinput)
            match = pattern.match(newinput)

             # did the pattern match?
            if match:
                print "Inside match"
                resp = random.choice(response)    # pick a random response
                print response
                #print resp
                resp = self._wildcards(resp, match) # process wildcards

                 # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

     # Hold a conversation with a chatbot
    def converse(self, quit="quit"):
        input = ""
        while input != quit:
            input = quit
            try: 
                input = raw_input(">")
            except EOFError:
                print input             
            if input:
                while input[-1] in "!.?":
                    input = input[:-1]
                #Passing input to see of there is an mathematical expression
                ques,answer = self.parse_mathexpression(input)
                if(answer):
                    try:
                        answer = eval(answer)
                        print self.respond(ques+" "+str(answer), answer,"maths")
                    except:
                        print self.respond(ques+" "+str(answer), answer,"maths:error")
                else:
                    #If no mathematical expression then pass question to wolfram alpha
                    answer =  self.get_fromwolfram(input)
                    if (answer):
                        print "Answer from wolfram %s" %(answer)
                        #Now check the named entity in the question
                        self.named_entity = self.get_namedentity(input)
                    else:
                        print "wolfram else"
                        # Here start a generic conversation, ask new questions, change topic etc


    def parse_mathexpression(self,input):
        pattern = re.compile('([^\d+/*-/%]*)([\d+/*-/%]+)')
        match =  pattern.match(input)
        if match:
            m =  match.group(2)
            output = m.translate(string.maketrans("",""), '!"#$&\'(),:;<=>?@[\\]_`|~')
            return (match.group(1),output)
        else:
            return "",""

    def get_fromwolfram(self, input):
        print "Inside wolfram"
        url  = 'http://api.wolframalpha.com/v2/query?appid=UAGAWR-3X6Y8W777Q&input='+input.replace(" ","%20")+'&format=plaintext'
        print url
        data = urllib2.urlopen(url).read()  
        soup = BeautifulSoup.BeautifulSoup(data)
        keys = soup.findAll('plaintext')
        if (keys):
            #Printing the first returned rresult of the query. The first result is the heading, second
            #result is the actual value hence printing [1:2]
            for k in keys[1:2]:
                output = k.text
        else:
            output = ""
        return output
        
    def get_namedentity(self,input):
        self.orglist = []
        self.personlist = []
        self.gpelist = []
        print input
        text = nltk.pos_tag(input.split())
        print text
        out = nltk.ne_chunk(text)
        print out
        for chunk in out:
            if hasattr(chunk,'node'):
                if chunk.node =='ORGANIZATION':
                    organization = ' '.join([c[0] for c in chunk.leaves()])
                    self.orglist.append(organization)
                if chunk.node =='PERSON':
                    person = ' '.join([c[0] for c in chunk.leaves()])
                    self.personlist.append(person)
                if chunk.node =='GSP' or chunk.node =='GPE' :
                    gpe = ' '.join([c[0] for c in chunk.leaves()])
                    self.gpelist.append(gpe)

        return [self.orglist, self.personlist, self.gpelist]


    def parse_entity(self,input):
        sent = "vanessa is at UC Berkeley"
        text = nltk.pos_tag(sent.split())
        nltk.ne_chunk(text)
