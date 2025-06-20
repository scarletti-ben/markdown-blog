---
title: "Cloning Python and Node.js Projects from GitHub"
date: "2025-05-14"
date-modified: "2025-05-14"
description: "Cloning Python / Node.js projects from GitHub"
categories: [
  coding
]
tags: [
  webdev, github, git, clone, cloning, python, pip, pypi, dependencies, javascript, node, node.js, npm, node package manager, node version manager, nvm, command prompt, command-line interface, cli
]
---

# Installing Python Repository and Dependencies (Windows)
Before starting, ensure that you have `git` and `python` installed on your system. Open your terminal and navigate to the location where you want your local repository to be created.

## Process (Command Prompt)
- Clone the repository to your system
    - `git clone https://github.com/{username}/{repository}`
- Change into the repository on your system
    - `cd {repository}`
- Create the virtual environment within the local repository
    - `python -m venv venv`
- Activate the virtual environment
    -  `.\venv\Scripts\activate`
- Verify the virtual environment is active
    - `where python`
- Install packages defined in `requirements.txt` from `PyPi`
    - `pip install -r requirements.txt`
- [Optional] Update the packages defined in `requirements.txt`
    - `pip install --upgrade -r requirements.txt`
- Verify the packages installed within the virtual environment
    - `pip list`
- Run the entry point script
    - Use `python -m main.py` if `main.py` is part of a package
    - Use `python main.py` if `main.py` is not part of a package

### Example
![alt text](/assets/gif/gif001-python-clone.gif)

> [!NOTE]
> By default, if you are not working in a virtual environment, `pip` installs packages to the global `site-packages` folder

# Installing Node.js Repository and Dependencies (Windows)
Before starting, ensure that you have `git` and `Node Version Manager` (`nvm` installed on your system. Open your command prompt and navigate to the location where you want your local repository to be created.

## Process (Command Prompt)
- Clone the repository to your system
    - `git clone https://github.com/{username}/{repository}`
- Change into the repository on your system
    - `cd {repository}`
- Install and use required `node` / `npm` version from `.nvmrc` 
    - `nvm install`
    - `nvm use`
- Verify your `node` version
    - `node -v`
    - `npm -v`
- Install project dependencies defined in `package.json` from `npm` registry
    - `npm install`
- Verify the packages installed  
    - `npm list --depth=0`
- [Optional] Update all packages to latest compatible versions  
    - `npm update`
- Run entry point of the project
    - Use `npm start` if defined in `package.json`
    - Otherwise use `node app.js` or `node index.js`
- [Miscellaneous] Commands that may be configured by the project
    - `npm run dev` to run development server if configured
    - `npm run build` to build project if configured
    - `npm test` to run tests if configured