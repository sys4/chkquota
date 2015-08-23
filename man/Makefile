# Makefile to create documentation
# Patrick Ben Koetter, p@sys4.de

SHELL = /bin/sh
SOURCES = chkquota.1.txt

# Substitutions
HTMLS= $(patsubst %.txt,%.html,$(SOURCES))
MANS= $(patsubst %.txt,%.man,$(SOURCES))
PDFS= $(patsubst %.txt,%.pdf,$(SOURCES))

# Build Targets
all:	html man pdf
html:	$(HTMLS)
man:	$(MANS)
pdf:	$(PDFS)

# Build commands
%.html: %.txt
	a2x -f xhtml $<

%.man: %.txt
	a2x --doctype manpage --format manpage $<

%.pdf: %.txt
	a2x $<

# Defaults
.PHONY:	clean

clean:	
	rm -f *.html *.pdf *.1 *.5 *.8

