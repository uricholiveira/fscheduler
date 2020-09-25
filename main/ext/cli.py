import click


def init_app(app):
	# app.cli.add_command(app.cli.command()function()) # To register a command from another file
	@app.cli.command(help='Flask say "Hello! :)"')
	def say_hello():
		click.echo('Hello! :)')
