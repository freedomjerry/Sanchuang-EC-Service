all: bin/ects

bin/ects: bin ects.cpp util.cpp
	g++ -std=c++11 -O3 -g ects.cpp util.cpp -o bin/ects

bin:
	mkdir -p bin

.PHONY: test

test: bin/ects
	@for v in loose; do for ms in  0.0 0.01 0.3 1.0; do \
		bin/ects -v $${v}  -m $${ms}  -d ../../test/data/Coffee_TRAIN.tsv ../../test/data/Coffee_TEST.tsv || exit; \
	done; done; done