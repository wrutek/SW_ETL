#! /usr/bin/env python

import click


@click.group()
def cli():
    pass


@click.command()
def fetch_characters():
    pass


@click.command()
def greet():
    click.echo(
        'Welcome to the "first" useless CLI app, that will amaze you with its functionality!'
    )


if __name__ == "__main__":
    cli.add_command(fetch_characters)
    cli.add_command(greet)
    cli()
