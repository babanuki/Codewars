def song_decoder(song):
    return ' '.join([i for i in song.split("WUB") if i is not ''])





'''
def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()

'''
