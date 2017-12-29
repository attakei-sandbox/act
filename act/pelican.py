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
def init_article(style: str):
    article_date = date.today()
    output_dir: Path = Path.cwd()\
        .joinpath(BASIC_PATH, str(article_date.year))
    output_dir.mkdir(parents=True, exist_ok=True)
    template: Template = JINJA2_ENV.get_template(f"{style}.j2")
    article_path: Path = output_dir.joinpath('article.rst')
    template.stream(
        article_date=article_date.strftime('%Y-%m-%d'))\
        .dump(str(article_path))
    click.echo(f"Generated: {article_path}")
    return
