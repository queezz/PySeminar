# Introduction to Jupyter notebook

[toc]

## Repository files

| name                                                       | info                                                  |
| ---------------------------------------------------------- | ----------------------------------------------------- |
| [Introduction_to_jupyter](./Introduction_to_jupyter.ipynb) | Load data, plot data, data structure and `%run` magic |
| [test.py](./test.py)                                       | Test file for explaining how to use `%run`.           |

# 1. Python

## 1.1. Install python (Python 3.xx)

### 1.1.1 Python environment manager:

Full Anaconda:

https://www.anaconda.com/

Or just miniconda:

https://docs.conda.io/en/latest/miniconda.html

### 1.1.2 Pure Python

Download the latest release from https://www.python.org/

If you don't need to work with different python environments, this might be your choice. But they say conda is easier on the new users. Generally it is good to know to use conda.

### 1.2 Python packages with pip

In Python, we use packages. In pure python you usually use `pip` package manager to install packages

For example, we can install `matplotlib` - a popular package for plotting, as follows:

```
pip install matplotlib
```

There could be several versions of python installed on your system. In that case it is better to specify which `pip` to use:

```bash
python3 -m pip install matplotlib
```

Or for upgrading a package with `pip`:

``` bash
python3 -m pip install --upgrade matplotlib
```

Here `python3` is used. If you have both `python 2` and `python 3` on your system, this maybe the way to specify which `python` to use. If you only have `python3`, it should be simply accessable with `python`. On Windows, a shorthand call is availiable: `py -2` or `py -3`.



Sometimes pip can tell that the user has no permissions to access data. In that case adding `--user` flag to the pip command can solve the problem:

```shell
python3 -m pip install matplotlib --user
```



## 1.3 Essential packages:

[numpy](https://numpy.org/) - work with matrices

[scipy](https://www.scipy.org/) - scientific calculations

[pandas](https://pandas.pydata.org/) - better work with 2D data

[xarray](https://xarray.pydata.org/en/stable/) -  Fujii sensei likes it, it is for Multiple Dimension arrays.

[lmfit](https://lmfit.github.io/lmfit-py/) - for fitting data with functions

## 1.4 Editor

Sometimes having a good editor is quite helpful. There are so many choices, and all depends on your preferences. There is `vim` - a command line, very poverful and adjustible editor. But it is somewhat hard to start using. There was an `atom` editor, but it is not well supported now. So the new lightweigt and modern easy to use one is from Microsoft, the Visual Studio Code: https://code.visualstudio.com/ . If you don't have anyt preferences now, you might as well try this one.

## 1.5 Jupyter

https://jupyterlab.readthedocs.io/en/stable/

Install `jupyter` and `jupyter lab`:

```bash
python3 -m pip install jupyter
python3 -m pip install jupyter lab
```

To start a jupyter notebook:

- jupyter notebook

To start a jupyter lab:

```bash
jupyter lab
```



# 2. Git: short summary

Git is a version control system. It is easy to use it in [VS Code](https://code.visualstudio.com/).

## 2.0 Install git.

It is easy to install git on any system. Go to it's page and see detailed example:

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git



For Windows, just download an installer. 

After git is installed, you can start using it.

## 2.1 Git initial commit

There are two components to this. One - web based repository, and another - local files. To get first, create a project in your favorite git service, such as github.com. For second - initiate git in your working directory.



```bash
# Do this in terminal [powershell] or directly in file browser
mkdir my_project
cd my_project
# You can copy existing .gitignor for your language.
touch .gitignore # creates empty file with name .gitignore
git init # initializes repository
git add . # add all files to repository
git commit -m "Initial commit" 
# this line didn't work for me
git remote add origin youruser@yourserver.com:/path/to/my_project.git
# Or which works for me and my git:
git remote add origin https://github.com/queezz/projectname.git
# get link in your github repository
git push origin master
```

## 2.2 Git clone and checkout

```bash
# copy a project from online repository into a local dir
git clone https://github.com/path/to/project.git
# update your local repository
git checkout origin master
```

## 2.3 Use .gitignore

There is no sense to upload all your data to git. And sometimes you want to have some test files, but you don't want to share them. Additionally, there are some technical files which are not needed in the repository, such as precompiled python code. 



To skip them all, create a file with name ".gitignore" and put all file names you want to skip there. Example:



```.gitignore
test.py
text.pdf

data/

*.pyc
```



# 3. Markdown

Here is some page with markdown syntax: ["Markdown Guide"][1]. And another one: ["Markdown記"][2].

The best for GitHub is probably this [Markdown Cheatsheet][3].



A good application for editing rendered markdown is [typora][4], which is avaliable for Windows, OS X, and Linux. 



[1]: https://www.markdownguide.org/basic-syntax/	"Markdown Guide"
[2]: https://www.markdown.jp/syntax/#markdown	"Markdown記"
[3]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet	"Markdown Cheatsheet"

[4]: https://typora.io/	"Typora"

# 4. Project folder structure

Organize!
- make separate folder for figures
- If you want to make some data output, put it in separate folder.
- One notebook for one topic 

```
project
│   README.md
│   .gitignore (if using git)
│   coronal_model.ipynb
│   fulcher-spectra-browser.ipynb
│   useful_programs.py
│   mypath.txt (list of data directories, for instance. put this file in .gitignore)
│
└───figures
│   │   20200101_experiment1-molecular-spectra.png
│   │   emission-diagram.png
│   │   ...
│   │
│   └───calibrations
│       │   calibration1.png
│       │   calibration2.png
│       │   ...
│   
└───out
│   │   experimnt1_analyzed_data1.txt
│   │   experimnt1_analyzed_data2.txt
│
│
└───CoronaModel
│    │   program1.py
│    │   program2.py
│
└───Diffusion
│    │   diffusion1.py
│    │   rawdatacalibration.py
```
