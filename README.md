# 🏗️ Static Site Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-lightgrey)
![Type](https://img.shields.io/badge/Type-Static%20Site%20Generator-purple)
![Input](https://img.shields.io/badge/Input-Markdown-yellow)
![Output](https://img.shields.io/badge/Output-HTML-yellow)
![Status](https://img.shields.io/badge/Status-Complete-success)

This project is a minimal static site generator written in `Python`.

It reads `Markdown` files from a content directory, converts them into `HTML`, injects them into a template, and generates a complete static website ready to be deployed.

The generated site is deployed using GitHub Pages.

## What it does

When the generator runs, it:

1. Copies static assets (`CSS`, images) into the build directory
2. Crawls the entire content directory recursively
3. Converts `Markdown` files into `HTML`
4. Injects the generated `HTML` into a template
5. Writes the final pages to the output directory
6. Produces a complete static website

All pages preserve the same directory structure as the content folder.

## How it works (high level)

The generator follows a typical static-site pipeline:

```
Markdown content
        ↓
Markdown parser
        ↓
HTML node tree
        ↓
Template injection
        ↓
Generated static website
```

The system recursively walks the content directory and generates a corresponding `.html` file for every `.md` file found.

## Requirements

- Python 3.x
- A Unix-like shell (bash, zsh, etc.)

No external dependencies are required.

## Setup

Clone the repository

```shell
git clone https://github.com/nicoPuegher/static-site-generator.git
cd static-site-generator
```

Run the generator locally

```shell
python3 src/main.py
```

This builds the site into the `docs/` directory.

## Running the local server

```shell
cd docs
python3 -m http.server 8888
```

Then open

```shell
http://localhost:8888
```

## Building for GitHub Pages

The repository includes a build script used for deployment.

```shell
./build.sh
```

This builds the site with the correct base path for GitHub Pages.

Internally the script runs:

```shell
python3 src/main.py "/static-site-generator/"
```

## Project structure

```graphql
.
├── src/
│   └── main.py                # Static site generator logic
│
├── content/                   # Markdown pages
│   ├── index.md
│   ├── blog/
│   │   ├── glorfindel/
│   │   │   └── index.md
│   │   ├── tom/
│   │   │   └── index.md
│   │   └── majesty/
│   │       └── index.md
│   └── contact/
│       └── index.md
│
├── static/                    # Static assets copied to output
│   ├── index.css
│   └── images/
│
├── docs/                      # Generated site (GitHub Pages root)
│
├── template.html              # HTML template
├── build.sh                   # Production build script
└── README.md
```

## Example generated pages

After building the site, pages will exist like:

```
/index.html
/blog/glorfindel/index.html
/blog/tom/index.html
/blog/majesty/index.html
/contact/index.html
```

These are served directly as static `HTML` files.

## Notes

- This project intentionally avoids external libraries
- The `Markdown` parser and `HTML` node system are implemented manually
- Designed primarily as a learning exercise for parsing and build pipelines
- Not intended to replace full-featured static site generators
