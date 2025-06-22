---
title: "Markdown Links Syntax"
date: "2025-05-12"
# last_modified_at: "2025-05-12"
description: "Syntax for local / web links in markdown"
categories: [
  coding
]
tags: [
  markdown
]
---

# Mardown Links
The syntax for a web link is `[text](url)`
- `[Google](https://www.google.co.uk)` shows [Google](https://www.google.co.uk)

The syntax for a local file link is `[text](relative path)` using `./` for the local directory
- `[Node](./2025-05-12-node.md)` shows [Node](./2025-05-12-node.md)
- `[Node](2025-05-12-node.md)` shows [Node](2025-05-12-node.md)
- `[Node](/_posts/2025-05-12-node.md)` shows [Node](/_posts/2025-05-12-node.md)

# Jekyll Links
The syntax for linking to another post involves omitting the extension for the filename, as it will not be a `markdown` file when the site is generated, you also omit the date.

- [Node](/node)
- [Node](../node)
- [Node](./node)
- [Node](node)
- [Node](./posts/node)
- [Node](/posts/node)
- [Node](posts/node)
- [Node]({% post_url 2025-05-12-node %})