import copy
from music import PLAYLIST
from music import SONGS

def if_find(song: list, old_word: str):
    '''

    It's used for checking if the word is inside the song.

    '''
    import re

    # this intializes a  lise within range of song
    b = ['' for i in range(len(song))]
    word_list = []

    # go through each sentence of a song
    for i in range(len(song)):

        # strip out the punctuations and put all words into word_list
        b[i] = list(filter(None, re.split('[ .,:;!?]', song[i])))
        for j in range(len(b[i])):
            word_list.append(b[i][j])

    # true when the word is found
    if old_word in word_list:
        return True

def substitute(song: list, old_word: str, new_word: str ) -> bool:
    # same thing as if_find
    import re
    b = ['' for i in range(len(song))]
    word_list = []
    for i in range(len(song)):
        b[i] = list(filter(None, re.split('[ .,:;!?]', song[i])))
        for j in range(len(b[i])):
            word_list.append(b[i][j])
    if old_word in word_list:
        result = True
        # if the word is found, we replace the old one with new one
        for i in range(len(b)):
            for j in range(len(b[i])):
                if b[i][j] == old_word:
                    b[i][j] = new_word
            # converse the list back to string
            b[i] = " ".join(b[i])
            song[i] = b[i]
    else:
        result = False

    return result


def reverse_it(song: list) -> list:
    # same thing as if_find
    import re
    b = ['' for i in range(len(song))]
    word_list = []
    for i in range(len(song)):
        b[i] = list(filter(None, re.split('[ .,:;!?]', song[i])))
        for j in range(len(b[i])):
            word_list.append(b[i][j])
    # reverse words within a sentence
    for i in range(len(b)):
        b[i] = b[i][::-1]
        b[i] = " ".join(b[i])
        song[i] = b[i]
    return song

def load_song(selection: int) -> list:
    # guarantee that selection in within the range
    if 1 <= selection <= len(PLAYLIST):
        returned_list = []
        returned_list.append(SONGS[selection - 1])
        returned_list.append(PLAYLIST[selection - 1])
        result = returned_list
    # if it is not within the range return empty list
    else:
        result = []
    return result


def song_title(specific_song, songs, playlist):
    '''

    this is just a helper function and help me to
    transfer among index, title and lyrics easily
    '''
    index = songs.index(specific_song)
    title = playlist[index]
    return title


def new_playlist(playlist):
    '''
    this is a helper function which helps me
    to build the "load-another-song" function in start,
    because the songs would change so the playlist
    should be updated as well.
    '''
    new_list = []
    for i in range(len(playlist)):
        a = str(i + 1) + ": " + playlist[i]
        new_list.append(f"{a}")
    return new_list

prompt_words = ('\nLet\'s mix songs!\n'
                'L = Load a different song\n'
                'T = Title of song\n'
                'S = Substitute a word\n'
                'P = Playback\n'
                'R = Reverse it!\n'
                'X = Reset to a original song\n'
                'Q = Quit?')

def start():
    '''

    I use deepcopy because I do not want to
    change the original songs when substitutions
    and reversion happen. So "X" calls out the original song.
    '''
    song = SONGS
    playlist = PLAYLIST
    songs_copy = copy.deepcopy(song)
    playlist_copy = copy.deepcopy(playlist)

    # at the default status, now_song is set as old macdonald.
    now_song = songs_copy[0]

    # if-elif statements to execute each of user's choice
    while True:
        print(prompt_words)
        choice = input("Your choice: ").upper()
        # print out the title of current song
        if choice == "T":
            print(f"you are mixing the song "
                  f"{song_title(now_song,songs_copy,playlist_copy)}")
        # substitute the words with new ones
        elif choice == "S":
            old_word = input("What word do you want to "
                             "replace in the existing song? ")
            new_word = input("What new word do you want to "
                             "use for the new song? ")
            if if_find(now_song, old_word):
                index_2 = songs_copy.index(now_song)
                substitute(now_song, old_word, new_word)
                songs_copy[index_2] = now_song
            else:
                print(f"Sorry, I can't find {old_word} in the existing song.")
        # play the song
        elif choice == "P":
            print(now_song)
        # reverse the song word by word
        elif choice == "R":
            index_3 = songs_copy.index(now_song)
            reverse_it(now_song)
            songs_copy[index_3] = now_song
        # load another song
        elif choice == "L":
            print(f"{new_playlist(playlist)}")
            num = input("Your choice: ")
            b = [i + 1 for i in range(len(playlist))]
            for i in range(len(b)):
                b[i] = str(b[i])
            if num not in b:
                print("The song is not valid. Mixed song is unchanged")
            else:
                new_song = load_song(int(num))[0]
                now_song = new_song
        # play the original version of current song
        elif choice == "X":
            index_1 = songs_copy.index(now_song)
            now_song = song[index_1]
            songs_copy[index_1] = now_song
        # quit the game
        elif choice == "Q":
            break

def main():
    start()

if __name__ == "__main__":
    main()