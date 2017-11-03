from os import path

import pytest


@pytest.fixture(scope='module')
def dre_content():
    curr_dir = path.dirname(__file__)
    project_dir = path.join(curr_dir, '..', '..')
    project_dir = path.abspath(project_dir)
    dre_file_path = path.join(project_dir, 'contrib', 'dre-sample.html')
    dre_file = open(dre_file_path, 'r')
    return '\n'.join(dre_file.readlines())


def test_dre_title(dre_content):
    assert 'Posto Flex' in dre_content
