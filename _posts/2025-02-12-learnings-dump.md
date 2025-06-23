---
title: "Learnings.md Dump"
date: "2025-02-12"
# last_modified_at: "2025-02-12"
description: "Dump of learnings.md from the deleted notes repository"
categories: [
  miscellaneous
]
tags: [
  unsorted, dump
]
---
## JavaScript Reference Guide

#### Click Event Listener
Adding a click event to an element is best achieved via `.addEventListener`, you can then pass a function, or anonymous function that will be called when a click event occurs involving that element

`element.addEventListener('click', func);`
`element.addEventListener('click', () => func());`
```javascript
element.addEventListener('click', function() {
    console.log();
});
```

Can be async, use named or anonymous functions

#### Finding Elements
```javascript
document.querySelector
document.querySelectorAll
document.getElementById
document.getElementsByClassName
document.getElementsByTagName
```

#### Semicolons
It's advised to use semicolons but in testing you can rely on Automatic Semicolon Insertion (ASI), which is a feature from ECMAScript (ECMA) which allows semicolons to be optional in JavaScript. ASI is not perfect and can cause still lead to syntax errors and unexpected behaviour.

#### 'for' Loop
There is a newer way to create for loops in `JavaScript` that is more syntactically similar to `Python`, the first method below

```javascript
const array = [1, 2, 3, 4];
for (const item of array) {
    console.log(item);
}
```

Another way is the `forEach` loop which is similar to an enumeration in `Python` using `for index, item in enumerate(array)`
```javascript
array.forEach((item, index) => {
  console.log(index, item);
});
```

The older method relies upon incrementing, and uses a start value `let i = 0`, a conidition `i < array.length`, and   something that happens each loop `i++` which increments `i` by one
```javascript
const array = [1, 2, 3, 4];
for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}
```

#### JavaScript Arrow Function `=>` / Anonymous Function
Used with or without function body `{}`

`document.addEventListener('click', () => console.log('test')`

```javascript
document.addEventListener('click', () => {
    let value = x * 2
    console.log(value);
});
```

Analogous with anonymous functions in `Python` via `lambda: print('hello')` or `lambda x: print(x)`

#### Script Defer
Using `<script src="script.js" defer></script>` instead of `<script src="script.js"></script>` saved from needing to wrap all functionality into `main` function in `script.js` and calling `document.addEventListener('DOMContentLoaded', main)`. Which sounds like it wasn't a big deal in theory, but global variables could not be defined outside of `main` for fear that they might been assigned before the document elements load in, meaning lots of `declaration without initialisation` statements / `uninitialised variables` which were later initialised once `main` was called.

#### Boilerplate
```html
<!DOCTYPE html>
<html lang="en">
<head>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Template</title>

  <!-- ! Imports -->

  <!-- ! CSS -->
  <link rel="stylesheet" href="styles.css">

</head>
<body>

  <!-- ! HTML -->
  <div id="page">
    
  </div>

  <!-- ! JavaScript -->
  <script src="script.js" defer></script>

</body>
</html>
```

```css

```

#### Snippets
```javascript

// Get ECMA date time string YYYY-MM-DDTHH:mm:ss.sssZ
function getDateString() {
    const date = new Date();
    const string = date.toISOString();
    return string;
}

// Custom HTML element, with this.element attribute
class Custom {
    constructor() {
        this.element = document.createElement('div');
    }

    // Log text content of the element attribute
    show() {
        console.log(this.element.textContent);
    }
}

```

```javascript
static staticMethod() {
  console.log(this) // Here 'this' refers to the class itself
}
```

#### Miscellaneous
You can add docstrings in `JavaScript` as below
```javascript
/**
 * Add two numbers and return the result
 * @param {number} a, the first number
 * @param {number} b, second number
 * @returns {number} the sum of a and b
 */
function add(a, b) {
    return a + b;
}
```
- You can find ways to auto generate these docstrings

Requests return status codes and 200 and 201-299 are considered successful status codes

