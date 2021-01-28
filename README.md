# Li-ion-SoC-Estimation

This repository outlines a project undertaken at Newcastle University to estimate the SoC of a Li-ion battery whilst under heavy use using various machine-learning techniques.

It utilises a dataset based of a Panasonic 18650PF Li-ion battery found here: https://data.mendeley.com/datasets/wykht8y7tg/1

## Files contained


The '*Graphs and Visualised Data*' folder contains all graphs that were produced as a part of this project, including all iterations of the Neural Network using various combinations of hidden layers and epochs.

The '*Models and Code*' folder contains the '*csv-data*', where the CSV data-files used in this project are stored. It also contains the '*Battery_Analysis.ipynb*' Jupyter Notebook which contains the code and models built for this project. The '*data-read.py*' file was created to convert the data-set from a .Mat format to CSV format. The '*requirements.txt*' file contains the library requirements needed to run the Jupyter Notebook.

The '*Woodhall_Poster.pptx*' contains the poster that was produced to present the results of the project, giving a brief overview of the entire project.

The '*Woodhall_Report.pdf*' file contains the report that was produced to accompany this project, including Literature Review, Methodology, Results & Discussion. It contains further information and details on the issues inherent with Li-ion SoC estimation and proposes a Battery Monitoring System that could be used to produce a custom data-set.

## Installation

Make sure you are running Python 3.7 or above.

Use the package manager *pip* to install the necessary libraries. It is recommended that all packages are using their laters versions.

To install Jupyter Lab, run this command in the Command Prompt:

```cmd
pip install jupyterlab
```
In the Command Prompt, navigate to the '*Li-ion-SoC-Estimation/Models and Code*' directory and enter this command to install the necessary libraries:

```cmd
pip install --user --upgrade -r requirements.txt
```

### Usage
---
To run the Jupyter Notebook file, run this command in the Command Prompt:

```cmd
jupyter lab
```

If this command does not work, try the following:

```cmd
jupyter-lab
```

```cmd
jupyter notebook
```

Once Jupyter Lab has opened, open the '*Battery_Analysis.ipynb*' file from within the '*Li-ion-SoC-Estimation/Models and Code*' directory.
