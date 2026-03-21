import click
@click.group()
def cli():
    """Deploy AI agents to any platform."""
    pass
@cli.command()
@click.argument('path')
@click.option('--platform', required=True, help='vercel|railway|fly|k8s')
@click.option('--name', required=True, help='Agent name')
def deploy(path, platform, name):
    click.echo(f"Deploying {path} to {platform} as {name}...")
    click.echo("TODO: Implement deployment logic")
if __name__ == "__main__":
    cli()
