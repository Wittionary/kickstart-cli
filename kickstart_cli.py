import click
import requests
import json

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
    try:
        r = requests.get("http://localhost:5000/api/v1/resources/scripts/all")
    except requests.exceptions.ConnectionError as e:
        click.echo(f"ConnectionError: {e}")
    else:
        # Format the JSON response in a user-friendly way
        script_library = json.loads(r.content)

        for script in script_library:
            print(f"{script['id']}\t{script['name']}\t{script['language']}")
        click.echo()

@click.command()
@click.option('--name', help='Name of the script or *.exe', type=str)
@click.option('--id', help='Id of the script', type=int)
def run(name, id):
    """
    This runs an existing script in the repo/library.
    """
    if id != None:
        click.echo(f'Running script id {id}')
    elif id == None and name != None:
        click.echo(f'Running {name}')
    else:
        click.echo("No name or id entered")

    # write API endpoint to run a script by name or id
    # before that it needs to search to see if it exists so search function (by name or id) needs to exist too

@click.command()
@click.option('--user', help='Username to login as')
def auth():
    """
    Authenticate to the kickstart server.
    """
    click.echo('Authenticating to the kickstart server.')
    try:
        r = requests.post("http://localhost:5000/api/v1/authenticate")
    except requests.exceptions.ConnectionError as e:
        click.echo(f"ConnectionError: {e}")
    else:
        click.echo(r.content)


@click.command()
def template_command():
    """
    Executes template_command.
    """
    click.echo('Template_command executing')

cli.add_command(ls)
cli.add_command(run)
cli.add_command(hello)
cli.add_command(auth)

cli.add_command(template_command)

if __name__ == '__main__':
    cli()