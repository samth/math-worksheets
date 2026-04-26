N ?= 2

times: timesN.tex
	MULTIPLIER=$(N) pdflatex -shell-escape -jobname=times$(N) timesN.tex

.PHONY: times

add: addN.tex
	ADDEND=$(N) pdflatex -shell-escape -jobname=add$(N) addN.tex

.PHONY: add

multgrid: multgrid.tex gen-grids.py
	python3 gen-grids.py
	pdflatex multgrid.tex

.PHONY: multgrid

TIMES_MAX ?= 12
ADD_MAX ?= 20

times100: times100.tex
	MAX=$(TIMES_MAX) pdflatex -shell-escape -jobname=times100_max$(TIMES_MAX) times100.tex

.PHONY: times100

add100: add100.tex
	MAX=$(ADD_MAX) pdflatex -shell-escape -jobname=add100_max$(ADD_MAX) add100.tex

.PHONY: add100

clean:
	rm -f times*.pdf times*.aux times*.log add*.pdf add*.aux add*.log multgrid.pdf multgrid.aux multgrid.log grids.tex

.PHONY: clean
