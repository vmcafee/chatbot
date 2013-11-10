# Natural Language Toolkit: Eliza
#
# Copyright (C) 2001-2013 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
#          Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.

# a translation table used to convert things you say into things the
# computer says back, e.g. "I am" --> "you are"

import nltk
import chat as c


pairs = (
    # suggestions
    (

    r"I'm hungry",
        ( "I'm hungry too!",
          "Let's get dinner!",
          "Let's go to the Doggy Diner!")),
    (r"maths:what is(.*)",
     ( "That's an easy one, answer is %1",
       "Hmm.. mathematics, well the answer is %1")),
    (r"maths:tell me what is(.*)",
     ( "Looks like you like maths, the answer is %1",
       "And the answer is %1")
     ),
    (r"maths:what is(.*)",
     ( "Looks like you like maths, the answer is %1",
       "And the answer is %1")
     ),
    (r"maths:evaluate(.*)",
     ( "Ok I evaluated the question and I found that the answer is %1")
     ),
    (r"maths:(.*)",
     ( "You're lazy, you just typed the expression or you didn't type the text correctly, answer is %1 ",
       "you got it! the answer is %1")
     ),
    (r"maths: error",
     ( "Looks like you didn't type the question correctly, try again may be!!",
       "Dumb ass I won't tell you the answer! Ask me something else")
     ),
    # anything else
    (r'(.*)',
     (
         "(Looking soulfully) treat please...",
         "Did you say 'Let's go for a walk?'",
         "Yes! Yes! Nap time!",
     )
    )
)

chatbot = c.Chat(pairs, nltk.chat.eliza.reflections)

def dog_chat():
    print "Emoting cutely ..."
    chatbot.converse()

def demo():
    dog_chat()

if __name__ == "__main__":
    demo()
