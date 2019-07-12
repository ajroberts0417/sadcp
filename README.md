# SADCP Monolith

A monolithic Django project for SADCP. May Charlie, Chingachgook, the Emer of Smer, and the Brooklynese Guy guide us.

## Contributing Code

- New commits should always be proposed in a [Pull Request](https://help.github.com/articles/about-pull-requests/)
- Every Pull Request requires at least one approval before merging
- This project uses [Black](https://github.com/python/black) for python style & formatting

## Quickstart

To start the server, ensure you have the dependencies installed in the Setup section below. Verify that Postgres is running using the default port.

Run this command to install Python dependencies to a virtual environment managed with Pipenv:

```bash
make install-dev
```

Run this command to start the local development server:

```bash
SECRET_KEY=notsecure DEBUG=1 make run
```

## Setup

### System Dependencies

This project requires the following software installed on the target operating system:

- [GNU Make](https://www.gnu.org/software/make/)
- [Python 3.7](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [Postgresql](https://www.postgresql.org/)

### macOS

#### Step 1: Install Xcode and enable command-line tools

Install Xcode in the App Store and then run this command to ensure the latest packaged version of `make` is available in your `PATH`.

```sh
xcode-select --install
```

#### Step 2: Ensure you have Python 3.7 installed

Check your currently installed version of Python 3.

```sh
python3 --version
```

If you don't have Python version 3.7, the Pipfile will not complete installation. Install or upgrade to Python 3 using [Homebrew](https://brew.sh/):

```sh
brew install python3
```

#### Step 3: Install Pipenv using Homebrew

Run this in your terminal:

```sh
brew install pipenv
```

**NOTE:** dependencies will only be available within the `pipenv` virtualenv. Enter the virtualenv with `pipenv shell`, or run a single command with `pipenv run my-cool-command`.

#### Step 4: Install Postgres using Homebrew

Run this in your terminal:

```sh
brew install postgresql
```

Postgres should start automatically. If you run into trouble, refer to [this guide](https://goonan.io/setting-up-postgresql-on-os-x-2/).

### Windows

#### Suggestion: Install a console emulator running on ConEmu

My personal recommendation is [Cmder](http://cmder.net/)

#### Step 1: Install Chocolatey, a package manager for windows

Install [chocolatey](https://chocolatey.org/install)

#### Step 2: Install make

Run this in your console
```sh
choco install make
```

Verify your installation of make:
```sh
refreshenv
make --version
```

#### Step 2: Ensure you have Python 3.7 installed

Check your currently installed version of Python.
```sh
python --version
```

If you don't have Python version 3.7, install or upgrade to Python 3 using Chocolatey:
```sh
choco install python
```

#### Step 3: Install Pipenv using pip

Python3 should install pip automatically, but check for updates with the following command:
```sh
python -m pip install -U pip
```

Now install pipenv with a User installation:
```sh
pip install --user pipenv
```

**NOTE:** If pipenv isn't available in your console after installing and running `refreshenv`
you will need to add the user base's binary directory to your PATH. This is relatively simple, read the Yellow Box on [this tutorial page](https://python-docs.readthedocs.io/en/latest/dev/virtualenvs.html#virtualenvironments-ref)

**NOTE 2:** dependencies will only be available within the `pipenv` virtualenv. Enter the virtualenv with `pipenv shell`, or run a single command with `pipenv run my-cool-command`.

#### Step 4: Install Postgres using Chocolatey

Postgres requires a password parameter, so run the following command, with your own password to be assigned to the postgres user:

```sh
choco install postgresql10 --params '/Password:YOURPASSWORDHERE' --params-global
```

Postgres should start automatically. If you run into trouble, refer to the [Postgres website](https://www.postgresql.org/download/windows/).

### Ubuntu 18.04

#### Step 1: Install build tools with apt-get

First, make sure you have `make`:

```sh
sudo apt-get update
sudo apt-get install build-essential -y
```

#### Step 2: Ensure you have Python 3.7 installed

Check your currently installed version of Python 3.

```sh
python3 --version
```

If you don't have Python version 3.7, the Pipfile will not complete installation. You will need to use the PPA provided by the _deadsnakes_ team.

```sh
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7 -y
```

#### Step 3: Install Pipenv using Pip

Run this command with `sudo` permissions to ensure `pipenv` is in your `PATH`.

```sh
sudo pip3 install pipenv -U
```

#### Step 4: Install Postgres with apt-get

Run this command to ensure Postgres is installed:

```sh
sudo apt-get update
sudo apt install postgresql postgresql-contrib -y
```

Postgres should run as a daemonized process and start automatically.

## System Status Checks

### Checking if Postgres is running

Sometimes, a configuration error can cause Postgres to fail on startup. To check the status of the process, run this command:

```sh
pg_ctl status
```

## Deploys

We currently deploy to Heroku. Install their CLI with `brew install heroku/brew/heroku`. Branches are deployed to Heroku by pushing to the corresponding `git` remote for staging or production. You can add each remote thusly:

```bash
# 1. add the git remote for sadcp
heroku git:remote -a sadcp
```

Now you can deploy to Heroku using the `deploy` make target See examples below.

```bash
# deploy your local master branch to heroku
make deploy
# deploy another local branch to heroku
make deploy REF=my-cool-branch
# deploy a specific commit to heroku by its SHA
make deploy REF=abc123def456abc123def456abc123def456
```


## Useful Commands

**Run All Tests and Checks**

`make test`

**Run Black, Lint, Type Checks, or Tests**

`make [black | lint | mypy | test-unit | test-int]`

**Tail Logs from Heroku remote**

`heroku logs --tail --remote heroku`


## Further Reading

**[Configuring Heroku for Django](https://devcenter.heroku.com/articles/django-app-configuration)**

A very brief guide for people in a hurry.
