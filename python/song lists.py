top_5 = input("enter your top 5 songs: ").split()
songs = [top_5]
print(songs)
extra_song = input("would you like to add another song, type 'y' for yes and 'n' for no")
if extra_song.lower() == "y":
    new_song = input("what song would you like to add")
    songs.extend("new_song")
    print(songs)
elif extra_song.lower() == "n":
    print(songs)