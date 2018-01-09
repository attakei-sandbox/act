# -*- coding:utf-8 -*-
from pathlib import Path
from datetime import date
import logging
import click
from jinja2 import Environment, FileSystemLoader
from git import Repo
from .cli import act, ROOT


Logger = logging.getLogger(__name__)

BASIC_PATH = 'content'
JINJA2_ENV = Environment(
    loader=FileSystemLoader(str(ROOT.joinpath('files', 'pelican'))),
)


@act.command('pelican-new')
@click.option('--style', '-s', type=str, default='simple')
@click.option('--title', '-t', type=str, required=True)
@click.option('--category', '-c', type=str, default='Life')
def init_article(style: str, title: str, category: str):
    article_date = date.today()
    output_dir = Path.cwd()\
        .joinpath(BASIC_PATH, str(article_date.year))  # type: Path
    output_dir.mkdir(parents=True, exist_ok=True)
    template = JINJA2_ENV.get_template(f"{style}.j2")  # type: jinja2.Template
    article_path = output_dir.joinpath('article.rst')  # type: Path
    template.stream(
        article_date=article_date.strftime('%Y-%m-%d'),
        title=title, category=category)\
        .dump(str(article_path))
    click.echo(f"Generated: {article_path}")
    repo = Repo(str(Path.cwd()))  # type: Repo
    new_branch = repo.create_head(
        f"articles/{article_date.strftime('%Y%m%d')}", 'master')
    new_branch.checkout()
    return


def rst_section(input: str):
    """Pretty simple reST section string
    """
    return '=' * len(input) * 2


JINJA2_ENV.filters['rst_section'] = rst_section
