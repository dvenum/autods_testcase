from flask.cli import FlaskGroup

from app import create_app

fcli = FlaskGroup(create_app=create_app)

# we need more commands here, if it real application
# from cli import *


if __name__ == '__main__':
    fcli()
