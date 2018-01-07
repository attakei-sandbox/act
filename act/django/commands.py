# -*- coding:utf-8 -*-
import logging
from datetime import datetime
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
def create_command(name: str):
    """Create sources of custom command
    """
    click.echo('Hello')
    template: Template = JINJA2_ENV.get_template('command.py.j2')
    template.stream().dump(f"{name}.py")
