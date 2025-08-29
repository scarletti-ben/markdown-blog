---
title: "Useful Hotkeys"
date: "2025-05-12"
description: "Useful hotkeys for Windows and Windows applications"
categories: [
  reference
]
tags: [
  hotkeys, windows, vscode
]
---

# Hotkeys

## Windows
- `Control + Shift + Click` on an application in the taskbar => run application as administrator
- `Windows + Print Screen` => save a screenshot to `%USERPROFILE%/Pictures/Screenshots`
- `Windows + Shift + S` => open the clipping tool to screenshot a part of the screen
- `Windows + A` => open action center / notification center
- `Windows + D` => toggle the desktop
- `Windows + P` => cycle through display options (for example if a second monitor is attached)
- `Windows + {0-9}` => open (or toggle visible) application on the taskbar in that number position
- `Windows + X` => open a set of `Windows` commands
- `Windows + V` => open the `Windows` clipboard
  - This has a history of things you have recently copied, very useful if you accidentally overwrite something you wanted to paste
- `Windows + X then U then U` => shut down your PC
- `Windows + X then I` => open the terminal
- `Windows + X then A` => open the terminal as administrator

# VSCode
- `Ctrl + K then Ctrl + S` => Open keyboard shortcuts
- `Ctrl + ,` => Open settings
- `Ctrl + Shift + T` => Reopen recently closed tab
- `Ctrl + Shift + F` => Find in all files (in the workspace)
- `Ctrl + Shift + H` => Replace in all files (in the workspace)
- `Alt + Shift + F` => Run the formatter on code, fixing code indents and layout
  - Requires an installed formatter for the current language
- `Ctrl + Alt + ↑ or ↓` => add a new cursor on the line above / below at the same position
  - If you start the first cursor on the longest line of things you plan to select, the new cursors will go to the end point of each new line you add a cursor to
- `Ctrl + Shift + K` => Delete the current line, similar to `Ctrl + X` but without copying the text
- `Ctrl + Shift + D` => Duplicate the current line to the line below
- `Alt + ← or →` => Go back or forward to previously focused text
- `Alt + ↑ or ↓` => Move the current line up or down
- `Shift + Alt + ↑ or ↓` => Copy the current line up or down
- `Ctrl + /` => Toggle line comment
- `Shift + Alt + A` => Toggle block comment
- `Ctrl + G` => Go to a specific line
- `Ctrl + L` => Select the current line
- `Ctrl + Shift + P` => Open the 'Command Palette'
- `Ctrl + P` => Open the 'Quick Open Palette'
- `Ctrl + Shift + [` => Fold the current region / fold mouse selection
- `Ctrl + Shift + ]` => Unfold the current region / unfold mouse selection
- `Ctrl + K then Ctrl + 0` => Fold all comments
- `Ctrl + K then Ctrl + J` => Unfold all comments
- `Ctrl + Shift + L` or `Ctrl + F2` => allows you to change all uses of a given word / token

## VSCode Custom Hotkeys
- `Ctrl + Alt + X` => Open the terminal, or most recent terminal, in the editor area, and pin it
  ```json
  {
      "_description": "View or create terminal in editor area",
      "_extension": "ryuta46.multi-command",
      "key": "ctrl+alt+x",
      "when": "!terminalFocus",
      "command": "extension.multiCommand.execute",
      "args": {
          "sequence": [
              "workbench.action.terminal.focus",
              "workbench.action.terminal.moveToEditor",
              "workbench.action.pinEditor"
          ]
      }
  },
  {
      "_description": "Switch view from terminal to recent file",
      "_extension": "ryuta46.multi-command",
      "key": "ctrl+alt+x",
      "when": "terminalFocus",
      "command": "workbench.action.navigateBack"
  }
  ```

## Miscellaneous
- `Right Click and 'Find All References' or 'Go To References'` => shows all uses of a given word / token
- `Right Click and 'Change All Occurences'` => allows you to change all uses of a given word / token

# Google Chrome
- `Ctrl + W` => Close current tab
- `Ctrl + T` => Open new tab
- `Ctrl + N` => Open new window
- `Ctrl + P` => Print current page
- `Ctrl + Shift + N` => Open new incognito window
- `Ctrl + Shift + T` => Reopen recently closed tab
- `Ctrl + Shift + B` => Toggle the bookmarks bar

# Template
- `Win + `
- `Ctrl + `
- `Alt + `
- `Shift + `
- `Win + Ctrl + `
- `Win + Alt + `
- `Win + Shift + `
- `Ctrl + Alt + `
- `Ctrl + Shift + `
- `Alt + Shift + `
- `Win + Ctrl + Alt + `
- `Win + Ctrl + Shift + `
- `Win + Alt + Shift + `
- `Ctrl + Alt + Shift + `
- `Win + Ctrl + Alt + Shift + `