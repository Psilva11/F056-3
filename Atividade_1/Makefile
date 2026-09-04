DOC = relatorio

all:
	pdflatex $(DOC).tex
	bibtex $(DOC)
	pdflatex $(DOC).tex
	pdflatex $(DOC).tex

AUX_FILES = $(wildcard *.aux *.log *.bbl *.blg *.out)
clean:
	rm -f $(AUX_FILES)
