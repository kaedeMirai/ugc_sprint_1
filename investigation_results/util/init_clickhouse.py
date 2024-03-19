from clickhouse_driver import Client

from core.config import settings


def init_clickhouse():
    with Client(host=settings.clickhouse_host) as client:
        client.execute("""
                    ATTACH DATABASE IF NOT EXISTS uuid
                    ON CLUSTER company_cluster ENGINE = Ordinary
                    """)
        client.execute("""
            CREATE TABLE IF NOT EXISTS uuid.uuid_v1 (id UUID) ENGINE = Memory;
        """)
        client.execute("""
                    CREATE DATABASE IF NOT EXISTS test
                    ON CLUSTER company_cluster
                    """)
        client.execute("""
            CREATE TABLE IF NOT EXISTS test.view (
                id UUID DEFAULT generateUUIDv4() NOT NULL,
                user_id String NOT NULL,
                movie_id String NOT NULL,
                viewed_frame UInt32 NOT NULL
            ) ENGINE = MergeTree ORDER BY id;
        """)

        client.execute("""
        CREATE INDEX idx_user_movie ON test.view (user_id, movie_id) TYPE minmax GRANULARITY 1;
        """)
