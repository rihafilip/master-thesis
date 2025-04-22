all: compile transform

.PHONY: all compile transform

compile:
	latexmk --shell-escape -dvilua example.tex

transform:
	dvisvgm example.dvi
