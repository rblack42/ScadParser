.PHONY:	docs
docs:	changes	## run Sphinx to build html pages
	cd rst && \
	sphinx-build -b html -d _build/doctrees . ../docs

.PHONY: testdocs
testdocs:	## run tests on ci
	cd rst && \
		sphinx-build -nW -b html -d _build/doctrees . ../docs
	cd rst && \
		sphinx-build -b linkcheck -d _build/doctrees . ../docs
	cd rst && \
		sphinx-build -b spelling -d _build/doctrees . ../docs

.PHONY:	docs-clean
docs-clean:	## clean docs for complete rebuild
		rm -rf rst/_build/doctrees

.PHONY: pdf
pdf:	## build PDF docs
	pip install . && \
	cd rst && \
	sphinx-build -b latex -d _build/doctrees . _build/latex && \
	cd _build/latex && \
	pdflatex pylit.tex && \
	cp pylit.pdf ../../../docs

