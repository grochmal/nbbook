#!/usr/bin/env python

import pytest
from nbbook import util


def test_parse_config():
    good_yaml = """extrastyle: /mystyle.css
mathjax: /MathJax-2.7.5/MathJax.js?config=TeX-AMS_HTML
    """
    config = util.parse_config(good_yaml)
    assert 'mathjax' in config
    assert 'extrastyle' in config


def test_parse_config_empty():
    empty_yaml = ''
    config = util.parse_config(empty_yaml)
    assert {} == config
    empty_yaml = None
    config = util.parse_config(empty_yaml)
    assert {} == config


def test_parse_config_random():
    random_yaml = """planet: jupiter
satelite: ganymede
    """
    config = util.parse_config(random_yaml)
    assert {} == config


def test_parse_config_list():
    bad_yaml = """- jupiter
- earth
- mars
    """
    with pytest.raises(util.NotConfig):
        config = util.parse_config(bad_yaml)

