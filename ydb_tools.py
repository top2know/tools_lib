import ydb
import os

from dotenv import load_dotenv

load_dotenv()

# Внутри Яндекс Облака можно без credentials
# IAM_TOKEN надо обновлять не реже чем раз в 12 часов
# https://cloud.yandex.ru/docs/iam/operations/iam-token/create

# create driver in global space.
driver_config = ydb.DriverConfig(
        endpoint=os.getenv('YDB_ENDPOINT'), database=os.getenv('YDB_DATABASE'),
        credentials=ydb.AccessTokenCredentials(os.getenv('IAM_TOKEN'))
    )


driver = ydb.Driver(driver_config)
# Wait for the driver to become active for requests.
driver.wait(fail_fast=True, timeout=5)
# Create the session pool instance to manage YDB sessions.
pool = ydb.SessionPool(driver)


def select_all(tablename):
    # create the transaction and execute query.
    text = f"SELECT * FROM {tablename};"
    return pool.retry_operation_sync(lambda s: s.transaction().execute(
        text,
        commit_tx=True,
        settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
    ))


def select(tablename, selection='*', where_statement='1=1'):
    text = f"SELECT {selection} FROM {tablename} WHERE {where_statement};"
    return pool.retry_operation_sync(lambda s: s.transaction().execute(
        text,
        commit_tx=True,
        settings=ydb.BaseRequestSettings().with_timeout(3).with_operation_timeout(2)
    ))
