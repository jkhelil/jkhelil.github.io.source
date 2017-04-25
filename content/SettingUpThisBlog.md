Title: Setting Up This Blog
Date: 2017-04-27 13:00
Tags: Blog
Category: Blog
Slug: setting-up
Author: Jawed khelil
Summary: Setting Up This Blog
This blog uses the static site generator [Pelican](http://www.getpelican.com) and is hosted on [Github](http://www.github.com). Here are a few notes on how I set things up.

Installing Pelican
------------------

    :::text
    mkdir pelican
    virtualenv .pelican
    source .pelican/bin/activate
    pip install pelican markdown
    deactivate
    mkdir jkhelil.github.io.source
    mkdir jkhelil.github.io

Creating The Blog
-------------------

    :::text
    cd jkhelil.github.io.source
    pelican-quickstart

The default answers to the questions are usually reasonable, but season to taste.

I edited the `pelicanconf.py` and changed the `OUTPUTPATH` variable to point to `jkhelil.github.io`:

    :::text
    OUTPUT_PATH = '../jkhelil.github.io'

Then add a post in the `content` directory at `jkhelil.github.io.source\content`. A simple Markdown post should work:

    :::text
    Title: First Post
    Date: 2017-4-27 15:00
    Tags: Blog
    Category: Blog
    Slug: first-post
    Author: Jawed Khelil
    Summary: First Post
    It's so easy when everybody's trying to please me, baby

We should be able to generate the blog now. Try this:

    :::text
    make html
    make serve

Browse to `127.0.0.1:8000` and, hey, it works!

Live Editing
------------

In one shell, run `make regenerate`. This automatically regenerates the `jkhelil.github.io` directory whenever you change a file in the `source` directory. In another shell, run the local web server `make serve`. Now you can change any file, refresh your browser, and immediately see your changes.

The command `make devserver` will also do that, but it calls a Bash script, which doesn't work on Windows.

Pelican Themes
--------------

The default Pelican theme isn't spectacular. You can get additional themes by cloning the Pelican theme repository:

    :::text
    cd pelican
    git clone https://github.com/getpelican/pelican-themes themes

You'll find all the themes in the new `themes` directory. To choose one, set the `THEME` variable in `pelicanconf.py`:

    :::text
    THEME = 'themes/pelican-bootstrap3'

I like the Pelican-Bootstrap3 theme. It has a `README.md` that you'll want to read. The Bootstrap theme is actually themed itself with [Bootswatch](http://bootswatch.com/). You can also easily customize the CSS and set the syntax highlighting style. Here's the relevant bits in my `pelicanconf.py`:

    :::text
    BOOTSTRAP_THEME = 'cyborg'        # Bootswatch sub-theme for Bootstrap
    PYGMENTS_STYLE = 'monokai'        # Syntax highlighting theme
    CUSTOM_CSS = 'static\custom.css'
    STATIC_PATHS=['images','extra\custom.css']
    EXTRA_PATH_METADATA = {'extra\custom.css': {'path': 'static\custom.css'}}

Github Pages Hosting
--------------------

I'm using [Github Pages](https://pages.github.com/) to host this blog. I created two repositories. One is named `jkhelil.github.io` and holds the blog site, and the other is named `jkhelil.github.io.source` and holds the Pelican source for the blog.


    :::text
    cd jkhelil.github.io
    git init
    git add -A .
    git commit -m "initial commit"
    git remote add origin https://github.com/jkhelil/jkhelil.github.io.git
    git push -u origin master
    cd jkhelil.github.io.source
    git init
    git add -A .
    git commit -m "initial commit"
    git remote add origin https://github.com/jkhelil/jkhelil.github.io.source.git
    git push -u origin master

A few minutes later, the blog appears at [jkhelil.github.io](http://jkhelil.github.io). 
