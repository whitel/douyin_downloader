.PHONY=all clean download

all: download

download:
	@python download.py

test:
	@python test.py

clean:
	rm htmls/* result/*
