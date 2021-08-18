from mmdesigner.cli import pass_environment
import sys
import click
from mmdesigner.Generator import Generator

@click.command("status", short_help="Shows summary of current model.")
@pass_environment
def cli(ctx):
    """Shows status of model in the current working directory."""
    gen = Generator(ctx.model_path)
    gen.inventory()
    click.echo("Design summary:")
    click.echo(f"\tCurrent working directory: {ctx.cwd}")
    click.echo(f"\tmodel_path: {ctx.model_path}")
    click.echo(f"\tmodel_name: {ctx.model_name}")
    click.echo(f"\tPart count: {ctx.part_count}")
    click.echo(f"\tAssembly count: {ctx.assembly_count}")
    click.echo(f"\tDebug: {ctx.debug}")
    sys.exit(0)
