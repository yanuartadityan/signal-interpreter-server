# Intermediate Python S/W Development 

Organized by Veldi Kompetens AB

# 1: Virtual Environment, Setting-Up Flask Server and Git

One of the easiest option to setup *virtual environment* IMO is Python 3's own *venv* built-in package. The simple command to create your new environment is to call `python -m venv [PATH_TO_VENV]`. If you want to bundle *venv*'s environment in the project, you can point your working directory as the PATH, e.g., `python -m venv ./vcc_venv/`. Next you can activate the *vcc_venv* virtual environment by running *activate* script under *./vcc_venv/Scripts/activate*.

This course uses *pipenv* package, therefore you must install the package first by calling `python -m pip install pipenv`. 

Personally, as long as you know what package to use, it's good to put it in *requirements.txt* file. Later on when you invoke `pipenv shell` on your working directory with *requirements.txt* file, *pipenv* will set up Pipfile with all packages copied from the *requirements.txt* file. For *venv*, you can install all packages in *requirements.txt* by invoking `python -m pip install -r requirements.txt`.

Note: This repository has *.gitignore* which contains both *Pipfile* and *Pipfile.lock*, that means when you clone it out, you won't see any Pipfile. You must run pipenv command in the previous paragraph to do so.

# 2: TBD