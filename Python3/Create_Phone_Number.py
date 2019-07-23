def create_phone_number(n):
    n=[str(i) for i in n]
    return str("("+str(''.join(n[:3]))+") "+str(''.join(n[3:6]))+"-"+str(''.join(n[6:])))



'''
def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
'''
