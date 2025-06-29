---
title: "Print Directory Tree"
date: "1995-12-22"
# last_modified_at: "2025-06-22"
description: "Print directory tree in Windows"
categories: [
  miscellaneous
]
tags: [
  coding, dev, windows, tips, command line, cmd, cli, terminal, useful commands
]
---

# How to Easily Print Directory Structure in Windows

- You can output straight to terminal with `tree /F /A`
    ```txt
    Folder PATH listing for volume SanDisk
    Volume serial number is 62E8-4963
    E:.
    |   .gitignore
    |   icon.png
    |   icons.svg
    |   index.html
    |   objects.json
    |   README.md
    |   script.js
    |   style.css
    |   
    \---tools
            firebase-wrapper.js
            idb-functions.js
            my-tools.js
            toaster.js
    ```

- You can output straight to terminal with `tree /F`
    ```txt
    Folder PATH listing for volume SanDisk
    Volume serial number is 62E8-4963
    E:.
    │   .gitignore
    │   icon.png
    │   icons.svg
    │   index.html
    │   objects.json
    │   README.md
    │   script.js
    │   style.css
    │
    └───tools
            firebase-wrapper.js
            idb-functions.js
            my-tools.js
            toaster.js      
    ```

- You can output to a text file with `tree /F /A > tree.txt`
    ```txt
    Folder PATH listing for volume SanDisk
    Volume serial number is 62E8-4963
    E:.
    |   .gitignore
    |   icon.png
    |   icons.svg
    |   index.html
    |   objects.json
    |   README.md
    |   script.js
    |   style.css
    |   
    \---tools
            firebase-wrapper.js
            idb-functions.js
            my-tools.js
            toaster.js
    ```

- You can output to a text file with `tree /F > tree.txt` but you will likely get garbled nonsense from the text file
    ```txt
    Folder PATH listing for volume SanDisk
    Volume serial number is 62E8-4963
    E:.
    ³   .gitignore
    ³   icon.png
    ³   icons.svg
    ³   index.html
    ³   objects.json
    ³   README.md
    ³   script.js
    ³   style.css
    ³   
    ÀÄÄÄtools
            firebase-wrapper.js
            idb-functions.js
            my-tools.js
            toaster.js       
    ```

- Example view of the commands in terminal
    ```cmd
    C:\...\directory> tree /F /A
    C:\...\directory> tree /F
    C:\...\directory> tree /F /A > tree.txt
    C:\...\directory> tree /F > tree.txt
    ```