def validBraces(string):
  l=[]
  for i in string:
      if i in ('(', '[', '{'):
          l.append(i)
          continue
      if len(l)==0:
          return False
      tmpW=l.pop()
      if (tmpW, i)!=('(', ')') and (tmpW, i)!=('[', ']') and (tmpW, i)!=('{', '}'):
          return False
  return len(l)==0




'''
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''
'''
