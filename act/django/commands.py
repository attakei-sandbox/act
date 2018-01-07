# -*- coding:utf-8 -*-
import logging
from datetime import datetime
from pathlib import Path
import click
from jinja2 import Environment, PackageLoader, Template
from ..cli import act
"""Django source generating
"""


Logger = logging.getLogger(__name__)

JINJA2_ENV = Environment(
    loader=PackageLoader(__name__),
)
JINJA2_ENV.globals['proc_date'] = datetime.now()


@act.group()
def django():
    """Handle django project
    """
    pass


@django.command()
@click.argument('name')
@click.option(
    '--dest', '-d', default='.',
    type=click.Path(file_okay=False, exists=True))
def create_command(name: str, dest: str):
    """Create sources of custom command
    """
    # Generate dependency files and directories
    dest = Path(dest)
    (dest / 'management').mkdir(parents=True, exist_ok=True)
    (dest / 'management/__init__.py').touch(exist_ok=True)
    (dest / 'management/commands').mkdir(parents=True, exist_ok=True)
    (dest / 'management/commands/__init__.py').touch(exist_ok=True)
    template: Template = JINJA2_ENV.get_template('command.py.j2')
    template.stream().dump(str(dest / f"management/commands/{name}.py"))
