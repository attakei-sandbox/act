# -*- coding:utf-8 -*-
from pathlib import Path
from urllib.request import urlopen
import logging
import subprocess
import click


Logger = logging.getLogger(__name__)


@click.group()
def act():
    pass


@act.command()
@click.argument('ignore_types', nargs=-1)
def gitignore(ignore_types: tuple):
    """Get .gitignore output from gitignore.io
    """
    URL_BASE = 'https://www.gitignore.io/api'
    ignore_types = sorted(ignore_types)
    Logger.debug('Targets are %s', ignore_types)
    url = '{}/{}'.format(URL_BASE, ','.join(ignore_types))
    Logger.debug('Call URL is %s', url)
    resp = urlopen(url)
    click.echo(resp.read())


@act.command()
def upgrade():
    """Upgrade act
    """
    repo = Path(__file__).parent.parent
    # TODO: Not use subprocess (use Python lib)
    commands = [
        'git pull',
        'pip install -e .',
    ]
    for command in commands:
        proc = subprocess.Popen(
            command.split(), cwd=repo)
        proc.communicate()


def main():
    """Script endpoint
    """
    act()
