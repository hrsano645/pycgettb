# coding=utf-8
from __future__ import (division,
                        absolute_import,
                        print_function,
                        unicode_literals)

from pycgettb import Source
from pycgettb import TextRender

import click

@click.command()
@click.argument('src_template', nargs=1, type=click.Path(exists=True))
@click.argument('src_data', nargs=1, type=click.Path(exists=True))
@click.argument('export_template', nargs=1, type=click.Path(exists=True))
@click.option('--export_filename', default="exported_data.txt", help="Set export filename")
def cmd(src_template, src_data, export_template, export_filename):
    source = Source(src_template, src_data)
    data_map = source.parse()
    textrender = TextRender(export_template, data_map)

    with open(export_filename, "w") as export_file:
        export_file.write(textrender.render())

def main():
    cmd()

if __name__ == "__main__":
    main()
