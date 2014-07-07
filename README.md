EdgePI Developer's Blog
=======================

Save22's EdgePI development blog

## Setting up

Have your account registered as contributor to this repo or fork it.

Clone the repo and install everything in `requirements.pip` inside a virtualenv.

## Writing new content

Create a file in this format under the `content` directory:

    my-awesome-article-slug.md

Once your done writing your article, run `build.py`, commit your changes and push.

## Article boilerplate

This is what your article should contain:

    Title: My Awesome Article 
    Date: 2013-05-25 18:00
    Category: code
    Tags: pelican, python
    Slug: my-awesome-article-slug 
    Author: @cr8ivecodesmith 
    
    Hello world!
    
    Here's some codeblock:

    ~~~~~
    codeblock_goes_here = True
    ~~~~~


