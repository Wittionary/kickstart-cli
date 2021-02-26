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
def ls():
    """
    This lists existing scripts in the repo/library.
    """
    click.echo('List scripts')
    r = requests.get("http://localhost:5000/api/v1/resources/scripts/all")
    click.echo(r.content)

@click.command()
@click.option('--name', help='Name of the script or *.exe')
@click.option('--id', help='Id of the script')
def run(name, id):
    """
    This runs an existing script in the repo/library.
    """
    click.echo(f'Running {name}')
    # write API endpoint to run a script by name or id
    # before that it needs to search to see if it exists so search function (by name or id) needs to exist too

@click.command()
def template_command():
    """
    Executes template_command.
    """
    click.echo('Template_command executing')

cli.add_command(ls)
cli.add_command(run)
cli.add_command(hello)
cli.add_command(template_command)

if __name__ == '__main__':
    cli()