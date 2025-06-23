---
title: "HTML Notes Dump"
date: "2023-10-31"
# last_modified_at: "2025-06-18"
description: "Dump of html-notes.txt, converted to Markdown"
categories: [
  miscellaneous
]
tags: [
  unfinished, dump
]
---

# `HTML` Notes

**Tutorial Source:**  
https://www.w3schools.com/html/html_intro.asp

**HTML Tester:**  
https://www.w3schools.com/html/tryit.asp?filename=tryhtml_intro

---

## Lesson One  
https://www.w3schools.com/html/html_intro.asp

- `HTML` stands for Hyper Text Markup Language  
- `HTML` is the standard markup language for creating languages  
  `< A markup language is a system for annotating or adding information to specify structure, presentation, or meaning. Markup languages are used to format and describe in a way that is both human-readable and machine-readable.`  
- `HTML` describes the structure of a web page  
- `HTML` consists of elements  
- `HTML` elements tell the browser how to display the content  
- `HTML` elements label pieces of content  

### Example 1

```html
<!DOCTYPE html>
<html>
<head>
    <title>Your Page Title</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a simple website with some content.</p>
    <!-- Add more content here -->
</body>
</html>
```

### Explanation

* The `<!DOCTYPE html>` declaration defines that this document is an HTML5 document

* The `<html>` element is the root element of an `HTML` page

* The `<head>` element contains meta information about the `HTML` page

* The `<title>` element specifies a title for the `HTML` page

  * Shown in the browser's title bar or in the page's tab

* The `<body>` element defines the document's body, and is a container for all the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.

* The `<h1>` element defines a large heading

* The `<p>` element defines a paragraph

* Most `HTML` elements are defined by a start tag, content and an end tag

* Some `HTML` elements have no content and are called empty elements

  * One example is the `<br>` element which does not have an end tag

* Web browsers read `HTML` documents and attempt to display them

* Web browsers do not show users the `HTML` tags, only the content

* Content in the `<body>` section will be displayed in the browser

* Content in the `<title>` element will be shown in the browser's title bar or browser tab

* The `HTML` versions from 2008 are `HTML` 5 to `HTML` 5.2

---

## Lesson 2

[https://www.w3schools.com/html/html\_editors.asp](https://www.w3schools.com/html/html_editors.asp)

* Web pages can be created and modified using `HTML` editors

  * Or they can be edited with notepad / VSCode etc.
* Save the file with the `.html` or `.htm` extension

  * `index.html` is the default
* Choose "Open with Chrome" when right clicking file and Chrome will display

---

## Lesson 3

[https://www.w3schools.com/html/html\_basic.asp](https://www.w3schools.com/html/html_basic.asp)

* All `HTML` documents must start with a document type declaration:
  `<!DOCTYPE html>`

* The `<!DOCTYPE>` declaration helps browsers display web pages correctly

  * It is not case sensitive `<!doctype html>`
  * It only appears once and does not need to be closed
  * `<!doctype html>` is the declaration for HTML5

* The document itself then begins with `<html>` and ends with `</html>`

  * Forward slashes close or end an element

* The visible part of an `HTML` document is within the `<body>` and `</body>`

* `HTML` headings are defined with the `<h1>` to `<h6>` tags

  * `<h1>` is the most important heading
  * `<h7>` is the least important heading

* `HTML` paragraphs are defined with the `<p>` tag

  * The element is closed with the `</p>` tag

* `HTML` links are defined with the `<a>` tag

  * Inside the `<a>` tag is where the link goes
  * The link's destination is specified with the `href` attribute
  * The content between `<a>` and `</a>` is the text displayed on the link

```html
<a href="https://www.w3schools.com">This is a link</a>
```

* This shows a link with the text: "This is a link"

* `HTML` images are defined with the `<img>` tag

  * The attributes are:

    * `src` for the source file
    * `alt` for the alternative text

      * This is displayed to user if the image does not load
    * `width` for the width, it will stretch
    * `height` for the height, it will stretch

```html
<img src="img_girl.jpg" width="500" height="600">
```

* Image source can be:

  * Absolute URL:
    `src="https://www.w3schools.com/images/img_girl.jpg"`
  * Relative URL (to the domain if it begins with a slash `/`):
    `src="/images/img_girl.jpg"`
  * Relative URL (to the current web page):
    `src="img_girl.jpg"`

    > This is recommended in case domain changes

* You can view `HTML` source with `Ctrl + U` in Chrome or right click to inspect

  * You can also right click and "View page source"

* No part of `HTML` is case sensitive but lowercase is recommended

---

## Lesson 6

[https://www.w3schools.com/html/html\_attributes.asp](https://www.w3schools.com/html/html_attributes.asp)

* The `style` attribute adds styles to an element such as colour, font or size

```html
<p style="color:red;"> This is a red paragraph.</p>
```

* The `lang` attribute should only be used once to declare the language of the web page

```html
<!DOCTYPE html>
<html lang="en">
```

Or

```html
<!DOCTYPE html>
<html lang="en-US">
```

* Where the first two letters indicate language and the second are country

* The `title` attribute defines extra information about an element

  * The value of this title shows in the tooltip when you mouse over the element

```html
<p title="I'm a tooltip"> Hover over this paragraph.</p>
```

* Quotation marks `"` are not technically required in `HTML` standard

  * They are recommended as otherwise spaces cause issues

* Single quotes and double quotes work much like Python, if single quotes are needed in the text, use double, if the double quotes are needed use single outside

### Lesson Summary

* All `HTML` elements can have attributes
* The `href` attribute of `<a>` specifies the URL of the page the link goes to
* The `src` attribute of `<img>` specifies the path to the image to be displayed
* The `width` and `height` attributes of `<img>` provide size information for images
* The `alt` attribute of `<img>` provides an alternate text for an image
* The `style` attribute is used to add styles to an element, such as color, font, size, and more
* The `lang` attribute of the `<html>` tag declares the language of the Web page
* The `title` attribute defines some extra information about an element

---

## Lesson 7

* Web pages use headings to index the structure and content of a web page
* Do not use headings simply to make text larger, use them only for section headings
* Each heading has a default size `<h1>` to `<h6>`

  * You can alter a heading size if you wish

```html
<h1 style="font-size:60px;">Heading 1</h1>
```

---

## Lesson 8

* `HTML` paragraphs `<p>` always start a new line and browsers automatically add white space before and after a paragraph (called a margin)

* You cannot be sure how `HTML` will be displayed on a given device, large or small screens, and resized windows will give different results

* `HTML` has the horizontal rules tag `<hr>`

  * This tag defines a thematic break in an `HTML` page
  * It looks like a very long line across the page left to right
  * `<hr>` is an empty tag and does not need to be closed

```html
<h1>This is heading 1</h1>
<p>This is some text.</p>
<hr>
<h2>This is heading 2</h2>
```

* `HTML` line break elements are created with the `<br>` tag

  * `<br>` is an empty tag and it does not need closing

### \~ Multi-Line Text

* Despite being written across multiple lines this will display on one line:

```html
<p>
Line
Line 2
</p>
```

* To fix this we use the `<pre>` element which defines preformatted text

```html
<pre>
Line
Line 2
</pre>
```

* This is usually displayed with a fixed width (monospace) font and preserves spaces and line breaks

---

## Lesson 9 - `HTML` Styles

*Unfinished*
[https://www.w3schools.com/html/html\_styles.asp](https://www.w3schools.com/html/html_styles.asp)

* The style of an `HTML` element can be done with the `style` attribute
* The `HTML` style attribute has the following syntax:
  `<tagname style="property:value;">`
* The property is a CSS property