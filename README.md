# Drecker & Dee

Drecker & Dee is a Discord bot that runs several games. Currently, it can run an auction game (D&D Bay), as well as a Zoltan game. 

The bot was made for Pathfinder 2e, but compatible with similar TTRPGs (table-top role playing games).
The bot takes information about a user's item for sale and "auctions" it to a fictional character from the game world.


## Table of Contents

-   [D&D Bay](#dd-bay-overview)

-   [Zoltan](#zoltan-Overview)

-   [Contributors](#contributors)
-   [Technologies](#technologies)
-   [Usage](#usage)

---
# D&D-Bay

## D&D-Bay-Overview

Auction off your item with Drecker & Dee!

Can’t find a buyer? Can’t talk fast enough to hold your own auction? Want to turn your bounty into gold? Put your item up for bid, and be guaranteed to receive at least over your asking price, or your item back! We’ll only auction your item if it has at least one bidder, and we’ll do it all for the low-low cost of 5% of the value of the item!

### Get started:

The PC starts with an optional hype check, to determine how hyped they can make characters in the town about the auction. Roll performance, diplomacy, or applicable skill to determine how hyped you can get the town about your item for sale.

    - Fail 5: -1 bidder
    - DC 5: 0 bidders
    - DC 15: +1 bidder
    - DC 20: 1d4 + 1 bidders
    - DC 25: 1d4 + 2 bidders
    - DC 35 (crit): 1d6 + 3 bidders

The PC inputs three options:

-   Item and its value (not selling price, but full value). The highest item value considered is 1000 sp.
-   Bidding start percent: 10%, 25%, 50%
-   Hype modifier (based on roll above)

Bidding starting percentages determine how many bidders the item will attract. The lower the asking price, the higher chance of attracting bidders.

    -   10%: safe. Attracts 1d6 + 1 bidders (auction is guaranteed to run).
    -   25%: difficult. Attracts 1d4 bidders.
    -   50%: very difficult. Attracts 1d4 - 1 bidders.

The number of bidders, then, is determined by the bidders attracted from the _starting bid_ and by the _hype modifier_.

If zero or one bidder is attracted, the auction will not commence, and the PC gets the item back from D&D Bay. D&D Bay is no longer interested in that item at all, as it has proven itself unsellable.

If there are bidders, bidding rounds commence!

### Bidding rounds

The first bidder will start with a _bid roll_. The bid roll determines if they choose to bid, and, if successful, by how much.

#### Bid roll:

    -   DC 20: increases bid by high bid -- 9% of the item's value
    -   DC 14: increases bid by mid bid -- 6.15% of the item's value
    -   DC 9 (or DC 10 for rare): increases bid by low bid -- 3.15% of the item's value
    -   <9 (or <10 for rare): No bid.

If the bidder makes a bid, that bid is added on top of the current _going bid_.
For instance, if the bidding started at 10 sp, and the successful bidder made a 9% bid, the _going bid_ is 10.90 sp.

If the bidder fails on the bid roll, they roll a _stop bidding check_ to determine if they will continue bidding or drop out.

Stop bidding checks are based on the rarity of the item at auction. The rarer the item, the higher the chance that the bidder will want to stay in the bid.

### Stop bidding checks:

#### Common item

    -   Rounds 1 - 4: DC 16 to continue bidding
    -   Rounds 5 - 7: DC 18 to continue bidding
    -   Rounds 8 +: DC 19 to continue bidding

#### Uncommon item

    -   Rounds 1 - 4: DC 12 to continue bidding
    -   Rounds 5 - 7: DC 16 to continue bidding
    -   Rounds 8 +: DC 18 to continue bidding

#### Rare item

    -   Rounds 1 - 4: DC 8 to continue bidding
    -   Rounds 5 - 7: DC 13 to continue bidding
    -   Rounds 8 +: DC 13 + 1d6 to continue bidding

If the bidder rolls unsuccessfully, they drop out of the auction, and the next player makes a _bid check_.

The auction stops when all bidders have dropped out, or if the item has reached its _terminus price_. The item is then sold as the current highest bid!

### Terminus price for item

    -   Common: 75% of actual value
    -   Uncommon: 110% of actual value
    -   Rare: 100 + 1d3 x 100% of actual value (200 - 400%)

While playing the game, PCs are able to see the auction in progress. They will see, through the Discord bot:

-   the bids as they appear
-   the dropouts as they occur
-   the selling price of the item
-   the name of the successful bidder

---
# Zoltan

## Zoltan-Overview

Zoltan is a game mimicking the fortune-telling arcade machines of a similar name (Zoltan, Zoltan). He is a machanical man in a box looking over a crystal ball; when money is inserted into the machine, the character speaks, and a paper fortune is printed out of the machine.

For this Pathfinder/D&D context, Zoltan returns a future with a perk that a player can use in their next game. "Standard" futures are less expensive, but only offer a 1 or 2-max bonus to various rolls. "Cooler" futures are much more expensive, but offer a 3 or 4-max bonus to other rolls. Both flavour texts and rolls are separate in "standard" and "cooler" futures.

## Zoltan-Get-Started

To play, a player must simply enter "$zoltan" when the bot is running and in a Discord channel. They will then be prompted to select "standard" or "cooler", and can select "$help" or "$info" for assistance, or "exit" to end the program. After selecting a future, they will be provided with flavour text and a perk that they will be able to use in their next game.

All futures are meant to be small perks that may add a bonus to gameplay, and encouragement to play creatively, with the perk in mind. Most of them are one-time-use bonuses to rolls.

---
## Contributors

-   [Joel MacKenzie](https://github.com/joelmackenz)

## Technologies

-   Python
-   Discord.py

## Usage

    1. Add a .env file with your Discord.py access token as TOKEN = [token]
    2. Add your bot to your Discord channel
    3. Run main.py in the terminal to start the bot
    4. Type "$auction" as a message in the Discord channel containing the bot, and away we go!
