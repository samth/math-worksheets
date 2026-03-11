N ?= 2

times: timesN.tex
	MULTIPLIER=$(N) pdflatex -shell-escape -jobname=times$(N) timesN.tex

.PHONY: times

add: addN.tex
	ADDEND=$(N) pdflatex -shell-escape -jobname=add$(N) addN.tex

.PHONY: add

clean:
	rm -f times*.pdf times*.aux times*.log add*.pdf add*.aux add*.log

.PHONY: clean
