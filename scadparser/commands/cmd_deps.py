from scadparser import __version__
import click
from scadparser.cli import pass_environment



@click.command("deps", help="Display dependency versions.")
@pass_environment
def cli(ctx):
    """Display current dependency versions."""
    click.echo(f"scadparser: {__version__}")
