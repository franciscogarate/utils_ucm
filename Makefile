# Definición de variables
SRC_DIR = notebooks
DEST_DIR = /

# Objetivo por defecto
.PHONY: dia1

ejercicios_dia1:
	#cp $(SRC_DIR)/*.ipynb $(DEST_DIR)
	cd ./notebooks/*.ipynb ../
dia1:
	cd ./notebooks && cp *.ipynb ../../