#### Things I Keep Forgetting / Mistakes I Keep Making
- CSS only has block commenting so you try and comment something out that has a comment inside and it does not work, or you try and uncomment one line of a block comment and it doesn't work (use custom hotkey Ctrl + F1 to fix some issues)
- JavaScript has a less polluted namespace so you can use words you'd expect to be reserved eg. `let string = 'test'`
- Declaring a variable or constant in the global scope, then assigning it a value in a function affects the global pointer eg. `var test = 5` in global with `test = 6` in a function call will alter the global value of `test`. Whereas using `var test = 6` in the function will create a function scoped `test` variable.
- Add `"use strict";` to a function or the script itself to disallow assigning value to an undeclared variable
- Asynchronous functions do work how they should, but they make every function that calls them need to be async if they care about waiting for the result, rather than just the act of firing them
- You can use `margin: auto` in many cases to avoid using `display: flex` on parent, and avoiding some quirks
- `display: flex` can throw a real tantrum with scrolling / overflow if any of the elements are too big for its defined space
- Remember to use `flex-grow: 0`, `flex-shrink: 0`, `flex-grow: 1`, `flex-shrink: 1` more often on flex elements within a `display: flex` parent
- `position: absolute` requires the parent to have a `position` attribute such as `relative` or `absolute`, and the element will then be placed within the parent but out of the flow of its layout. An example would be `position: absolute; top: 0; left: 0;` which would place the element in the top left of the parent above all other elements, you may need `z-index` in certain situations to ensure it is on top
- Using `display: none !important` can ensure an element is hidden, useful in the class below
```css
.hidden {
  display: none !important;
}
```
- You can toggle classes with `element.classList.toggle(name)`, remove classes `element.classList.remove(name)`, and add classes `element.classList.add(name)`, there will be no effect for a remove if it is not present, and no effect for an add if it is already present so they are safe methods
- You can change a `CSS` style, rather than an element specificially by using something like `document.querySelector('.hidden').style.display = 'block';`
- You can clear all temporary `JavaScript` in-line styles from a given element using `element.style = ''`, or reset a specific attribute to its `CSS` value using something like `element.display.style = '';`
- Asynchronous code returns a `Promise` object, you can either `await` promises so that a function is blocked until the promise is resolved, or use a callback via `Promise.then()` which will run the callback when the promise resolves
```javascript
asyncFunction()
  .then(result => {
    console.log('success');
  })
  .catch(error => {
    console.log('error');
  });
```
- Text from different elements is usually attained via one of the ways below
```javascript
element.textContent;
element.value;
element.innerHTML;
element.innerText;
```
- `box-sizing: border-box;` fixes a great many problems in which padding, margin and border change the size and layout of an element
- `user-select: none;` is useful to avoid text selection on double-click for an element

#### Niche Bugs
Had an issue where tapping between a non-empty textarea and a clickable div on mobile led to the phone trying to google search an empty string, hacked / fixed by clearing all window selection on clicking into the clickable div
```javascript
function clearSelection() {
  if (window.getSelection) { // Modern
    window.getSelection().removeAllRanges();
  } else if (document.selection) { // Legacy
    document.selection.empty();
  }
}
```

Had an issue where triple-clicking on dekstop in an empty contenteditable element tried to essentially tab to another text element even though they were not direct siblings, seemingly some sort of inate behaviour searching for nearest text nodes for a paragraph select / select all mechanic

Some older CDN modules / packages aren't setup to be imported easily with modern import export / require define syntax

FFmpeg WASM is broken at the moment or underdocumented


#### Installing `npm` for JavaScript
The main package manager for `JavaScript` is `npm`, and it works similar to `pip` in `Python`

Install nvm for windows (as the actual nvm is for linux), then use that to install node

nvm -v
nvm install latest
nvm use 23.7.0
node -v
npm -v

nvm allows you to switch the currently used version of node depending on the project with nvm use x.y.z

#### You can add your own custom .bat files to CMD path to call them globally
- Have decided to use folder `C:\bscripts`