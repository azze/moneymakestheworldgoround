import strategy
from os import listdir

class trade:
	def __init__(self):
		self.start=0
		self.orig=1
		self.end=0
		self.final=1
	def begin(stDate, stVal):
		self.start=stDate
		self.orig=stVal
	def finish(endDate, endVal):
		self.end=endDate
		self.final=endVal
	

if __name__ == "__main__":
	#todo grab all strats in folder /strategies add to list strats and create array with info on bank balance
	# also create other lists to save stuff like amount of trades, length of trades etc
	#open file containing data to be analysed
	#for each
	strats=[]
	strats.append(evolutionStrat())
	
	trades=[]
	for i in range(len(strats)):
		trst =[]
		trades.append(trst)
	
	files=os.listdir("GOOGL/")
	
	min=0
	for name in files:
		file=open("GOOGL/"+name)
		line=file.readline()
		while(!line==none):
			for j in range(len(strats)):
				inf =int(float(line))
				c=strats[i].tick(inf)
				if c is 1:
					tr=trade()
					tr.begin(min,inf)
					trades[i].append(tr)
				if c is -1:
					trades[i][-1].finish(min,inf)
			min=min+1
			line=file.readline()

	