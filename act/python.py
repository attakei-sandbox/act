# -*- coding:utf-8 -*-
from pathlib import Path
import logging
import click
from .cli import act
"""Python source generating
"""


Logger = logging.getLogger(__name__)


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
    dest: Path = Path(dest).absolute()
    Logger.debug('Target path is %s', dest)
    click.echo(f"Create source at {dest}")
    return
