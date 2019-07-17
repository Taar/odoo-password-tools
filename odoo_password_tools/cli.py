import click
import configparser

from .database import test, change_password

@click.command()
@click.argument('config_path', type=click.Path(exists=True))
def test_db(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)

    dbname = config['database'].get('dbname')
    dbpassword = config['database'].get('dbpassword')
    dbuser = config['database'].get('dbuser')
    dbhost = config['database'].get('dbhost')
    dbport = config['database'].getint('dbport')

    # password = config['password'].get('password')

    test(dbname, dbuser, dbpassword, dbhost, dbport)

@click.command()
@click.argument('config_path', type=click.Path(exists=True))
def manage(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)

    dbname = config['database'].get('dbname')
    dbpassword = config['database'].get('dbpassword')
    dbuser = config['database'].get('dbuser')
    dbhost = config['database'].get('dbhost')
    dbport = config['database'].getint('dbport')

    password = config['password'].get('password')
    login = config['password'].get('login')

    change_password(
        {
            'dbname': dbname,
            'password': dbpassword,
            'user': dbuser,
            'host': dbhost,
            'port': dbport
        },
        {
            'password': password,
            'login': login
        }
    )
