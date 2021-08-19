.PHONY: build
build:	## package project for PyPi
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine check dist/*

.PHONY: pypitest
pypitest:	 build  ## upload project to pypi test server
	twine upload --repository testpypi dist/* --skip-existing

.PHONY: upload
upload:	build ## upload new version to PyPi
	twine upload dist/* --skip-existing
