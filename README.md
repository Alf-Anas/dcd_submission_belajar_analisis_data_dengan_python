### Local Setup

- Download and Install Anaconda from `https://www.anaconda.com/download`
- Before create new project make sure to create new python environment to make sure the depedencies not conflict with root or other project
- Create new env by using code `conda create --name dicoding-project-env python=3.9` or using Anaconda Navigator UI by clicking `environments` tab  in left side
- Acivate the environment using code `conda activate dicoding-project-env` or clicking the `green start` button in Anaconda Navigator UI
- Install the necessary python package using `pip install numpy pandas scipy matplotlib seaborn jupyter` or in Anaconda Navigator click Install in Notebook


### Change Directory

- To change work directory in different drive, in terminal use `D:` to change to Drive D
- To move to the directory use `cd D:/full-path`
- To create new directory use `mkdir proyek_analisis_data` and then `cd proyek_analisis_data`
- Open the jupyter notebook using `jupyter notebook .` or `jupyter lab .`


### List All active Jupyter Notebook or Lab

- To list use `jupyter notebook list`
- To close or shut down the session, open the url individually, click `file > shutdown`


### Install the package requirements

- Install package by using `pip install -r requirements.txt`


### How to run notebook

- Open the `notebook.ipynb` or double click the file, Click `restart the kernel and run all the cell` to restart the notebook file and recalculate all data.


### How to run dashboard

- Dashboard was made using streamlit
- To open the deployed one, open the url.txt file, copy the url and paste it in browser
- To start dashboard locally, change direcory to dashboard dir using `cd dashboard`
- Run dashboard using `streamlit run dashboard.py`
- A new tab will open to show  dashoard

  