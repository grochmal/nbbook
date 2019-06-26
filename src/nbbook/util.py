#!/usr/bin/env python

import yaml


KNOWN_CONFIGS = (
    'imgfmt',
    'mathjax',
    'extrastyle',
    'baseurl',
    'doctype',
)


class NotConfig(RuntimeError):
    pass


def parse_config(config):
    if not config:
        return {}
    contents = yaml.safe_load(config)
    if contents and not isinstance(contents, dict):
        raise NotConfig('Config must be a YAML dictionary')
    config = {}
    for k in contents:
        if k in KNOWN_CONFIGS:
            config[k] = contents[k]
    return config


class Section(object):
    pass


def parse_defs(cwd, definput):
    pass

