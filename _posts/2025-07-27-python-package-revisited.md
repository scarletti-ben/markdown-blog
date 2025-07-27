---
title: "Python Packages Revisited"
date: "2025-07-27"
# last_modified_at: ""
# description: ""
categories: [
  miscellaneous
]
tags: [
  coding, dev, python, packages, pip
]
---

# Python Packages Revisited
I have always struggled with managing `Python` packages, especially as I end up with long chains of relative imports like `from ...thing import stuff`, but it turns out that a `Python` package always knows the root package name, and can access things from the root package downward via `from package.things.thing import stuff`

> [!NOTE]
> - Trying to run a `Python` script within the package, without calling it via the package itself will run into errors that mention `no known parent package`
> - By default you execute a package via `python -m package.module_name`
> - If the package has a `__main__.py` then you can use `python -m package` and this will execute the code in `package.__main__`

An example directory for a `Python` package that uses the `package.module` syntax can be found below. It uses `__init__.py` files to expose functions from within folders for easier access from `package`, and lays out the possibilty of a `core` directory of features that all modules within the package can access with ease

# Directory Tree

```text
project/
└── package/
    ├── core/
    │   ├── features.py
    │   └── __init__.py
    ├── tools/
    │   ├── things.py
    │   └── __init__.py
    ├── __init__.py
    └── __main__.py
```

# `package/`

```text
package/
├── core/
├── tools/
├── __init__.py
└── __main__.py
```

## `__init__.py`

```python
"""Serves as the public API for the package"""
# < =======================================================
# < Imports
# < =======================================================

from .core import feature
from .tools import thing
```

## `__main__.py`

```python
"""Package entry point, accessed via python -m package"""
# < =======================================================
# < Imports
# < =======================================================

from .tools import thing

# < =======================================================
# < Execution
# < =======================================================

thing()
```

## `core/`

```text
core/
├── features.py
└── __init__.py
```

### `__init__.py`

```python
"""Expose features to be accessed via package.core"""
# < =======================================================
# < Imports
# < =======================================================

from .features import feature
```

### `features.py`

```python
"""Features to be exported via package/core/__init__.py"""
# < =======================================================
# < Features to be Exported
# < =======================================================

def feature() -> None:
    """Feature function to print information"""
    print("You have called function 'feature'")
    print("Feature function accessible via package.core")
    print("Feature function accessible via package.core.features")
```

## `tools/`

```text
tools/
├── things.py
└── __init__.py
```

### `__init__.py`

```python
"""Expose features to be accessed via package.tools"""
# < =======================================================
# < Imports
# < =======================================================

from .things import thing
```

### `things.py`

```python
"""Things to be exported via package/tools/__init__.py"""
# < =======================================================
# < Imports
# < =======================================================

from package.core import feature

# < =======================================================
# < Things to be Exported
# < =======================================================

def thing() -> None:
    """Thing function to print information"""
    print("You have called function 'thing'")
    print("Thing function accessible via package.things")
    print("Thing function accessible via package.things.thing")
    print("Preparing to call package.core.features.feature()\n")
    feature()
```