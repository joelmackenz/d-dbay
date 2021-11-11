import random
import state


def set_result(x):
    result = x
    if result == state.last_result:
        return_random_future()
    else:
        return result


def return_random_future(standard=True):
    randNum = coin_toss()
    if standard:
        result = set_result(
            standard_futures[random.randint(1, len(standard_futures))])
    else:
        randNum += 2
        result = set_result(
            cooler_futures[random.randint(1, len(cooler_futures))]
        )
    state.last_result = result
    if "+" in result[1]:
        i = result[1].index('+') + 1
        return [
            result[0],
            "\nOn your next game, " +
            result[1][:i] + str(randNum) + result[1][i:]
        ]
    else:
        return [
            result[0],
            "\nOn your next game, " + result[1]
        ]


def coin_toss():
    return random.randint(1, 2)


def get_lucky_numbers():
    lucky_numbers = ""
    for i in range(0, 4):
        lucky_numbers += " " + str(random.randint(1, 99))
    return lucky_numbers.strip()


standard_futures = {
    1: [
        "having the gift of foresight",
        "re-roll any one roll."
    ],
    2: [
        "becoming a hero",
        "start with one additional hero point."
    ],
    3: [
        "wary",
        "re-roll any one roll, but your first result must be used for your next roll."
    ],
    4: [
        "being a protective mama bear",
        "add an additional + to any one damage roll on an enemy who attacked or attempted to attack an ally."
    ],
    5: [
        "having a silver tongue",
        "add + to any one persuasion roll of your choice."
    ],
    6: [
        "learning a fun factoid",
        "add + to any one lore skill check of your choice."
    ],
    7: [
        "getting a good rest",
        "add + to any one initiative roll of your choice."
    ],
    8: [
        "having the gift of hindsight",
        "ret-con the last sentence you said, only once."
    ],
    9: [
        "thinking fast",
        "you can use one additional reaction on any one attack."
    ],
    10: [
        "looking trustworthy",
        "add + to any one deception check."
    ],
    11: [
        "feeling huge -- ain't nothing but a peanut",
        "add + strength to any one roll."
    ],
    12: [
        "feeling sharp, looking sharp, being sharp",
        "add + dexterity to any one roll."
    ],
    13: [
        "looking like you're finally getting over this cold",
        "add an extra + to the next healing potion you drink."
    ],
    14: [
        "looking mean",
        "add an extra + to any one intimidation roll."
    ],
    15: [
        "thirsting for blood",
        "add an extra + to any one damage roll."
    ],
    16:  ["looking especially pitiful",
          "for any one saving roll, choose a teammate to roll for you, adding their modifier like a standard roll."
          ],
    # the following must be saved in database so it doesn't happen too often
    # "becoming invested",
    # "you will get a new lead from a GM @JoelYes#9757 @liam#4021 elizabot#4690"
}

cooler_futures = {
    1: [
        "being a gambler",
        "on any one attack, let the Dandy Phantom sword attack for you with an additional 10 AC, or perform the attack yourself and deal double damage. The deal can only be made once."
    ],
    2: [
        "eating some good spicy food",
        "you may release Deadly Neurotoxins at any time, once; all nearby humans get the flee trait."
    ],
    3: [
        "being a master hide-and-go-seeker",
        "once, if you take cover, you will be completely forgotten by nearby enemies."
    ],
    4: [
        "swimming with the fishes",
        "once, for ten consecutive minutes, you can breathe under water."
    ],
    5: [
        "feeling paranoid",
        "on the first battle, start with a surprise attack round with only you. If the team is already taking a surprise attack round, start your own surprise attack round before taking your second surprise attack with the team."
    ],
    6: [
        "feeling confident and sexy",
        "to any one roll involving NPC interaction, roll twice and take the higher result."
    ],
    7: [
        "feeling thick-skinned",
        "add + AC when being dealt any slashing attack."
    ],
    8: [
        "feeling gassy",
        "because of your recent meal which included frankly too much garlic, you can take one free action to release Noxious Garlic Burp, dealing 2 HP damage to anyone within 5 ft of you."
    ],
    9: [
        "feeling exhausted. Your back aches, your heart aches. . . but your feet. . . your feet are resilient!",
        "gain + to your speed for the entire game."
    ],
    10: [
        "warmed up, limber; immune to pulling your hammies",
        "add + to any one acrobatics check."
    ],
    11: [
        "hearing the blues a'callin'",
        "your previous day's meal of tossed salad and scambled eggs adds an additional 5 HP on top of your standard HP."
    ],
    12: [
        "being a fearless leader",
        "at any time, once, chant \"imhotep\" to your allies and give them + on their next roll."
    ],
    13: [
        "shooting first",
        "if someone attacks with a ranged weapon and yours is ready, take your attack before they do theirs."
    ],
    14: [
        "bringing a ranged weapon to a melee fight",
        "if someone attacks you or an ally with a melee weapon and your ranged weapon is ready, fire your melee weapon as a reaction before they attack."
    ],
    15: [
        "channelling a diva",
        "you can sing notes that are literally impossible -- add + to any one performance roll."
    ],
    16: [
        "your spirit being willing but your flesh spongey and bruised",
        "the first time your health goes below 10 HP, add one additional action to your next turn."
    ],
    17: [
        "having an unforgetable luncheon",
        "add + to any one deception roll; add +6 to any one deception roll about any consumable item (eg. food, potions, etc.)"
    ],
    18: [
        "borrowing a feeling",
        "the first time someone rolls a natural 20, add + to your next roll. "
    ]
}
