def data_type(n):#creating the function 
#initializing some values
  a='no value'
  b='more than 100'
  c='less than 100'
  d='equal to 100'
  if type(n)==str:#checking for string length
    return len(n)
    
  elif type(n)==type (None):#checking for None
    return a
  elif type(n)==type (True):#checking for boolean
    return (n)
  elif type(n)==type (7):#checking for integers
    if n>100:
      return b
    elif n<100:
      return c
    else:
      return d
  
  elif type (n)==type([]):#checking for lists
    if len(n)==3:
      return n[2]
    else:
      return None