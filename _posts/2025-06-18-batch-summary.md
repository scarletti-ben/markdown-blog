---
title: "Windows Batch File Syntax / Summary / Cheat Sheet"
date: "2025-06-18"
date-modified: "2025-06-18"
description: "Windows Batch File Syntax / Summary / Cheat Sheet"
categories: [
  coding
]
tags: [
  coding, dev, batch, microsoft windows, .bat, cheat sheet, cmd, command line, cli
]
---

# Overview
Below is a code block that contains a cheat sheet `batch` file for `Microsoft Windows`, that I wrote a while ago. It is by no means complete, and likely contains a fair few errors, but was useful for my learning purposes at the time

```batch
:: Comments in batch files are done via "REM" or "::"
:: You can use the "@" symbol to hide a command, it will not hide its output
REM Using the "REM" command without "@" symbol leaves the command visible on the line above
@REM Using the "REM" command with the "@" symbol hides the command
:: Using :: is not a command, and does not need the "@" symbol
:: Comments can also be called 'remarks' in batch files
:: Comments ignore all special characters, for instance ' or " or @ or ^
:: Comments only work if they are at the start of the line [see in-line comments below]
:: NOTE: You can have unintended issues in some scripts when using "::" rather than "@REM"

:: The main purpose of the "^" symbol is to escape a special character, including itself, in a command
@echo The '^&' symbol is escaped by the '^^' symbol

:: The secondary purpose of the "^" symbol is to continue a single command on another line
@echo this is the first half of the command ^
and this is the second

:: The main purpose of the "&" symbol is to chain two commands together
@echo Command chain using the chain symbol "^&" and the hide symbol @ & @echo The second part of the chain

:: The secondary purpose of the "&" symbol is for in-line comments
@echo Testing in-line comments 1 & @REM This is an in-line comment
@echo Testing in-line comments 2 & :: This is also an in-line comment, and the rest of this document will use them in this format

@echo off & :: You can turn off echo entirely using "echo off"
@echo testing direct echo command after echo set to off & :: Direct echo commands will still work
@echo on & :: You can turn on echo using "echo on"
@echo. & :: You can use "@echo." to send an empty line, similar to python print("", end = "\n")

@pause & :: You can use "pause" to pause the script and wait for user input

:: ================================================================================================
:: Testing
:: ================================================================================================

@echo off
setlocal
:: setlocal ensures that any changes to environment variables are local to the script.
:: setlocal has no effect outside of a batch file

:: Prompt the user for input and store it in the variable "userInput"
set /p userInput=Enter your name: 

:: Print the value of the variable "userInput"
echo Hello, %userInput%!

endlocal 
:: endlocal ends the command block where the local variable was

echo Hello, %userInput%!

@echo off
set MY_VAR=GlobalValue
echo Before setlocal: %MY_VAR%

setlocal
set MY_VAR=LocalValue
echo Inside setlocal: %MY_VAR%
endlocal

echo After endlocal: %MY_VAR%

echo Invalid: %test123%

pause

:: ================================================================================================
:: Testing
:: ================================================================================================

@REM Other symbols
:: & separates commands on a line.
:: && executes this command only if previous command's errorlevel is 0.
:: || executes this command only if previous command's errorlevel is NOT 0
:: > output to a file
:: >> append output to a file
:: < input from a file
:: | output of one command into the input of another command
:: ^ escapes any of the above, including itself, if needed to be passed to a program
:: " parameters with spaces must be enclosed in quotes
:: + used with copy to concatenate files. E.G. copy file1+file2 newfile
:: %variablename% an inbuilt or user set environmental variable
:: !variablename! a user set environmental variable expanded at execution time, turned with SetLocal EnableDelayedExpansion command
:: %<number> (%1) the nth command line parameter passed to a batch file. %0 is the batchfile's name
:: %* (%*) the entire command line
:: %<a letter> or %%<a letter> (%A or %%A) the variable in a for loop. Single % sign at command prompt and double % sign in a batch file

:: Ending a script with cmd /k will keep it open in the event that it ends
@cmd /k
:: If you are having issues with cmd /k, run the file manually via command prompt
:: C:\...\...>cmd /k filename.bat
```