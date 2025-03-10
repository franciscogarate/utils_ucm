# Definición de variables
REPO_URL = https://github.com/franciscogarate/utils_ucm.git
REPO_DIR = utils_ucm
SRC_DIR = notebooks
DEST_DIR = /

# Objetivo por defecto
.PHONY: update dia1 ejercicio%

libs:
	pip install -r requirements.txt

libs_env:
	pip install uv
	uv pip install -r requirements.txt

update:
	@if [ -d "$(REPO_DIR)/.git" ]; then \
		cd $(REPO_DIR) && git pull; \
	else \
		git clone $(REPO_URL); \
	fi

dia1:
	cd ./notebooks && cp *.ipynb ../../

copia_siniestros:
	cd ./data && cp Siniestros.csv ../../

ejercicio%:
	#cd utils && cp file$*.xlsx ..
	cd ./notebooks && cp Ejercicio_$*_*.ipynb ../../
