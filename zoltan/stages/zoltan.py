from zoltan.assets.random_phrases import cooler_response, misunderstand_response
from zoltan.assets.random_phrases import leaving_response, returning_player_welcome
import state
import random
from state import init_state
from assets.functions import paused_send, short_paused_send, long_paused_send, half_sec_pause, set_current_user
from zoltan.assets.readings import return_random_future
from assets.functions import one_sec_pause
from zoltan.assets.readings import get_lucky_numbers
from zoltan.assets.databaseCalls import save_future_to_database, check_for_returning_player


async def send(s):
    await state.message.channel.send(s)


async def zoltan_welcome():
    set_current_user()
    check_for_returning_player()
    await long_paused_send(["Who dares summon the almighty Zoltan?!"])
    if not state.returning_player:
        await long_paused_send(
            [
                "Wait, don't tell me, don't tell me. . .",
                "it's. . .",
                state.current_user + "",
                "!",
                "Huzzah!",
            ])
        half_sec_pause()
        await short_paused_send([state.current_user + ", tell me,"])
        await long_paused_send(
            [
                "Would you like to know your standard future, for 10 sp?",
                "Or your much",
                "cooler"
            ])
        await paused_send(
            [
                "future, for 5 gp?",
                "(Type \"standard\" or \"cooler\")"
            ])
    else:
        welcome = returning_player_welcome()
        await long_paused_send(welcome)
        half_sec_pause()
        await send("(Type \"standard\" or \"cooler\")")
    state.zoltan_stage = 1


async def zoltan_goodbye():
    responses = [
        [
            "Your loss, " + state.current_user + "!",
            "The Mighty Zoltan will be here,",
            "with nothing to pass the time except the excruciating burden of knowing absolutely every possible future all the time.",
            "The Zoltan will be fine."
        ],
        [
            "Well",
            "Well, smell you later, I guess, " + state.current_user + ".",
            "Zoltan will be fine.",
            "The Mighty Zoltan can't exactly leave. This is Zoltan's fortune-telling office.",
            "Zoltan will be fine."
        ],
        [
            "My disappointment is palpable, " + state.current_user + "!",
            "Palpable!",
            "Wait"
            "Pulpable.",
            "I mean pulpable.",
            "I had an orange earlier."
        ],
        [
            "You want to leave?",
            "YOU WANT TO LEAVE?!",
            "That's fine.",
            "You take care now, " + state.current_user + ". Happy trails."
        ]
    ]
    random_response = responses[random.randint(0, len(responses) - 1)]
    await long_paused_send(random_response)
    init_state()


async def zoltan_misunderstand():
    misunderstanding_statements = [
        "Hmm. . . The Mighty Zoltan struggles to understand your meaning. Can you repeat that?",
        "The Zoltan understands not what you say, " + state.current_user +
        ". Can you speak in a manner which is clear more?",
        "Sorry. . . what? Can you repeat that?",
        "The Zoltan understands not! Repeat!"
    ]
    await send(misunderstanding_statements[random.randint(0, len(misunderstanding_statements) - 1)])


async def zoltan_start():
    message_lower = state.message.content.lower()

    if state.zoltan_stage == 1:
        async def read_crystal_ball(standard=True):
            await short_paused_send(["In your future. . .\n", ".\n", ".\n", ".\n"])
            await paused_send(["I see. . . you. . ."])
            await short_paused_send([".\n", ".\n", ".\n"])
            one_sec_pause()
            random_future = return_random_future(standard)
            state.zoltan_result = random_future
            one_sec_pause()
            await long_paused_send([random_future[0], random_future[1]])
            half_sec_pause()

        if message_lower.startswith('sta'):
            await paused_send(["One standard future, coming up."])
            await read_crystal_ball()
            state.zoltan_stage = 2

        elif message_lower.startswith('coo'):
            await long_paused_send(cooler_response())
            await read_crystal_ball(False)
            state.zoltan_stage = 2

        else:
            phrase = misunderstand_response()
            await long_paused_send([phrase])

    if state.zoltan_stage == 2:
        await paused_send(["**You gained one Official Zoltan Brand Collectable Ticket!**",
                          "*It has your fortune written on it, and below your lucky numbers:*",
                          "*" + get_lucky_numbers() + "*",
                          "*On the bottom, there is a large, empty space. . .*"])
        await short_paused_send([".\n", ".\n", ".\n"])
        save_future_to_database()
        one_sec_pause()
        await paused_send([
            "The Zoltan thanks you for your patronage,",
            "and hopes that you will come again."
        ])
        phrase = leaving_response()
        await long_paused_send(phrase)
        init_state()
