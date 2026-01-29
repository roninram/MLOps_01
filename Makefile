install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black -v *.py

lint:
	pylint --disable=R,C car.py
	pylint --disable=R,C hello.py

all:	install lint test format
