import state
# Latest message
message = {}

# Current game being played
game = ""
game_running = False
returning_player = False

# User and item states
current_user = str()
item = str()
item_value = int()
hype = str()
modifier = int()
item_percent = int()
rarity = str()

# Auction Setup states
auction_stage = int()
potential_state = None
return_to_step = int()

# Auction states
going_bid = float()
starting_round = int()
auctionRound = int()
current_bidders = int()
total_bidders = int()
terminus_price = int()
winning_bid = float()
finalPrizeMoney = float()

# zoltan states
zoltan_stage = int()
last_result = []
last_response = {}
zoltan_result = ""

def init_state():
    state.message = {}
    state.game = ""
    state.game_running = False
    state.returning_player = False
    state.current_user = str()
    state.item = str()
    state.item_value = int()
    state.hype = str()
    state.modifier = int()
    state.item_percent = int()
    state.rarity = str()

    # state.auction = False

    state.auction_stage = int()
    state.potential_state = []
    state.return_to_step = int()

    state.going_bid = float()
    state.starting_round = int()
    state.current_bidders = int()
    state.total_bidders = int()
    state.terminus_price = int()
    state.winning_bid = float()
    state.zoltan_stage = int()
    state.last_result = []
    state.last_response = {}
    state.zoltan_result = "Test test test"