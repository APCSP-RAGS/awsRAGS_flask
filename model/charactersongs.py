import random

charactersongs_data = []
# Character-specific song list for Walter White from Breaking Bad
walter_white_songs = {
    "Early Days of Innocence (when he was a chemistry teacher)": [
        "The Police - Every Breath You Take",
        "David Bowie - Changes",
        "The Rolling Stones - Paint It Black",
    ],
    "Breaking Bad Transformation (when he enters the world of drug manufacturing)": [
        "Moby - Porcelain",
        "Tommy James and the Shondells - Crystal Blue Persuasion",
        "Lynyrd Skynyrd - Sweet Home Alabama",
    ],
    "Ruthless Heisenberg (as he becomes a drug lord)": [
        "AC/DC - Back in Black",
        "The Doors - Break on Through (To the Other Side)",
        "Johnny Cash - God's Gonna Cut You Down",
    ],
    "Dark Descent (as his character darkens)": [
        "Nine Inch Nails - Hurt",
        "Radiohead - Street Spirit (Fade Out)",
        "Pink Floyd - Comfortably Numb",
    ],
    "Redemption and Consequences (in the final episodes)": [
        "Badfinger - Baby Blue",
        "The Black Keys - Baby, I'm Howlin' for You",
        "Beck - Blue Moon",
    ],
}

# Initialize CharacterSongs
def initSongs():
    # setup CharacterSongs into a dictionary with id, CharacterSong, haha, boohoo
    global item_id
    item_id = 0
    for item in charactersong_list:
        charactersongs_data.append({"id": item_id, "CharacterSong": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomSong()['id']
        addSongHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomSong()['id']
        addSongBooHoo(id)
        
# Function to add CharacterSongs(for create method)
def createSong(CharacterSong):
    item_id = len(charactersongs_data)
    charactersongs_data.append({"id": item_id, "CharacterSong": CharacterSong, "haha": 0, "boohoo": 0})
    


# Return all CharacterSongs from charactersongs_data
def getSongs():
    return(charactersongs_data)

# CharacterSong getter
def getSong(id):
    return(charactersongs_data[id])

# Return random CharacterSong from charactersongs_data
def getRandomSong():
    return(random.choice(charactersongs_data))

# Liked CharacterSong
def favoriteSong():
    best = 0
    bestID = -1
    for CharacterSong in getCharacterSongs():
        if CharacterSong['haha'] > best:
            best = CharacterSong['haha']
            bestID = CharacterSong['id']
    return charactersongs_data[bestID]
    
# Jeered CharacterSong
def jeeredSong():
    worst = 0
    worstID = -1
    for CharacterSong in getSongs():
        if CharacterSong['boohoo'] > worst:
            worst = CharacterSong['boohoo']
            worstID = CharacterSong['id']
    return charactersongs_data[worstID]

# Add to haha for requested id
def addSongHaHa(id):
    charactersongs_data[id]['haha'] = charactersongs_data[id]['haha'] + 1
    return charactersongs_data[id]['haha']

# Add to boohoo for requested id
def addSongBooHoo(id):
    charactersongs_data[id]['boohoo'] = charactersongs_data[id]['boohoo'] + 1
    return charactersongs_data[id]['boohoo']

# Pretty Print CharacterSong
def printSong(CharacterSong):
    print(CharacterSong['id'], CharacterSong['CharacterSong'], "\n", "haha:", CharacterSong['haha'], "\n", "boohoo:", CharacterSong['boohoo'], "\n")

# Number of CharacterSongs
def countSongs():
    return len(charactersongs_data)

# Test CharacterSong Model
if __name__ == "__main__": 
    initSongs()  # initialize CharacterSongs
    
    # Most likes and most jeered
    best = favoriteSong()
    print("Most liked", best['haha'])
    printSong(best)
    worst = jeeredSong()
    print("Most jeered", worst['boohoo'])
    printSong(worst)
    
    # Random CharacterSong
    print("Random CharacterSong")
    printSong(getRandomSong())
    
    # Count of CharacterSongs
    print("CharacterSongs Count: " + str(countSongs()))