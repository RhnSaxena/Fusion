# FusionIIIT
[![Maintainability](https://api.codeclimate.com/v1/badges/f82b80eb18f62f88fbfe/maintainability)](https://codeclimate.com/github/sdhiman99/Fusion/maintainability)

**FusionIIIT** is the automation of various functionalities, modules and tasks of/for **PDPM Indian Institute of Information Technology, Design and Manufacturing, Jabalpur** being developed in `python3.8` and using `Django` Webframework.

## System Configuration

* Ubuntu `20.04` **(Recommended)**
* *OR* WSL for Windows `10` \(Follow the guide below\) :  
    [Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* *OR* Windows `7/8/8.1/10`

## Software Requirements

* Python `3.8`
* Git

## How to get started

* on **Ubuntu**:

    ```sh
    // Install the required packages using the following command:
    
    sudo apt install python3-pip python3-dev python3-venv libpq-dev build-essential git
    sudo -H pip3 install --upgrade pip
    ```

* on **Windows**:

  * Get Python 3.8 from [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe) for AMD64/x64 or [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe) for x86
  * Git from [here](https://git-scm.com/download/win)
  * Install both using the downloaded `exe` files   
  **Important:** Make sure to check the box that says **Add Python 3.x to PATH** to ensure that the interpreter will be placed in your execution path

### Downloading the Code

* Go to (<https://github.com/FusionIIIT/Fusion>) and click on **Fork**
* You will be redirected to *your* fork, `https://github.com/<your_user_name>/Fusion`
* Open the terminal, change to the directory where you want to clone the **Fusion** repository
* Clone your repository using `git clone https://github.com/<your_user_name>/Fusion`
* Enter the cloned directory using `cd Fusion/`

### Setting up environment

* Create a virtual environment  
  * on **Ubuntu**: `python3 -m venv env`  
  * on **Windows PowerShell**: `python -m venv env`
* Activate the *env*    
  * on **Ubuntu**: `source env/bin/activate`
  * on **Windows PowerShell**: `.\env\Scripts\Activate.ps1`     
  **Note** : On Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following command: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
* Install the requirements: `pip install -r requirements.txt`

### Running server

* Change directory to **FusionIIIT** `cd FusionIIIT`
* Run the server `python manage.py runserver`

## Working with Code \(Method 1\)

### Setting upstream

* `git remote add upstream https://github.com/FusionIIIT/Fusion`
  * Adds the remote repository (the repository you forked from) so that changes can be pulled from/pushed to it

### Switching branch

* `git checkout -b <module-name>`
  * Creates a new branch `<module-name>` in your repository
* `git checkout <module-name>`
  * Switches to the branch you just created
  
### Migrating Changes (Database)

* Make migrations `$ python manage.py makemigrations`  
* Migrate the changes to the database `$ python manage.py migrate`

### Committing

* `git add .`
  * Adds the changes to the staging area
* `git commit`
  * Commits the staged changes

### Syncing

#### Pulling

* `git pull upstream master`
  * Pulls the changes from the *upstream* master branch

#### Pushing

* `git push -u origin <module-name>`
  * Pushes the changes to your repository **\(First time only\)**; using `git push` is sufficient later on
* Go to `https://github.com/<your_user_name>/Fusion/tree/<module-name>` and create pull request

## Working with Code \(Alternative\)

* **(Recommended)** Use [Visual Studio Code](https://code.visualstudio.com/) as a text editor. Go through the [Tutorial](https://code.visualstudio.com/docs/python/python-tutorial) for getting started with **Visual Studio Code for Python**.  
**Note** : Use the following guide if using **WSL** for Development  
    (<https://code.visualstudio.com/docs/remote/wsl>)
* Use the inbuilt **Source Control** feature for checking out, committing, pushing, pulling changes. You can also use [Github Desktop](https://desktop.github.com/) **_\(Windows/Mac only\)_**.  
* Refer to below link for best practices regarding commit messages :  
    (<https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53>)

## Different modules included

* Academic database management  
* Academic workflows  
* Finance and Accounting  
* Placement Cell  
* Mess management  
* Gymkhana Activities  
* Scholarship and Awards Portal  
* Employee Management  
* Course Management  
* Complaint System  
* File Tracking System  
* Health Centre Mangement  
* Visitor's Hostel Management  
* Leave Module
