# Natural Language Toolkit: Mimi
#
# 
# Authors: Sonali Sharma
#          Vanessa McAfee

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.

import nltk
import chat as c


pairs = (

     (r'(hi|hello|hey|howdy|hiya|what\'s up)(.*)',
     ( "Hi! How are you?",
      "Hello! How have you been?",
      "Hi, want to ask me something?")),
     (r"repeat:(.*)",
     ( "You already said that!",
       "Say something new, we've already talked about that!",
       "Let's talk about something new!")
     ),
    (r"maths:answer:(.*)",
     ( "I <3 math! That's an easy one, the answer is %1",
       "Hmm.. mathematics, well the answer is %1",
       "Looks like you like math too, the answer is %1")
     ),
     (r"maths:error:(.*)",
     ( "Looks like a mathematics question but you haven't framed it correctly",
       "Hmm.. mathematics, but check you expression again")
     ),
     (r"wolfram:answer:what is(.*)",
     ( "Let's see... the answer is %1",
       "I've got an answer for you!  %1")),
    (r"wolfram:answer: who is(.*)",
     ( "Why do you ask? I will still tell you %1")
     ),
    (r"wolfram:answer:(.*)",
     ( "Good question!! the answer is, %1",
      "I found it for you, %1")
     ),
    (r"organization:(.*)",
     ( "Do you know anyone who works at %1?",
       "What type of organization is %1?",
       "%1? I've heard of that organization.")
     ),
    (r"person:(.*)",
     ( "How do you know this person, did you say %1?",
       "%1 is a person, what else do you know about this person?")
     ),
    (r"location:(.*)",
     ( "I love %1! Have you been there?",
       "Have you been to any cool places in %1?",
       "I hear that's a cool place to visit if you haven't already been there.")
     ),
    (r"facility:(.*)",
     ( "Have you been to this artifact?",
       "%1 is a famous artifact?"
       "That would be a good place to visit if you haven't already been here.")
     ),
    (r"oldtopic:(.*)",
     ( "Let's talk more about %1",
       "I remember you mentioning %1 before, tell me more.")
     ),
    (r'I\'m (.*)',
    ( "ur%1? that's great! tell me more!",
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
    ( "I'm Mimi, I'm here to answer your questions!!",
      "The question is, who are you?")),
    (r'(.*)name(.*)',
    ( "I am Mimi, I'm here to answer your questions!!",
      "Why should I tell u?? kekeke >_>")),
    (r'(.*)(no|yes)(.*)',
    ( "ok, got it! what's your next question",
      "cool, what else do you want to ask me?")),
    (r'(good|fine|okay|ok)(.*)',
    ( "OK!",
      "All right!",
      "Great!")),
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
    ( "Man u talk a lot!!!",
      "Is that a question?",
      "Haha you're fun!")),
    )
  
chatbot = c.Chat(pairs, nltk.chat.eliza.reflections)

def mimi_chat():
    print "Hi there! I'm Mimi and I like answering questions. I can solve math problems and like chatting about people and places."
    chatbot.converse()

def demo():
    mimi_chat()

if __name__ == "__main__":
    demo()
