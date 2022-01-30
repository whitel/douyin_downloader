.PHONY = all clean download
PYCACHE := $(shell find . -type d -name "__pycache__")
HTMLS := htmls
RESULT := result

all: download

download:
	@python download.py

test:
	@python test.py

clean:
	rm $(HTMLS)/* $(RESULT)/* -f
	rm $(PYCACHE) -rf
