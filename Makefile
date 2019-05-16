install:
	pip install -r requirements.txt

deploy:
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*