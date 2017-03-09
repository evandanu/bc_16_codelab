def find_max_min(alist):#first define function
	if max(alist)==min(alist):
		blist=[len(alist)]
		return blist
	else:
		newarray=[min(alist),max(alist)]
		return newarray


	