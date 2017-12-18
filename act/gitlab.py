# -*- coding:utf-8 -*-
from pathlib import Path
import logging
import click
from .cli import act, ROOT


Logger = logging.getLogger(__name__)


@act.command('gitlab-ci-init')
@click.argument('lang')
def init_yml(lang: str):
    cur_dir = Path.cwd()
    cur_yml = cur_dir / '.gitlab-ci.yml'
    if cur_yml.exists():
        click.echo('.gitlab-ci.yml is already exists.')
        return
    # TODO: generate by module
    src = ROOT / 'files' / 'gitlab' / f"gitlab-ci.{lang}.yml"
    content = src.read_text()
    cur_yml.write_text(content)
    click.echo('Generated!')
    return
