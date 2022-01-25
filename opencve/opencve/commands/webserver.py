import os

import click
from flask.cli import with_appcontext

from opencve.commands import ensure_config


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
@ensure_config
@with_appcontext
def webserver(args):
    """Run the webserver."""
    # TODO : Find a better way of handling timeouts so that xlsx files can be imported correctly
    # Maybe search for threading with a waiting logo ?
    args = ["gunicorn"] + list(args) + ["-t", "1000"]
    args.append("opencve.app:app")
    os.execvp(args[0], args)
