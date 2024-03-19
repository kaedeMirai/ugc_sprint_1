import asyncio
import logging
from aiochclient import ChClient

from core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def execute_clickhouse_commands(url, commands):
    async with ChClient(url=url) as client:
        for command in commands:
            try:
                await client.execute(command)
                logger.info(f"Completed successfully: {command}")
            except Exception as e:
                logger.error(f"Error when executing the command: {command}\nERROR: {str(e)}")


async def execute_commands_for_nodes(nodes: list):
    for node in nodes:
        url = node['url']
        commands = node['commands']
        await execute_clickhouse_commands(url, commands)


async def init_clickhouse():

    node1_commands = [
        "CREATE DATABASE data_analytics;",
        "CREATE TABLE data_analytics.event_table (id String, user_id String, movie_id String, action String, timestamp Int64, event_data String, event_time DateTime) Engine=ReplicatedMergeTree('/clickhouse/tables/data_analytics1/event_table', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;",
        "CREATE TABLE default.event_table (id String, user_id String, movie_id String, action String, timestamp Int64, event_data String, event_time DateTime) ENGINE = Distributed('company_cluster', '', event_table, rand());"
    ]

    node2_commands = [
        "CREATE DATABASE replica;",
        "CREATE TABLE replica.event_table (id String, user_id String, movie_id String, action String, timestamp Int64, event_data String, event_time DateTime) Engine=ReplicatedMergeTree('/clickhouse/tables/data_analytics1/event_table', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;"
    ]

    node3_commands = [
        "CREATE DATABASE data_analytics;",
        "CREATE TABLE data_analytics.event_table (id String, user_id String, movie_id String, action String, timestamp Int64, event_data String, event_time DateTime) Engine=ReplicatedMergeTree('/clickhouse/tables/data_analytics2/event_table', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;",
        "CREATE TABLE default.event_table (id String, user_id String, movie_id String, action String, timestamp Int64, event_data String, event_time DateTime) ENGINE = Distributed('company_cluster', '', event_table, rand());"
    ]

    node4_commands = [
        "CREATE DATABASE replica;",
        "CREATE TABLE replica.event_table (id String, user_id String, movie_id String, action String, timestamp Int64, event_data String, event_time DateTime) Engine=ReplicatedMergeTree('/clickhouse/tables/data_analytics2/event_table', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;"
    ]

    nodes = [
        {'url': settings.clickhouse_brokers[0], 'commands': node1_commands},
        {'url': settings.clickhouse_brokers[1], 'commands': node2_commands},
        {'url': settings.clickhouse_brokers[2], 'commands': node3_commands},
        {'url': settings.clickhouse_brokers[3], 'commands': node4_commands},
    ]

    for node in nodes:
        await execute_clickhouse_commands(node['url'], node['commands'])
        await asyncio.sleep(1)
