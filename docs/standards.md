# standards #

Project and python specific standards that have been chosen and not otherwise
explicitly recommended.

## project layout ##

This project loosely follows the conventions established by the most popular
open source project for bootstrapping a new django project, to provide a
reasonable layout and structure.

See [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) for
reference.  

## best practices ##

Where possible, follow established best practices.  See:

  1. [django-best-practices](https://wsvincent.com/django-best-practices/)

## test-driven software development ##

Generally use [Robert Martin's](https://en.wikipedia.org/wiki/Robert_C._Martin) [three laws of TDD](https://www.youtube.com/watch?v=qkblc5WRn-U):

  1. Only write enough of a unit test to fail.
  2. Only write production code to make a failing unit test pass.

## dependencies ##

Where possible, minimize the number of package dependencies used to get the job
done.  If it's a complex task and someone else has an appropriately licensed
solution which is carefully maintained and largely established, then it's
a good idea.  

Example dependencies that are used:

  1. [django-localflavor](https://github.com/django/django-localflavor) which
     provides our model a USPostalCodeField

## SOLID KISS ##

Use [SOLID](https://en.wikipedia.org/wiki/SOLID) design principles and [keep it stupid simple](https://en.wikipedia.org/wiki/KISS_principle).

## 12Factor ##

Generally heroku's [The Twelve-Factor App](https://12factor.net/) guide should
be followed.
