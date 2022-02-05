import state
import random


def returning_player_welcome():
    welcomes = [
        [
            "...oh, I see it's you again, " + state.current_user + ".",
            "What are we feeling today,",
            "your standard future for 10 sp,",
            "or the  \~ *m* *u* *c* *h*  *c* *o* *o* *l* *e* *r* \~  one for 5 gp?",
        ],
        ["Oh, " + state.current_user + ", it's you! Welcome back!",
         "that future come true yet?",
         "just kidding Zoltan knows it did.",
         "What'll it be this time?"],
        ["Well, well, well, if it isn't " + state.current_user + ".",
         "Welcome! Last time was fun, eh?",
         "Shall we look again into the future? Perhaps the cooler one?"],
        ["It's you! " + state.current_user + "!",
         "You came back!",
         "Oh, you. . .",
         "You're not here to chat, you just want another future.",
         "No that's fine that's fine.",
         "What'll it be?"],
        ["Hey, I know you!",
         state.current_user + ", right?",
         "What'll it be?"]
    ]
    welcome = welcomes[random.randint(0, len(welcomes) - 1)]
    if "welcome" in state.last_response and state.last_response["welcome"] == welcome:
        welcome = returning_player_welcome()
    else:
        state.last_response["welcome"] = welcome
    return welcome


def leaving_response():
    responses = ["Stay cool.",
                 "Look to the skies.",
                 "Run along now, you cheeky lad.",
                 "Off you go, the lot of you.",
                 "Toodle-oo!",
                 "So long, partner.",
                 ["Bye, I love you.",
                  "Wait, oh, wait, I didn't mean to say that.",
                  "Oh man."]
                 ]
    response = responses[random.randint(0, len(responses) - 1)]
    if "leaving_response" in state.last_response and state.last_response["leaving_response"] == response:
        response = leaving_response()
    else:
        state.last_response["leaving_response"] = response
    if type(response) is list:
        return response
    else:
        return [response]


def misunderstand_response():
    misunderstanding_statements = [
        "Hmm. . . The Mighty Zoltan struggles to understand your meaning. Can you repeat that?",
        "The Zoltan understands not what you say, " + state.current_user +
        ". Can you speak in a manner which is clear more?",
        "Sorry. . . what? Can you repeat that?",
        "The Zoltan understands not! Repeat!"
    ]
    response = misunderstanding_statements[random.randint(
        0, len(misunderstanding_statements) - 1)]
    if "misunderstandingResponse" in state.last_response and state.last_response["misunderstandingResponse"] == response:
        response = misunderstand_response()
    else:
        state.last_response["misunderstandingResponse"] = response
    return response


def cooler_response():
    cooler_responses = [
        ["Whoa, you really want the cooler one?",
         "I mean,",
         "Great, yes, let's do it!"],
        ["YES!",
         "Great, yes, great.",
         "Let's do it, let's get cool."],
        ["Very cool of you."]
    ]
    response = cooler_responses[random.randint(0, len(cooler_responses) - 1)]
    if "cooler_responses" in state.last_response and state.last_response["cooler_response"] == response:
        response = cooler_response()
    else:
        state.last_response["cooler_response"] = response
    return response
