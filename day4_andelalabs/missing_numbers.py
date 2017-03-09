def find_missing(list1,list2):
  list_with_items=[]
  list_with_more_items=[]
  
  if len(list_with_more_items)>len(list_with_items):
    list_with_more_items = list1
    list_with_items = list2
  else:
    list_with_more_items = list2
    list_with_items = list1
    
    for a in list_with_more_items:
      if a in list_with_more_items and a not in list_with_items:
        return a
      
  if list1 == list2:
    return 0
  