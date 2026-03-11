# Math Worksheets

Generates timed drill worksheets (multiplication and addition) as PDFs. Each build produces 5 pages of 20 randomly-generated problems.

## Requirements

- LaTeX with `pdflatex` (TeX Live or similar)
- `extarticle`, `pgfmath`, and `catchfile` packages (included in TeX Live)

## Usage

```bash
make times N=2    # generates times2.pdf (2 times tables)
make times N=7    # generates times7.pdf (7 times tables)
make times        # defaults to N=2

make add N=5      # generates add5.pdf (addition: +5)
make add N=9      # generates add9.pdf (addition: +9)
make add          # defaults to N=2
```

Each run produces fresh random problems. Rebuild to get a new set.

## Cleaning up

```bash
make clean        # removes all generated PDFs and auxiliary files
```
