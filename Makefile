# Definición de variables
SRC_DIR = notebooks
DEST_DIR = /

# Objetivo por defecto
.PHONY: copy_notebooks

ejercicios_dia1:
	#cp $(SRC_DIR)/*.ipynb $(DEST_DIR)
	#cd notebooks\
	copy notebooks\*.ipynb ..\..\