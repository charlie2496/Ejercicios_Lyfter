def read_songs(filename):
    with open(filename, "r", encoding="utf-8") as file:
        songs = file.readlines()

    clean_songs = []

    for song in songs:
        song = song.strip()

        if song:
            clean_songs.append(song)

    return clean_songs


def organize_songs(songs):
    songs.sort()
    return songs


def write_songs(filename, songs):
    with open(filename, "w", encoding="utf-8") as file:
        for song in songs:
            file.write(song + "\n")
print(read_songs("songs.txt"))
print("Songs organized:")
print(organize_songs(read_songs("songs.txt")))