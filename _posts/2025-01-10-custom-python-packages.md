---
title: "Custom Python Packages"
date: "2025-01-10"
# last_modified_at: "2025-01-10"
# last_modified_at: "2025-01-10"
categories: [
  coding
]
tags: [
  dev, python, python packages, pypi, egg, egg-link, imports
]
---

# Custom Python Packages
Python packages are normally installed via `pip` eg. `pip install package-name`, or are inbuilt packages that don't need installing manually eg. `random`. Once installed you can import a package using the `import` keyword in your script eg. `import package_name`.

Package names usually follow the format `package-name` but are imported via `import package_name`.

## PyPi
[PyPi](https://pypi.org/) is the main python package index and is usually where `pip` is searching in order to install and update packages, users can upload packages to `PyPi`.

Python packages submitted to `PyPi` should be formatted in a certain way in order to function correctly as packages, and allow `pip` to install them successfully.

## Formatting a Custom Python Package
You can format a package specifically for `PyPi` but it's also possible to make custom python packages locally, that aren't going to be uploaded to `PyPi`

# Mess
`package_name.egg-info` directory