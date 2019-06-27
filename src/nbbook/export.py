#!/usr/bin/env python

import os
import nbformat
import nbconvert
from . import LOG


class Exporter(object):

    def __init__(self, **kw):
        """
        Parse the command line and figure out what we are exporting.

        Whether we are exporting a full book or just a single or a handful
        of notebooks.  We also update the configuration from the already
        read configuration file.

        This only performs the validation that the input looks correct,
        it does not attempt to check whether file-system entities
        are in the correct state.  Check `_validate_fs` below for
        the file-system checks.
        """
        pass

    def _validate_fs(self):
        pass

    def read_nbs(self):
        pass

    def build_output(self):
        pass


class HTMLExporter(Exporter):
    pass


class LaTeXExporter(Exporter):
    pass


    #if not htmlout:
    #    base, _ = os.path.splitext(os.path.basename(nbinput.name))
    #    htmlout = f'{base}.html'
    #htmlout = open(htmlout, 'w')
    #if ctx.obj['DEBUG']:
    #    if slides:
    #        click.echo(f'Export slides HTML: {nbinput.name} -> {htmlout.name}')
    #    else:
    #        click.echo(f'Export full HTML: {nbinput.name} -> {htmlout.name}')
    #nbops.html_export(nbinput, htmlout, imgfmt=imgfmt, slides=slides)


def html_export(nbin, htmlout, imgfmt='b64', slides=False):
    """
    Does a complete HTML export, including cell attachments.

    Function heavily inpired by the code in the github issue:
    https://github.com/jupyter/nbconvert/issues/699
    by Søren Fuglede Jørgensen and Donghyun Kwak.
    """
    contents = nbin.read()
    # first convert it the normal way
    notebook = nbformat.reads(contents, as_version=4)
    if slides:
        exporter = nbconvert.SlidesExporter()
    else:
        exporter = nbconvert.HTMLExporter()
    #exporter = Exp()
    exporter = nbconvert.HTMLExporter()
    #exporter.template_file = '/home/grochmal/programs/my/daml/basic.tpl'
    exporter.template_file = '/home/grochmal/programs/my/daml/bookhtml.tpl'
    print('PATH', Exp.default_template_path)
    resources = {
        'title': 'NB Title',
        #'mathjax': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML'
        'mathjax': 'MathJax-2.7.5/MathJax.js?config=TeX-AMS_HTML',
        'main_style': 'bookhtml.css',
        'extra_style': None,
    }
    body, _ = exporter.from_notebook_node(notebook, resources=resources)
    # save a mapping of all attachments
    images = []
    for cell in notebook['cells']:
        if 'attachments' in cell:
            atts = cell['attachments']
            for filename, att in atts.items():
                for mime, base64 in att.items():
                    images.append({
                        'att_name': f'attachment:{filename}',
                        'name': f'{filename}',
                        'href': f'{filename}',
                        'b64': f'data:{mime};base64,{base64}',
                    })
    # fix the HTML by hand
    for i in images:
        att = i['att_name']
        data = i[imgfmt]
        body = body.replace(f'src="{att}"', f'src="{data}"', 1)
        short = data[:60]
        if len(data) > 60:
            short += '...'
        LOG.info(f'Image at: src="{short}"')
    LOG.info('%s %s' %  (dir(body), type(body)))
    LOG.info(body[:200])
    htmlout.write(body)

