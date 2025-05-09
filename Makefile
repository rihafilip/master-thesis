all: compile

.PHONY: all compile minted force cleanmk clean

compile:
	latexmk --shell-escape -file-line-error -pdflua ctufit-thesis.tex

minted:
	echo '{"custom_lexers": {' > .latexminted_config
	sha256sum minted/PIRLexer.py | awk '{print "\"PIRLexer.py\": \"" $$1  "\","}' >> .latexminted_config
	sha256sum minted/RIRLexer.py | awk '{print "\"RIRLexer.py\": \"" $$1  "\""}' >> .latexminted_config
	echo "}}" >> .latexminted_config

force: cleanmk minted compile

cleanmk:
	latexmk -C
	rm -rf _minted/

clean: cleanmk
	rm -rf _minted/ svg-inkscape/ diagrams/*.svg
	rm -f text/*.aux ctufit-thesis.bbl* ctufit-thesis.lol ctufit-thesis.xmpdata pdfa.xmpi
