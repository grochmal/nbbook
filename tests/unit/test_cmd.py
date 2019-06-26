#!/usr/bin/env python

import logging
import pytest
from click.testing import CliRunner
from nbbook import cmd, LOG


def test_log_quiet():
    runner = CliRunner()
    result = runner.invoke(cmd.cli, ['html', '--help'])
    print(result.output)  # allow pytest to capture stdout
    assert logging.WARNING == LOG.getEffectiveLevel()


def test_log_verbose():
    runner = CliRunner()
    result = runner.invoke(cmd.cli, ['-v', 'html', '--help'])
    print(result.output)  # allow pytest to capture stdout
    assert logging.INFO == LOG.getEffectiveLevel()


def test_log_debug():
    runner = CliRunner()
    result = runner.invoke(cmd.cli, ['-vv', 'html', '--help'])
    print(result.output)  # allow pytest to capture stdout
    assert logging.DEBUG == LOG.getEffectiveLevel()


def test_log_over():
    runner = CliRunner()
    result = runner.invoke(cmd.cli, ['-vvv', 'html', '--help'])
    print(result.output)  # allow pytest to capture stdout
    assert logging.DEBUG == LOG.getEffectiveLevel()


def test_log_params(tmp_path):
    config_path = tmp_path / 'c.yaml'
    config_path.touch()
    runner = CliRunner()
    result = runner.invoke(cmd.cli,
        ['-vn', '-c', config_path,
         'latex', '--help', '--doctype'
         r'\documentclass[11pt,a4paper,oneside,draft]{report}'])
    print(result.output)  # allow pytest to capture stdout
    assert logging.INFO == LOG.getEffectiveLevel()

