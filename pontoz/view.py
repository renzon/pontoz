from os import path

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

_templates_path = path.dirname(__file__)
_templates_path = path.join(_templates_path, 'templates')

_env = Environment(loader=FileSystemLoader(_templates_path))


def render(template, context=None):
    if context is None:
        context = {}
    return _env.get_template(template).render(context)
