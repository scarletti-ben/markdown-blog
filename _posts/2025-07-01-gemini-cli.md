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

# Gemini CLI

## How to Install Gemini CLI

[here](https://github.com/google-gemini/gemini-cli)

`npx https://github.com/google-gemini/gemini-cli` for one time usage, using systemp `TEMP` folder

`npm install -g @google/gemini-cli` for a global install

`npm install @google/gemini-cli` for a local install

then `gemini` to sign in

For auth you can login with `Google` or via `Gemini API Key`, currently testing with `notspam`

```text
> hello

✦ Hello! How can I help you today?

> how does your system work with a project, eg. reading and understanding the file tree

✦ Excellent question. I don't "see" or "understand" a project's file tree visually like you do. Instead, I interact with the file system through a specific
  set of tools and a methodical process.


  Here’s a breakdown of how it works:

  1. Exploration Tools

  I have several tools to explore the file system and its contents. I use them based on what I need to find.


   * `list_directory`: This is my equivalent of ls or dir. I use it to see the immediate contents of a single directory. It's useful for getting a quick look
     at a specific location, like list_directory(path='src/').
   * `glob`: This is one of my most powerful tools for understanding structure. It lets me find files across the entire project that match a pattern. For
     example:
       * To find all Python test files: glob(pattern='**/*_test.py')
       * To find all configuration files: glob(pattern='**/app.config')
       * To find all package manifests: glob(pattern='**/package.json')
   * `search_file_content`: When I don't know which file contains the information I need, I can search the content of all files for a specific keyword or
     pattern (using regular expressions). For example, if you ask me to find where the database connection is defined, I might run
     search_file_content(pattern='database.connect').

  2. Reading Content

  Once I have a list of relevant file paths from my exploration, I use these tools to read their content:


   * `read_file`: Reads the entire content of a single, specific file.
   * `read_many_files`: Reads multiple files at once, which is very efficient for gathering broad context. For example, after finding all *.ts files in a
     directory with glob, I can read them all in one go.


  3. The "Understanding" Process

  This is where my language model capabilities come in. I combine the information from the tools to build a mental model of the project.


   1. Scoping the Project: When you give me a task, I first try to understand the project's landscape. I'll often start by looking for key files:
       * README.md: To understand the project's purpose and setup instructions.
       * package.json, requirements.txt, pom.xml, etc.: To identify the programming language, frameworks, and dependencies.
       * .gitignore: To know what files are intentionally excluded.
       * tests/ or spec/ directories: To understand the testing conventions.


   2. Finding the "Zone of Action": For a specific task like "refactor the login function," I'll use glob and search_file_content to pinpoint the exact files
      and code sections related to "login."


   3. Analyzing the Code: I read the relevant files. I don't just see text; I analyze it for:
       * Imports/Dependencies: What libraries or other modules does this code rely on?
       * Code Style: What are the naming conventions (camelCase, snake_case)? How is the code formatted?
       * Structure: Are there classes, functions, or a different architectural pattern?
       * Context: I read the code surrounding the area of interest to ensure my changes will fit in seamlessly.

   4. Taking Action: Only after building this context do I use tools like replace or write_file to modify code, or run_shell_command to execute build or test
      commands.


  In short, I build my understanding by exploring the file system with targeted searches, reading the content of relevant files, and then using my analytical
  capabilities to piece together the project's structure, conventions, and logic.
```

`gemini-2.5-pro (98% context left)`

`Node.js v18` (`Node 18`) or later