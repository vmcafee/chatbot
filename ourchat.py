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

     (r'(hi|hello|hey)(.*)',
     ( "hi!!! how r u!!",)),
     (r"repeat:(.*)",
     ( "You already asked me that!!",
       "Give me a new question, I already told you that")
     ),
    (r"maths:answer:(.*)",
     ( "Maths!! That's an easy one, the answer is %1",
       "Hmm.. mathematics, well the answer is %1",
       "Looks like you like math too, the answer is %1")
     ),
     (r"maths:error:(.*)",
     ( "Looks like a mathematics question but you haven't framed it correctly",
       "Hmm.. mathematics, but check you expression again")
     ),
     (r"wolfram:answer:what is(.*)",
     ( "That's an easy one, answer is %1",
       "I got an answer for you!  %1")),
    (r"wolfram:answer: who is(.*)",
     ( "Why do you ask? I will still tell you %1")
     ),
    (r"wolfram:answer:(.*)",
     ( "%1",
      "I found it for you, %1")
     ),
    (r"organization:(.*)",
     ( "Do you know anyone who works at %1?",
       "What type of organization is %1?")
     ),
    (r"person:(.*)",
     ( "How do you know this person, did you say %1?",
       "%1 is a person, what else do you know about this person?")
     ),
    (r"location:(.*)",
     ( "Have you been to this place??",
       "Have you been to places near by %1?"
       "This would be a good place to visit if you haven't already been here")
     ),
    (r"facility:(.*)",
     ( "Have you been to this facility??",
       "%1 is a fmous facility?"
       "This would be a good place to visit if you haven't already been here")
     ),
    (r'I\'m (.*)',
    ( "ur%1?? that's so cool! kekekekeke ^_^ tell me more!",
      "ur%1? neat!! kekeke >_<")),
    (r'(.*) don\'t you (.*)',
    ( "u think I can%2??! really?? kekeke \<_\<",
      "what do u mean%2??!",
      "i could if i wanted, don't you think!! kekeke")),
    (r'ye[as] [iI] (.*)',
    ( "u%1? cool!! how?",
      "how come u%1??",
      "u%1? so do i!!")),
    (r'do (you|u) (.*)\??',
    ( "do i%2? only on tuesdays! kekeke *_*",
      "i dunno! do u%2??")),
    (r'(cos|because) (.*)',
    ( "hee! i don't believe u! >_<",
      "nuh-uh! >_<",
      "ooooh i agree!")),
    (r'why can\'t [iI] (.*)',
    ( "i dunno! y u askin me for!",
      "try harder, silly! hee! ^_^",
      "i dunno! but when i can't%1 i jump up and down!")),
    (r'I can\'t (.*)',
    ( "u can't what??! >_<",
      "that's ok! i can't%1 either! kekekekeke ^_^",
      "try harder, silly! hee! ^&^")),

    (r'(.*) (like|love|watch) anime',
    ( "omg i love anime!! do u like sailor moon??! ^&^",
      "anime yay! anime rocks sooooo much!",
      "oooh anime! i love anime more than anything!",
      "anime is the bestest evar! evangelion is the best!",
      "hee anime is the best! do you have ur fav??")),

    (r'I (like|love|watch|play) (.*)',
    ( "yay! %2 rocks!",
      "yay! %2 is neat!",
      "cool! do u like other stuff?? ^_^")),

    (r'anime sucks|(.*) (hate|detest) anime',
    ( "ur a liar! i'm not gonna talk to u nemore if u h8 anime *;*",
      "no way! anime is the best ever!",
      "nuh-uh, anime is the best!")),

    (r'(are|r) (you|u) (.*)',
    ( "am i%1??! how come u ask that!",
      "maybe!  y shud i tell u?? kekeke >_>")),

    (r'who (are|r) (you|u)(.*)',
    ( "I am Mimi, I'm here to answer your questions!!",
      "y shud i tell u?? kekeke >_>")),
    (r'(.*)name(.*)',
    ( "I am Mimi, I'm here to answer your questions!!",
      "y shud i tell u?? kekeke >_>")),
    (r'(.*)(no|yes)(.*)',
    ( "ok, got it! what's your next question",
      "cool, what else do you want to ask me?")),

    (r'quit',
    ( "mom says i have to go eat dinner now :,( bye!!",
      "awww u have to go?? see u next time!!",
      "how to see u again soon! ^_^")),
    (r'(what|why|how)(.*)',
    (
     "I have no clue, try looking it up on wikipedia!",
     "Did you say what is %1",
     "well I don't know yet but I will find out for you! Next question please",
     "hee u think im gonna tell u? .v.",
     "booooooooring! ask me somethin else!")),
    (r'(.*)',
    ( "man u talk a lot!!!",
      "I don't feel like talking anymore",
      "boooooring!! ur not very fun")),
    )
  
chatbot = c.Chat(pairs, nltk.chat.eliza.reflections)

def dog_chat():
    print "Hi there! I'm Mimi and I like answering questions. Ask me something."
    chatbot.converse()

def demo():
    dog_chat()

if __name__ == "__main__":
    demo()
