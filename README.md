# Statement

1. Creating scripts for filling an existing database:

    1.1. *data/movies.json* contains movies descriptions: cast, genre and release year.
These scripts do not have to be a part of the application, they do not have to
accept the file by endpoint, just simple external scripts which will run once during
the presentation.<br/>
    1.2. The file must be parsed, the data must be placed in the database. The data model
has already been declared, the database has been created, the migration carried
out. Please, use all of that in your work.<br/>
    1.3. For extra credit, you can come up with a process to remove invalid cast members
names from the dataset in scripts. *– Optional*

2. Creating an API:

    2.1. The user should be able to create/edit/delete a movie. Creation and editing should
be executed by selection actors and genres from the existing ones in the database.<br/>
    2.2. The user should be able to get a list of actors aggregated by the years of release
of the films in which he starred, with the number of films released this year.

    Example:

    * Ashton Kutcher, 2006, 2
    * Ashton Kutcher, 2007, 1
    * Gary Sinise, 2005, 3
    * Gary Sinise, 2006, 4

Here are a few notes:
1. The service should be written in Flask, each request and response should be validate
by Marshmallow.
2. Write a lot of comments with an explanation of what you did and what you intended
to achieve.
3. Run your project and see that it works before submitting it.
4. Submit the project with readme file (markdown) containing anything that you want
me to read regarding the project (things that you weren't sure about, packages that
you used) – Optional


# Disclaimer

It using flask 1.1.2 as a task restriction.


# Installation

$ docker-compose up


# Usage
