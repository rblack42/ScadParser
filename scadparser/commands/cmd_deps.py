from mmdesigner import __version__
from mmdesigner.OpenSCAD import OpenSCAD
from stl import __about__
import click

@click.command("deps", help="Display dependency versions.")
def cli():
    """Display current dependency versions."""
    osc = OpenSCAD()
    osc_version = osc.get_version()
    click.echo(f"mmd: {__version__}")
    click.echo(f"OpenSCAD: {osc_version}")
    click.echo(f"numpy-stl: {__about__.__version__}")
