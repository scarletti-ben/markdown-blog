# Markdown Blog
This repository contains the source code for a blog site that is hosted on `GitHub Pages` [here](https://scarletti-ben.github.io/markdown-blog/). It uses the `Chirpy` theme for `Jekyll` and converts `Markdown` files to `HTML` pages during the build process.

## Jekyll
`Jekyll` is a static site generator that converts `Markdown` files to `HTML` pages. It uses templates to ensure the resulting pages are close to uniform, and can also read `YAML` "front matter" from `Markdown` files as a sort of file metadata.

For this repository the setting for `GitHub Pages` "Build and deployment/Source" [here](https://github.com/scarletti-ben/markdown-blog/settings) is set to "GitHub Actions". You don't always need to turn this setting on, and `Jekyll` may still run if a repository is in a compatible structure. But with the setting on you can customise the build process a little more, and use unsupported plugins. In essence you can control `GitHub Actions` more precisely.

Currently the repository is set up to run the build process whenever a change is pushed to the `main` branch, you can check the status of each build via the "actions" tab of the repository [here](https://github.com/scarletti-ben/markdown-blog/actions). If there are any errors, you can read the logs.

> [!NOTE]
> One example error from this repository comes from `htmlproofer`, which is a `Ruby` `gem` that tries to validate the site in the final stages, and often finds that links within `Markdown` files are broken as the local file references don't match built site paths. Currently `htmlproofer` is disabled within `pages-deploy.yml`

## Chirpy
This repository was generated from the template repository [`chirpy-starter`](https://github.com/cotes2020/chirpy-starter) via the "Use this template" button. `Chirpy` is a theme `gem` for `Jekyll`, and `chirpy-starter` makes it quite simple to build and deploy a site to `GitHub` pages that uses the `Chirpy` theme. 

For your site to build correctly the first time you will need to make sure that `_config.yml` and `pages-deploy.yml` are correctly updated with your personal and repository-specific information. 

## Front Matter
Normally you won't find front matter in `Markdown` files as it isn't feature of the language by default. However, `Jekyll` will read `YAML` that it finds between two sets of `---` found at the top of a `Markdown` file

The front matter in the context of a post is read as a metadata of sorts for the post, and contains fields that influence how the post appears on the site. As well as the search function / sorting, such as `date` and `tags`. An example post front matter can be found below

```yaml
---
title: "Node.js, npm, nvm and npx Setup"
date: "2025-05-12"
# last_modified_at: "2025-05-12"
description: "Notes on installing and using node.js, npm, nvm and npx"
categories: [
  coding
]
tags: [
  webdev, javascript, html, css, node, node.js, npm, node package manager, node version manager, nvm, npx, node package execute
]
---
```

The `categories` field can be thought of as a sort of folder structure eg. `Web Development` / `JavaScript` would be two "folders" deep, this is separate from the `tags` field which doesn't create a connected structure in the same sense

## Repository Overview
There are a great deal of files and directories in this repository that serve important purposes or allow you to fine-tune certain things. But for my purposes, the only files and directories I am editing can be found below. My aim in the future is to build a similar site from the ground up, rather than attempt to "hack together" template code and my own code into a “Frankenstein’s monster” of a project.

### `.github/workflows/pages-deploy.yml`
This file defines a `GitHub Actions` "workflow" that builds the site and deploys it to `GitHub Pages`. It automates the process every time you push to the `main` branch, or any branch specified in `on/push/branches`. It specifies the environment for the virtual machine (`VM`) used for building and deploying and specifies a list of commands / processes to execute in order on the `VM`.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      ...
  deploy:
      ...
```

### `_config.yml`
This is the main configuration file for `Jekyll`. It sets global values used by the site and theme, such as the title, description, base URL, author info, and plugin settings. It’s required for your site to build properly.

### `_posts`
Contains all the `Mardown` files with [front matter](#front-matter). These will be read by [`Jekyll`](#jekyll) to build the site, and influence the search function.

### `_tabs`
Contains template `YAML` for the tabs that will appear on the left hand side of the page. Currently I feel it is best to leave them as they are. One exception is the tab `about.md` which is likely to contain site information in the same sort of format as can be found in this `README`.

## `assets`
You can add any files and folders into the `assets` directory, and reference them within your `Markdown` files. Files within the `assets` directory will be built into, and accessible from, your site.

## Progressive Web App (PWA)
By default the `pwa` option is enabled in `_config.yml`, this means that the built site is a `Progressive Web App` (`PWA`). In essence this makes the site closer to a native application when using a mobile device. It also gives the ability to "install" the app to your device for both mobile and desktop. 

Enabling `PWA` enables a `service worker` to handle caching, this means that the site can be used offline, and will use cached files to load the site faster. Due to the caching, the `service worker` runs in the background and checks for updates to its cached files. In the case of this site, it will prompt the user with a button to update site content when there is a commit pushed to the `main` branch.

## Generating a Favicon
You need a `favicon` of various sizes for different devices, one example is for the `Progressive Web App` (`PWA`).

Take a `512x512` image and go to [`Favicon Generator`](https://realfavicongenerator.net/), this will create a `.zip` file of all the images you will need. Extract this file and remove `browserconfig.xml` and `site.webmanifest` if they exist. Move the contents of this file to `assets/img/favicons`, create the directory if it doesn't exist. You don't need to make any changes to other files, such as `_config.yml`.

# Miscellaneous
- I have not really messed around with local build tools for this repository, but you can certainly set it up to build and test locally
- The `_scarletti` directory was added to the "exclude" section of `_config.yml` as a place for files that will not be built into the site
- In general, changes to files from the template are marked with `POSTIT` comments
- Due to the way that the pages are made, name clashes can exist as the date is omitted from the filename, eg. `1995-12-22-test.md` and `2025-12-22-test.md` both point to the same `URL` which is `markdown-blog/posts/test`
- The build process generates a `.json` file for use in the site's serach function, and you can view the raw file it generates [here](https://scarletti-ben.github.io/markdown-blog/assets/js/data/search.json)
- Adding a `description` field to the front matter of a post will stop it fromm automatically generating an excerpt from the first paragraph, so you can add if you want to manually control the description, or omit if you want it to generate automatically
- Remove the `author` section from front matter and it will use the site wide name as the author, specified in `_config.yml`
- You can use the field `last_modified_at` in the front matter of a post, otherwise it will be automatically generated from commit dates
- Added `.vscode/markdown.code-snippets` for project-specific snippets, such as a post template

# License
This work is published under the [MIT](https://github.com/scarletti-ben/markdown-blog/blob/main/LICENSE) license, the original license from `chirpy-starter` can be found [here](https://github.com/cotes2020/chirpy-starter/blob/master/LICENSE).

# Repository Metadata
```yml
---
title: "Markdown Blog README"
date: "2025-06-22"
categories: [
  repository
]
tags: [
  repository, readme, markdown, html, github, github pages, jekyll, front matter, metadata, chirpy, ruby, gem, gemfile, _config.yml, pages-deploy.yml, .yml, yaml, favicon, icon, snippets, .vscode, progressive web app, pwa, service worker, offline cache, caching, cache, template, use this template
]
---
```