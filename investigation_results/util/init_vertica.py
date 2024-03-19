import vertica_python
from core.config import settings


connection_info = {
    'host': settings.vertica_host,
    'port': settings.vertica_port,
    'user': settings.vertica_user,
    'password': settings.vertica_password,
    'database': settings.vertica_db,
    'autocommit': True,
}


def init_vertica():
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS view (
            id UUID DEFAULT uuid_generate() NOT NULL,
            user_id VARCHAR NOT NULL,
            movie_id VARCHAR NOT NULL,
            viewed_frame INTEGER NOT NULL
        );
        """)

        cursor.execute("""CREATE PROJECTION IF NOT EXISTS view_projection
                       (
                           id,
                           user_id,
                           movie_id,
                           viewed_frame
                        )
                        AS SELECT id, user_id, movie_id, viewed_frame
                        FROM view ORDER BY id, user_id, movie_id, viewed_frame
                        SEGMENTED BY HASH(id) ALL NODES KSAFE 0;""")

        cursor.execute("""SELECT MAKE_AHM_NOW();""")
