# -*- coding:utf-8 -*-
from pathlib import Path
from datetime import datetime
import logging
import click
from jinja2 import Environment, FileSystemLoader
from .cli import act, ROOT
"""Python source generating
"""


Logger = logging.getLogger(__name__)

JINJA2_ENV = Environment(
    loader=FileSystemLoader(str(ROOT.joinpath('files', 'python'))),
)


@act.group()
def python():
    """Grouping sub commands in this module
    """
    pass


@python.command()
@click.argument('dest', type=click.Path())
def short(dest):
    """Generate source as short script
    """
    dest = Path(dest).absolute()  # type: Path
    if dest.suffix != 'py':
        Logger.debug('File extension is added automate')
        dest = dest.with_suffix('.py')
    Logger.debug('Target path is %s', dest)
    now = datetime.now()
    template = JINJA2_ENV.get_template('script.py.j2')  # type: jinja2.Template
    template.stream(dest=dest, now=now).dump(str(dest))
    click.echo(f"Create source at {dest}")
    return
