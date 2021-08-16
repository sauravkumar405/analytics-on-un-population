# Analytics on UN Population

## Brief Description

In this poject we are provided with a raw data that consists of Population statistics of diffrent countries and region around the world. This data is provided to the United Nations Organization and can be downloaded via this link: <https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv> Our aim in this project will be to convert raw open data which consists of  country and year wise population estimates  into bar charts that tell some kind of story.

## Installation

These are some basic steps to follow for installation of the project

### 1) Create Virtual Environment

* Create a folder in your local machine and open a teminal inside the folder.

* Next you have to create a virtual enivironment and install all the packages, to do so run the following command

```bash
virtualenv new_env
```

A new folder named 'new_env' will be created in your current path.

* Next to activate this virtual environment run the following command

```bash
source new_env/bin/activate
```

### 2) Clone your repository

* Create a folder in your current directory and run the following command in the terminal set the path to that directory

```bash
git init
```

* Now click on the clone button on the repository page of the project(link: <>)
* Now click on clone via HTTPS option , an address will be copied to your clipboard
* Now run the following command in your machine's terminal and paste the address

```bash
 git clone <paste the address here>
```

### 3) Install all Requirements

* All the project files and folders will be cloned to your local system inside the folder

* Through terminal you have to install all the software requirements of the project which has been specifies in the requirements.txt file.
Run the following command to install all the library and packages.

```bash
 pip3 install -r requirements.txt
```

### 4) Ajdust the location of Dataset

* From the above given link, download the dataset csv file.

* Create a folder named 'DataSet' in your current path and move your dataset csv file inside this folder

* Next rename this file to 'data.csv'

### 5) Check for PEP8 Standards

* Run the following command in your terminal

```bash
flake8 main.py

flake8 module1.py

flake8 module2.py

flake8 module3.py

flake8 module4.py
```

If all these commands run without prompting any message on the terminal, then all PEP8 standards have been followed.

### 6) Run the project

* Next you can run the project main file that is main.py via running this command

```bash
 python3 main.py
```

* In the terminal itself you will get four options of choosing the particular graph you want to see. The option will be from 1 to 4, you can press any option key and hit enter.
* You will be able to see the graph in a new window.

## Contributing

* Fork it!

* Create your feature branch:

```bash
git checkout -b my-new-feature
```

* Commit your changes:

```bash
git commit -am 'Add some feature'
```

* Push to the branch:

```bash
git push origin my-new-feature
```

* Submit a pull request
