f = open("example_data.txt", "r")
data = f.read().split("\n")

cards = [
    "A", 
    "K", 
    "Q", 
    "J", 
    "T", 
    "9", 
    "8", 
    "7", 
    "6", 
    "5", 
    "4", 
    "3",
    "2"
]

strength = list(range(len(cards)))

card_strength = {k:v for k,v in zip(cards, strength[::-1])}

hands = []
bids = []
for x in data:
    hand, bid = x.split(" ")[0], x.split(" ")[1]
    hands.append(hand)
    bids.append(bid)

example_hand = hands[0]

def classify_hand(h):
    c_freq_dict = {card: h.count(card) for card in h}
    return(c_freq_dict)
    