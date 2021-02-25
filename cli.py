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
def ls(): # list scripts
    click.echo('List scripts')
    r = requests.get("http://localhost:5000/api/v1/resources/scripts/all")
    click.echo(r.content)

@click.command()
def run(): # run script; needs to take an argument of script id or script name
    click.echo('Run script')

cli.add_command(ls)
cli.add_command(run)
cli.add_command(hello)

if __name__ == '__main__':
    cli()