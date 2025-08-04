---
title: "Installing Lua on Windows"
date: "2025-08-04"
# last_modified_at: ""
# description: ""
categories: [
  miscellaneous
]
tags: [
  coding, dev, lua, compiler, binary, path variable, system path, system environment variables, installing lua, command line, cli, terminal, command prompt
]
---

https://www.lua.org/download.html

Lua 5.4.8

Repo is https://luarocks.org/ like PyPi

Remember to attribute `Lua` in projects

You can build the binary yourself using `make` or get the pre-compiled binary from [here](https://luabinaries.sourceforge.net/download.html)

Put the extracted zip contents in a folder like `C:\Lua\bin`, and add that folder to your system `PATH`, you should find `lua54.exe` for `Lua-v5.4.2` and you can check if it is working via `lua54 -v` or `lua54.exe -v`, and run `Lua` itself via `lua54`. You can also rename `lua54` to `lua` if you only plan on having a single version of `Lua` installed on your system.

You should then be able to run `lua main.lua` (remember to restart your terminal / VSCode after updating system environment variables)