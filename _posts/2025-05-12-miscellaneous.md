---
title: "Miscellaneous Notes"
date: "2025-05-12"
# last_modified_at: "2025-05-12"
description: "Miscellaneous notes"
categories: [
  miscellaneous
]
tags: [
  notes
]
---

# Miscellaneous

Subprocesses in Command Prompt (CMD), eg via `Python` `subprocess.run` do not maintain environment variables from the initial process **?**

git config --global user.email "username@gmail.com"
git config --global user.name "Forename Surname"

powercfg /batteryreport /output "%USERPROFILE%\Desktop\battery-report.html"
powercfg /batteryreport /output "$env:USERPROFILE\Desktop\battery-report.html"

`JavaScript` scoping for `let`, `var`, `const`

# Windows PATH
Windows `PATH` is an environment variable that `Windows` uses to look for executable code. In its purest form it is a concatenated string of different directory paths. `Windows` uses this as a sort of "root" directory when commands are used eg. in `Command Prompt` or `PowerShell`.

## User PATH vs System PATH
Normally in `Windows` a user environment variable will take precedence over a sytem environment variable, but in the case of `PATH` the two are connected together to make the `PATH` variable. The user `PATH` is appended to the system `PATH` to create the `PATH` variable that `Windows` uses to look for executable code.

You can check the current value of `PATH` using `echo %PATH%` in `Command Prompt` and 
`$env:Path` in `PowerShell`

You can use the `set` command in `Command Prompt` to set environment variables for the current session eg. `set PATH "%PATH%;C:\...\folder"` will append the folder to `PATH` for this session.

It is not recommended to alter `PATH` permanently using the `setx` command, it is better done via `Edit the system environment variables` in `Control Panel`

# foobar2000

[](https://www.foobar2000.org/download)

`foobar2000` `foobar2000 /play /immediate "C:\path\to\folder\"`

`foobar2000 /play /immediate "C:\Users\Ben\Desktop\Core\Media\Sounds\Music\Rainy Spring Morning Ambience.opus"`

You can alter settings to make it minimise to system tray "preferences/display/default user interface/background and notifications"

`foobar2000.exe /play /immediate "C:\Users\Ben\Desktop\Core\Media\Sounds\Music\Rainy Spring Morning Ambience.opus" && foobar2000 /hide`

`/hide` doesn't seem to work with the initial run command

# VSCode Copilot
- When you open a new file you can press `CTRL + I` to open `Copilot`
- If you have it on within the file it will make informed guesses about what you want to type / code (as inline suggestions)