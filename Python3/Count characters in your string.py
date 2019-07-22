def count(string):
    dict={letter:string.count(letter) for letter in set(string)}
    return dict
