# WorkFuncScript
These are some script files that handle the VASP's output files to get the Work Function.

## Introduction
This project contains several python and fortran scripts for processing and analyzing LOCPOT file, as well as obtaining Fermi energy levels and ultimately Distance-Potential plots and work functions.

## Procedures

### 1. Processing of LOCPOT file
We obtained the LOCPOT by performing DFT calculations with the VASP program, and subsequently will have to process the LOCPOT with the vtotav.py file.
First, make sure your Python version is 3.x and that you have the required dependencies installed.

```bash
pip install matplotlib ase numpy
```

Next, use the following command to process the LOCPOT file and generate LOCPOT_Z:

```bash
python vtotav.py LOCPOT z
```
This generates a LOCPOT_Z file in the current directory, where LOCPOT is the name of the input file and z is the direction parameter.


### 2. Calculating vacuum energy level and plotting graph
You can use the CalculationWF.py script to calculate vacuum energy levels and plot Distance-Potential curves. Make sure you have installed the required Python dependencies.

Run the following commands to perform the calculation and plot:

```bash
python CalculationWF.py
```

One can then obtain the vacuum energy level.
