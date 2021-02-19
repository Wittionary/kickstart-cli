import click
import requests

@click.command()
def hello():
    r = requests.get("http://localhost:5000/hello")
    click.echo(r.content)

@click.group()
def cli():
    pass

@click.command()
def initdb():
    
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(hello)

if __name__ == '__main__':
    cli()