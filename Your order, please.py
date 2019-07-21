import string

def order(sentence):
    tmpl=[]
    ansl=[]
    l=sentence.split(" ")
    for i in l:
        for j in i:
            if j in string.printable[0:10]:
                tmpl.append(j+i)
    tmpl.sort()
    for i in tmpl:
        j=list(i)
        del j[0]
        ansl.append("".join(j))
    return " ".join(ansl)
