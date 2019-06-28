#!/usr/bin/env python

import sys
import os
import logging
from collections import defaultdict
import click
import yaml
from . import LOG, LOG_LEVELS
from .util import parse_config, parse_defs
from .export import HTMLExporter, LaTeXExporter, BadUsage


@click.group()
@click.option('-v', '--verbose', count=True,
              help='Be more verbose, up to -vv.')
@click.option('-n', '--dry-run', is_flag=True,
              help='Do not write out anything, just report what will be done.')
@click.option('-s', '--single', is_flag=True,
              help='Export only a single notebook, instead of a full book.')
@click.option('-c', '--config', type=click.File('r'),
              help='Static configuration for every notebook export.')
@click.option('-o', '--output', type=click.File('w'),
              help='Output file for single exports.')
@click.option('-r', '--root',
              type=click.Path(file_okay=False, dir_okay=True, writable=True),
              help='Output directory for a complete book export.')
@click.pass_context
def cli(ctx, verbose, dry_run, single, config, output, root):
    click.echo(LOG)
    LOG.setLevel(LOG_LEVELS[verbose])
    click.echo(LOG)
    ctx.ensure_object(dict)
    cwd = os.getcwd()
    ctx.obj['CWD'] = cwd
    ctx.obj['VERBOSE'] = verbose
    ctx.obj['DRY_RUN'] = dry_run
    ctx.obj['SINGLE'] = single
    ctx.obj['CONFIG'] = parse_config(config)
    ctx.obj['OUTPUT'] = output
    ctx.obj['ROOT'] = root
    LOG.info(f'Publish WD: {cwd}')


@cli.command()
@click.option('--doctype', type=str,
              help='Overwrite LateX doc class, must be a full doctype string')
@click.argument('nbinput', type=click.File('r'))
@click.pass_context
def latex(ctx, doctype, nbinput):
    """
    Exports a LateX article or full book.
    """
    kw = dict(
        cwd=ctx.obj['CWD'],
        dry_run=ctx.obj['DRY_RUN'],
        single=ctx.obj['SINGLE'],
        config=ctx.obj['CONFIG'],
        output=ctx.obj['OUTPUT'],
        root=ctx.obj['ROOT'],
        doctype=doctype,
        nbinput=nbinput,
    )
    try:
        exporter = LaTeXExporter(**kw)
    except BadUsage as e:
        raise click.UsageError(str(e))
    exporter.read_nbs()
    exporter.build_output()


@cli.command()
@click.option('--imgfmt', default='b64',
              help='Attachment image format, either `b64` or `href`')
@click.option('--mathjax', type=str,
              help='Path to MathJax, default is to use a CDN instead.')
@click.option('--extrastyle', type=str,
              help='Path to extra CSS to be included in the pages.')
@click.option('--title', type=str,
              help='Title for single notebook export.')
@click.option('--baseurl', type=str,
              help='If not root, the URL on which the book will live.')
@click.option('--section', multiple=True, type=str,
              help='Generate this section(s) of the book (default: all).')
@click.argument('nbinput', type=click.File('r'))
@click.pass_context
def html(ctx, imgfmt, mathjax, extrastyle, title, baseurl, section, nbinput):
    """
    Exports complete HTML, including attachments.
    """
    kw = dict(
        cwd=ctx.obj['CWD'],
        dry_run=ctx.obj['DRY_RUN'],
        single=ctx.obj['SINGLE'],
        config=ctx.obj['CONFIG'],
        output=ctx.obj['OUTPUT'],
        root=ctx.obj['ROOT'],
        imgfmt=imgfmt,
        mathjax=mathjax,
        extrastyle=extrastyle,
        title=title,
        baseurl=baseurl,
        section=section,
        nbinput=nbinput,
    )
    try:
        exporter = HTMLExporter(**kw)
    except BadUsage as e:
        raise click.UsageError(str(e))
    exporter.read_nbs()
    exporter.build_output()


if '__main__' == __name__:
    cli(obj={})

