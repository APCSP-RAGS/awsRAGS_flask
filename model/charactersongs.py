import random

charactersongs_data = []
charactersong_list = [
    "If you give someone a program... you will frustrate them for a day; if you teach them how to program... you will "
    "frustrate them for a lifetime.",
    "Q: Why did I divide sin by tan? A: Just cos.",
    "UNIX is basically a simple operating system... but you have to be a genius to understand the simplicity.",
    "Enter any 11-digit prime number to continue.",
    "If at first you don't succeed; call it version 1.0.",
    "Java programmers are some of the most materialistic people I know, very object-oriented",
    "The oldest computer can be traced back to Adam and Eve. It was an apple but with extremely limited memory. Just "
    "1 byte. And then everything crashed.",
    "Q: Why did Wi-Fi and the computer get married? A: Because they had a connection",
    "Bill Gates teaches a kindergarten class to count to ten. 1, 2, 3, 3.1, 95, 98, ME, 2000, XP, Vista, 7, 8, 10.",
    "Q: What’s a aliens favorite computer key? A: the space bar!",
    "There are 10 types of people in the world: those who understand binary, and those who don’t.",
    "If it wasn't for C, we’d all be programming in BASI and OBOL.",
    "Computers make very fast, very accurate mistakes.",
    "Q: Why is it that programmers always confuse Halloween with Christmas? A: Because 31 OCT = 25 DEC.",
    "Q: How many programmers does it take to change a light bulb? A: None. It’s a hardware problem.",
    "The programmer got stuck in the shower because the instructions on the shampoo bottle said: Lather, Rinse, Repeat.",
    "Q: What is the biggest lie in the entire universe? A: I have read and agree to the Terms and Conditions.",
    'An SQL statement walks into a bar and sees two tables. It approaches, and asks may I join you?'
]

# Initialize CharacterSongs
def initCharacterSongs():
    # setup CharacterSongs into a dictionary with id, CharacterSong, haha, boohoo
    global item_id
    item_id = 0
    for item in charactersong_list:
        charactersongs_data.append({"id": item_id, "CharacterSong": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomCharacterSong()['id']
        addCharacterSongHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomCharacterSong()['id']
        addCharacterSongBooHoo(id)
        
# Function to add CharacterSongs(for create method)
def createCharacterSong(CharacterSong):
    item_id = len(charactersongs_data)
    charactersongs_data.append({"id": item_id, "CharacterSong": CharacterSong, "haha": 0, "boohoo": 0})
    


# Return all CharacterSongs from charactersongs_data
def getCharacterSongs():
    return(charactersongs_data)

# CharacterSong getter
def getCharacterSong(id):
    return(charactersongs_data[id])

# Return random CharacterSong from charactersongs_data
def getRandomCharacterSong():
    return(random.choice(charactersongs_data))

# Liked CharacterSong
def favoriteCharacterSong():
    best = 0
    bestID = -1
    for CharacterSong in getCharacterSongs():
        if CharacterSong['haha'] > best:
            best = CharacterSong['haha']
            bestID = CharacterSong['id']
    return charactersongs_data[bestID]
    
# Jeered CharacterSong
def jeeredCharacterSong():
    worst = 0
    worstID = -1
    for CharacterSong in getCharacterSongs():
        if CharacterSong['boohoo'] > worst:
            worst = CharacterSong['boohoo']
            worstID = CharacterSong['id']
    return charactersongs_data[worstID]

# Add to haha for requested id
def addCharacterSongHaHa(id):
    charactersongs_data[id]['haha'] = charactersongs_data[id]['haha'] + 1
    return charactersongs_data[id]['haha']

# Add to boohoo for requested id
def addCharacterSongBooHoo(id):
    charactersongs_data[id]['boohoo'] = charactersongs_data[id]['boohoo'] + 1
    return charactersongs_data[id]['boohoo']

# Pretty Print CharacterSong
def printCharacterSong(CharacterSong):
    print(CharacterSong['id'], CharacterSong['CharacterSong'], "\n", "haha:", CharacterSong['haha'], "\n", "boohoo:", CharacterSong['boohoo'], "\n")

# Number of CharacterSongs
def countCharacterSongs():
    return len(charactersongs_data)

# Test CharacterSong Model
if __name__ == "__main__": 
    initCharacterSongs()  # initialize CharacterSongs
    
    # Most likes and most jeered
    best = favoriteCharacterSong()
    print("Most liked", best['haha'])
    printCharacterSong(best)
    worst = jeeredCharacterSong()
    print("Most jeered", worst['boohoo'])
    printCharacterSong(worst)
    
    # Random CharacterSong
    print("Random CharacterSong")
    printCharacterSong(getRandomCharacterSong())
    
    # Count of CharacterSongs
    print("CharacterSongs Count: " + str(countCharacterSongs()))