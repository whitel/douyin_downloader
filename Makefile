.PHONY=all clean download

all: download

download:
	@python download.py

clean:
	rm htmls/* result/*
