class Search_capital:
	def __init__(self,search):
        	self.searchIn=search
	def search(self):	
		a=self.searchIn
		file=open('base_date_city.txt','r',encoding='UTF-8')
		for line in file:
			if a in line:
			    capital=line[0:line.index(':')]
			    return(capital)
