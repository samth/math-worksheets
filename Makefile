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

mult100: mult100.tex
	pdflatex mult100.tex

.PHONY: mult100

clean:
	rm -f times*.pdf times*.aux times*.log add*.pdf add*.aux add*.log multgrid.pdf multgrid.aux multgrid.log grids.tex mult100.pdf mult100.aux mult100.log

.PHONY: clean
