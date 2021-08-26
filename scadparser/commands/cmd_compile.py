import click
import os

from scadparser.cli import pass_environment
from scadparser.ScadParser import ScadParser


@click.command("compile", help="Process input scad file.")
@click.argument('filename', nargs=1)
@pass_environment
def cli(ctx, filename):
    """Parse input scad file."""
    click.echo(f"scadparser: compiling {filename}")
    parser = ScadParser()
    cwd = os.getcwd()
    click.echo(f"CWD: {cwd}")
    fn = os.path.abspath(os.path.join(cwd, filename))
    click.echo(f"FN: {fn}")
    text = open(fn).read()
    parser.parse(text)
