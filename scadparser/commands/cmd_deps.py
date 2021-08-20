from scadparser import __version__
import click


@click.command("deps", help="Display dependency versions.")
def cli():
    """Display current dependency versions."""
    click.echo(f"scadparser: {__version__}")
