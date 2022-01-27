install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
format:
	black *.py

lint:
	pylint --disable=R,C utils.py
	
test:
	python -m pytest -vv --cov=utils test_utils.py
	