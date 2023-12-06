import pandas

df = pandas.read_parquet("dataframe/0.parquet")
df2 = df.groupby(["recording_name", "artist_name", "user_id"]).size()


def compare_nb_ecoute(nb_ecoute1, nb_ecoute2):
    if (nb_ecoute1 == 0 and nb_ecoute2 != 0) or (nb_ecoute1 != 0 and nb_ecoute2 == 0):
        return 1
    else:
        return 0


def distance_songs(chanson1, chanson2):
    ecoutes_chanson1 = df2.loc[chanson1]
    ecoutes_chanson2 = df2.loc[chanson2]

    l1 = len(ecoutes_chanson1)
    l2 = len(ecoutes_chanson2)
    n = 0

    if l1 < l2:
        for user_id in ecoutes_chanson1.index:
            if user_id in ecoutes_chanson2.index:
                n += 2
    else:
        for user_id in ecoutes_chanson1.index:
            if user_id in ecoutes_chanson2.index:
                n += 2

    return l1 + l2 - n


def search_engine(song):
    my_song = song
    five_songs = []

    for other_song in df2.index:
        if my_song != other_song[0]:
            d = distance_songs(my_song, other_song[0])
            if (other_song[0], other_song[1], d) not in five_songs:
                if len(five_songs) < 5:
                    five_songs.append((other_song[0], other_song[1], d))
                    # Trier la liste par distance
                    five_songs.sort(key=lambda x: x[1])
                elif d < five_songs[-1][2]:
                    five_songs.pop(-1)
                    five_songs.append((other_song[0], other_song[1], d))
                    # Trier la liste par distance
                    five_songs.sort(key=lambda x: x[1])
    return five_songs
