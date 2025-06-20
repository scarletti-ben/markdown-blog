
# A Note on this Directory
The `_scarletti` directory from this repository was added to the "exclude" section of `_config.yml`. This is not really required as `Jekyll` should ignore it by default when building the site for `GitHub` pages, but I thought I might as well add it.

```yaml
exclude:
  - ...
  - _scarletti/
```

# PWA
Enabling `PWA` also enables the "site content changed, update site" thing as the service worker checks file changes

Update the About

# Categories
Categories are folders, eg. Web Development / JavaScript is two folders deep, not in both categores - citation needed


# htmlproofer
`_pages-deploy.yaml`
```yaml
# POSTIT - Here htmlproofer is used to check if internal links are valid
# Currently disabled
# - name: Test site
#   run: |
#     bundle exec htmlproofer _site \
#       \-\-disable-external \
#       \-\-ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"
```

# Name Clashes
Due to the way that the pages are made, name clashes can exist as the date is omitted from the filename, eg. `1995-12-22-test.md` and `2025-12-22-test.md` both point to the same `URL` which is `markdown-blog/posts/test`

# ...
Take a `512x512` image and go to [`Favicon Generator`](https://realfavicongenerator.net/), this will create a `.zip` file of all the images you will need. Extract this file and remove `browserconfig.xml` and `site.webmanifest` if they exist. Move the contents of this file to `assets/img/favicons`, create the directory if it doesn't exist. You don't need to make any changes to other files, such as `_config.yml`.

# Miscellaneous
- Adding a description to the yaml will stop it showing an excerpt, so you can add if you want to manually control the description, but can also omit if you want
- Mention the `PWA` service worker
- Remove the `author` section from front matter and it will use the site wide name, otherwise