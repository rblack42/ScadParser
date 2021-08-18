from mmdesigner.cli import pass_environment
from mmdesigner.Generator import Generator

import click


@click.command("excel", short_help="Generate Excel spreadsheet for current model.")
@pass_environment
def cli(ctx):
    """Shows file changes in the current working directory."""
    click.echo("Generating spreadsheet...")
    gen = Generator(ctx.model_path)
    gen.gen_excel(ctx.model_name)
