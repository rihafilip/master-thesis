all: compile transform

.PHONY: all compile transform clean

compile:
	latexmk --shell-escape -pdflua example.tex
	latexmk -C
	latexmk --shell-escape -pdflua example.tex

transform:
	magick -density 900 example.pdf -quality 100 example.png

clean:
	latexmk -C
	rm -rf _minted/
