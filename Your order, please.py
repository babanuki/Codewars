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


'''
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda words: sorted(words)))
    
    
    
sorted()와 sort()는 key function으로 정렬 기준을 정할 수 있음.
'''
