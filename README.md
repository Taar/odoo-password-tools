# Odoo Password tools

Small sets of CLI tools to help manage odoo users by modifying the database. Mainly used to change the `admin`'s password.

## Config file

Example config:

    [database]
    dbname = odoo_demo
    dbuser = odoo
    dbpassword = supersecure
    dbhost = localhost
    dbport = 5432

    [password]
    password = supersupersecure
    login = admin

## CLI

Test your config:

    python test_connection.py database.ini

Update user's password:

    python update.py database.ini
