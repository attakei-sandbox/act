# -*- coding:utf-8 -*-
from pathlib import Path
from datetime import date
import logging
import click
from jinja2 import Environment, FileSystemLoader, Template
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
    output_dir: Path = Path.cwd()\
        .joinpath(BASIC_PATH, str(article_date.year))
    output_dir.mkdir(parents=True, exist_ok=True)
    template: Template = JINJA2_ENV.get_template(f"{style}.j2")
    article_path: Path = output_dir.joinpath('article.rst')
    template.stream(
        article_date=article_date.strftime('%Y-%m-%d'),
        title=title, category=category)\
        .dump(str(article_path))
    click.echo(f"Generated: {article_path}")
    return


def rst_section(input: str):
    """Pretty simple reST section string
    """
    return '=' * len(input) * 2


JINJA2_ENV.filters['rst_section'] = rst_section
