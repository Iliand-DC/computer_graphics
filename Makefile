SRC = src
MAIN = $(SRC)/main.py
VENV = .venv
ACTIVATE_VENV = . .venv/bin/activate

all: create_venv
	 $(ACTIVATE_VENV); python $(MAIN)

create_venv:
	if [ ! -d $(VENV) ]; then python -m venv $(VENV); fi
	$(ACTIVATE_VENV); pip install pysdl2 pysdl2-dll
