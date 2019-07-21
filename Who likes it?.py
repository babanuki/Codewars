def likes(names):
    sz=len(names)
    if sz==0:
        return "no one likes this"
    elif sz==1:
        return names[0]+" likes this"
    elif sz==2:
        return " and ".join(names)+" like this"
    else:
        tmp=names[0]+", "+names[1]+" and "
        if sz==3:
            tmp+=names[2]+" like this"
            return tmp
        else:
            tmp+=str(sz-2)+" others like this"
            return tmp
