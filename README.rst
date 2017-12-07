What's This?
============
Pycgettb is convert guided form excel files to text data. No special programming is required.

First, prepare the same xlsx format of the data and the template, to define the text data using the jinja2-based template.

This command/library is currently alpha version
===============================================

Recommended to use it in virtual environment.

Dependencies
============

- Python 3.6, 2.7(Development by 3.6)
- `openpyxl <https://openpyxl.readthedocs.io/en/default/>`_
- `Jinja2 <http://jinja.pocoo.org/docs/2.9/>`_
- `Click <http://click.pocoo.org/5/>`_

Install
=======

Using pip
---------

::

    # Example, Using Python3 venv module.
    $ python3 -m venv env
    $ source env/bin/activate
    (env)$ pip install pycgettb

Using by Github
---------------

::

    $ git clone https://github.com/hrsano645/pycgettb.git
    $ cd pycgettb

    # Example, Using Python3 venv module.
    $ python3 -m venv env
    $ source env/bin/activate

    (env)$ pip install -r requirements.txt

Command Usage
=============

::

    (env)$ pycgettbcli --help
    Usage: pycgettbcli [OPTIONS] SRC_TEMPLATE SRC_DATA EXPORT_TEMPLATE

    Options:
      --export_filename TEXT  Set export filename
      --help                  Show this message and exit.


- `--export_filename`: If not specified, create a file named `exported_data.txt`.

How To Use
==========

When using pycgettb, prepare three files. The sample file is `./tests/testfiles/`.

Source Data: An xlsx file containing the data.

.. image:: https://github.com/hrsano645/pycgettb/blob/master/docs/img/example_data_img.png?raw=true
    :alt: source data file image

Source Template: An xlsx file with embedded template variables. Make the same worksheet and cell layout of the source data file.

.. image:: https://github.com/hrsano645/pycgettb/blob/master/docs/img/example_template_img.png?raw=true
    :alt:  source template file image

Export Template: The jinja2 template file (html, json, csv, etc...)

※:The jinja2 template currently supports variables only.

::

    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
    </head>
    <body>

    <h1>{{ title }}</h1>

    <table>
        <tr>
            <td>date</td>
            <td>name</td>
            <td>note</td>
        </tr>
        <tr>
            <td>{{ date_1 }}</td>
            <td>{{ name_1 }}</td>
            <td>{{ note_1 }}</td>
        </tr>
        <tr>
            <td>{{ date_2 }}</td>
            <td>{{ name_2 }}</td>
            <td>{{ note_2 }}</td>
        </tr>
    </table>
    </body>
    </html>

Template files(source template, export template) must be the same template variable name. Based on that convert to text data using jinja2.

::

    (env)$ pycgettbcli ./tests/testfiles/template.xlsx ./tests/testfiles/data.xlsx ./tests/testfiles/export_template.html

Converted result. Default file name is exported_data.txt

::

    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>Example Title</title>
    </head>
    <body>

    <h1>Example Title</h1>

    <table>
        <tr>
            <td>date</td>
            <td>name</td>
            <td>note</td>
        </tr>
        <tr>
            <td>2017-01-01 00:00:00</td>
            <td>suzuki</td>
            <td>日本語テスト</td>
        </tr>
        <tr>
            <td>2017-01-02 00:00:00</td>
            <td>sato</td>
            <td>None</td>
        </tr>
    </table>
    </body>
    </html>

Using as a Library
==================

pycgettb can also be used as a library.

::

    from pycgettb import Source
    from pycgettb import TextRender

    # set file path
    src_template = "[source template file path]"
    src_data = "[source data file path]"
    export_template = "[export template file path]"

    # define export filename
    export_filename = "exported_file.txt"

    source = Source(src_template, src_data)
    source_data_map = source.parse()

    textrender = TextRender(export_template, source_data_map)

    # write rendreing textdata
    with open(export_filename, "w") as export_file:
        export_file.write(textrender.render())

Future Work
===========

- Building a command binary for Windows, macOS, Linux.
- Add list type to source template variable
- GUI Frontend
- API Document

License
=======

MIT License

