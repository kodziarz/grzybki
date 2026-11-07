import click

from . import __version__


@click.group()
@click.version_option(__version__, prog_name="grzybki")
def main() -> None:
    pass


@main.command()
@click.argument("instance", type=click.Path(exists=True, dir_okay=False))
@click.option("--out", "out_dir", type=click.Path(file_okay=False), default=None)
def optimize(instance: str, out_dir: str | None) -> None:
    from .commands import run_optimize

    run_optimize(instance, out_dir)


@main.command()
@click.argument("run_dir", type=click.Path(exists=True, file_okay=False))
@click.option("--out", "out_dir", type=click.Path(file_okay=False), default=None)
def visualize(run_dir: str, out_dir: str | None) -> None:
    from .commands import run_visualize

    run_visualize(run_dir, out_dir)
