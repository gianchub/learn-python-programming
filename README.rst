=========================================
Learning Python Programming - Source Code
=========================================

This project holds the source code for the book:

**Learn Python Programming, 2nd Edition - Packt Publishing**

Author: **Fabrizio Romano**

ISBN: **9781788996662**

Publication date: **June 2018**


Setup
=====

Create a virtual environment with a Python version 3.7.*.


Installing requirements
-----------------------

Install all the requirements text files via pip like this:

    $ pip install -r requirements.txt

Requirements for the data science chapter can be cumbersome to install
so I kept them separated, in the `requirements.data.science.txt` file.

If you wish to install all requirements at once, just execute the following:

    $ pip install -r all.txt


Updating requirements
---------------------

To update requirements you can use `pip-tools` to compile the `*.in`
sources in the `requirements` folder.

To compile and update a single `.in` file, run the following:

    $ pip-compile -U requirements.in

If you want to compile all requirements into one single `.txt` file,
run the following:

    $ pip-compile -U -o all.txt *.in

This will read all the `.in` files and compile them together into the
`all.txt` file.


Python Version
==============

Python 3.7


Last update
-----------

2018.06.29


Note on Pull Requests
=====================

Due to this code being tied to a published book, any PRs will be
ignored.
