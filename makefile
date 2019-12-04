all: sigma.png solar.png

sigma.png : metropolis.py 
	python metropolis.py 
	
solar.png : manchas.py
	python manchas.py

	