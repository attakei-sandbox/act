# -*- coding:utf-8 -*-
from urllib.request import urlopen
import logging
import click


Logger = logging.getLogger(__name__)


@click.group()
def act():
    pass


@act.command()
@click.argument('ignore_types', nargs=-1)
def gitignore(ignore_types: tuple):
    URL_BASE = 'https://www.gitignore.io/api'
    ignore_types = sorted(ignore_types)
    Logger.debug('Targets are %s', ignore_types)
    url = '{}/{}'.format(URL_BASE, ','.join(ignore_types))
    Logger.debug('Call URL is %s', url)
    resp = urlopen(url)
    click.echo(resp.read())


def main():
    """Script endpoint
    """
    act()
