N ?= 2

times: timesN.tex
	MULTIPLIER=$(N) pdflatex -shell-escape -jobname=times$(N) timesN.tex

.PHONY: times

clean:
	rm -f times*.pdf times*.aux times*.log

.PHONY: clean
