directions = [North, East, South, West]
globals = {}

def run():
	init_globals(globals)
	prioritize("cactus")
	#init_sunflowers()
	while True:
		# basic_strategy()
		harvest_pumpkins()
		#harvest_sunflower()
		#harvest_cactuses()
		# update strategy if necessary
		
run()