# Natural Language Toolkit: Mimi
#
# 
# Authors: Sonali Sharma
#          Vanessa McAfee

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.

import string
import re
import random
import nltk
#import BeautifulSoup #this line doesn't work for Vanessa
from bs4 import BeautifulSoup
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
 "me"     : "you",
 "u"      : "me",
 "ur"     : "my",
 "urs"    : "mine"
}

hist_ques = []

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
    def respond(self, input, type):
         # check each pattern
        for (pattern, response) in self._pairs:
            #Adding type to the input
            if(type):
                newinput = type+":"+input
            else:
                newinput=input
            #print "New Input %s" %(newinput)
            match = pattern.match(newinput)
             # did the pattern match?
            if match:
                #print "Inside match"
                resp = random.choice(response)    # pick a random response
                #print response
                #print resp
                resp = self._wildcards(resp, match) # process wildcards

                 # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

     # Hold a conversation with a chatbot
    def converse(self, quit="quit"):
        filterlist = ["hi","how are","how're","hello","hey","hiya","you","me","I am","I","me","they","my","myself","u",
        "r","i","your","you're","i'm"]

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
                #Checking if the question was already asked

                if input in hist_ques:
                    print self.respond(input,"repeat")
                else:
                    hist_ques.append(input)

                
                #Passing input to see of there is an mathematical expression
                ques,answer = self.parse_mathexpression(input)
                ques_tokens = input.lower().split()

                c = filter(lambda (x): True if x.lower() in ques_tokens else False, filterlist)  

                if(answer):
                    try:
                        answer = eval(answer)
                        print self.respond(str(answer),"maths:answer")
                    except:
                        print self.respond(ques,"maths:error")
                elif(len(c)==0):
                #If no mathematical expression then pass question to wolfram alpha
                    answer =  self.get_fromwolfram(input)
                    #print len(answer)
                    if (len(answer)> 0 and len(answer)<80):
                        #print "Answer from wolfram %s" %(answer)
                        print self.respond(str(answer),"wolfram:answer")
                    else:
                        pass
                        #print "either no wolfram answer or its too long"
                       # Here start a generic conversation, ask new questions, change topic etc
                self.named_entity = self.get_namedentity(input)
                #self.named_entity[1] is to get Person named entity
                if(self.named_entity[1]):
                    print self.named_entity[1]
                    print self.respond(str("".join(self.named_entity[1])),"person")
                elif(self.named_entity[0]):
                    #print "found an organization"
                    #print "ques is: " + ques
                    print self.respond(str("".join(self.named_entity[0][0])),"organization")
                elif(self.named_entity[2]):
                    #print "found a location"
                    #print "ques is: " + ques
                    print self.named_entity[2][0]
                    print self.respond(str("".join(self.named_entity[2][0])),"location")
                elif(self.named_entity[3]):
                    #print "found a facility"
                    #print "ques is: " + ques
                    print self.respond(str("".join(self.named_entity[3][0])),"facility")
                else:
                    print self.respond(input,"")
                #else:
                    #print self.respond(input,"")

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
        #print "Inside wolfram"
        url  = 'http://api.wolframalpha.com/v2/query?appid=UAGAWR-3X6Y8W777Q&input='+input.replace(" ","%20")+'&format=plaintext'
        #print url
        data = urllib2.urlopen(url).read()  
        #soup = BeautifulSoup.BeautifulSoup(data)  ## changed to work for Vanessa's import statement
        soup = BeautifulSoup(data)
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
        self.facilitylist = []
        #print input
        text = nltk.pos_tag(input.split())
        #print text
        out = nltk.ne_chunk(text)
        #print out
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
                if chunk.node =='FACILITY':
                    facility = ' '.join([c[0] for c in chunk.leaves()])
                    self.facilitylist.append(facility)
        #print [self.orglist, self.personlist, self.gpelist,self.facilitylist]
        return [self.orglist, self.personlist, self.gpelist,self.facilitylist]
