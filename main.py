#! /usr/bin/env python
"""
This priceless tool that is invaluable to the world of programming, fetches Star Wars characters from the SWAPI.
In details:
- fetch SWAPI characters
- sort them by number of films they appear in
- get first 10 characters
- sort them by height
- save in CSV file
- send CSV file to httbin.org

Awesome, right?
"""
import click

from controllers import swapi


@click.group()
def cli():
    """Awesome group of commands"""
    pass


@click.command()
def fetch_characters():
    """Fetch characters from the SWAPI"""
    swapi.fetch_characters()


@click.command()
def greet():
    """Dummy command to test the cli"""
    click.echo(
        'Welcome to the "first" useless CLI app, that will amaze you with its functionality!'
    )


cli.add_command(fetch_characters)
cli.add_command(greet)
if __name__ == "__main__":
    cli()
