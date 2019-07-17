import psycopg2
from passlib.context import CryptContext
from typing import Dict

def change_password(connection: Dict, data: Dict) -> None:
    cxt = CryptContext(schemes=['pbkdf2_sha512'])
    pw_hash = cxt.hash(data['password'])

    with psycopg2.connect(**connection) as conn:
        with conn.cursor() as cursor:
            update_query = (
                'UPDATE res_users '
                'SET password = %(password)s '
                'WHERE login = %(login)s'
            )
            cursor.execute(update_query, {
                'password': pw_hash,
                'login': data['login'],
            })

        with conn.cursor() as cursor:
            query = (
                'SELECT password FROM res_users '
                'WHERE login = %(login)s'
            )

            cursor.execute(query, {
                'login': data['login'],
            })

            result = cursor.fetchone()

            if not result:
                raise Exception('No results found!')

            check_password = result[0]

            if cxt.verify(data['password'], check_password):
                print('Success!')
            else:
                raise Exception('Hash stored in database did not match!')


def test(dbname: str, dbuser: str, dbpassword: str, dbhost: str, dbport: int) -> None:
    with psycopg2.connect(
            dbname=dbname,
            user=dbuser,
            password=dbpassword,
            host=dbhost,
            port=dbport,
        ):
        print('Success!')
