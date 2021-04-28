# Gene Set Variation Analysis

This tutorial covers basic steps to perform Gene Set Variation Analysis from Somascan Dataset.

Gene Set Variation Analysis tool is available at [GSVA](https://github.com/rcastelo/GSVA).

## Dataset Description

The tutorial uses an in-silico dataset with two groups: cancer (treatment) and healthy donor (placebo). 
In the cancer group, proteins associated to Pancreatic Cancer were overexpression of 10-folds.

A simulated, in-silico molecular signature was created by subsampling some of the proteins associated to Pancreatic Cancer.

Therefore, both molecular signature as well as the Somascan dataset are simulated data.

## Tutorial Usage

```bash
git clone https://github.com/andreagrioni/Tutorials.git
```

then:

1. Open the `GSVA.Rmd` file located at `Tutorials/R/GSVA/` with RStudio. 
2. Set the subfolder `Tutorials/R/GSVA` as working directory. 
3. Run the Rmarkdown vignette.

### Settings

The Rmarkdown tutorial runs `renv` to restore the environment with packages necessary for the analysis.
More information on `renv` [here](https://rstudio.github.io/renv/articles/renv.html)

Restoring the environment may take a while; if your want to avoid to use your private server, RStudio Cloud is a great – and free – alternative.

You can reach it [here](https://rstudio.cloud/)

### GSVA Citation

Hänzelmann S, Castelo R, Guinney J (2013).  
“GSVA: gene set variation analysis for microarray and RNA-Seq data.”  
BMC Bioinformatics, 14, 7.  
doi: 10.1186/1471-2105-14-7, http://www.biomedcentral.com/1471-2105/14/7.
