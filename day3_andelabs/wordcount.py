def words(this_is_a_string):

	mydict={}
	mysplit=this_is_a_string.split()

	if len(mysplit)==1:
		mydict[mysplit[0]]=1
		return mydict

	for item in mysplit:
		if item.isdigit():
			item=int(item)
			mydict[item]=mysplit.count(str(item))
	return mydict



