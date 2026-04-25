# GBSC
# Gel Band Size Calculator

This tool estimates the size of a DNA band using DNA ladder band sizes and migration distances from gel electrophoresis.

## Why I built this
Gel electrophoresis results are often interpreted manually by comparing sample bands to a DNA ladder. This can be time-consuming and inconsistent. This tool helps users estimate DNA band size more systematically.

## How it works
The program uses ladder band sizes and ladder migration distances to build a standard curve based on the relationship between migration distance and log10 band size. It then estimates the size of an unknown sample band.

## How to run
1. Download the repository
2. Run:

```bash
python band_calculator.py
