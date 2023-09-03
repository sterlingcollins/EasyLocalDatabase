import pytest  # noqa: F401

from sqlalchemy import Engine

import ezlocaldb as ezdb

appname = "MyAppName"


def test_create_and_remove_db():
    engine = ezdb.get_engine(appname)
    assert isinstance(engine, Engine)


def test_db_path_setup_and_removal():
    dbName = "Database.db"
    dbPath = ezdb._setupDB(appname, dbName)
    assert dbPath.exists()
    ezdb.removeDatabase(appname, dbName)
    assert not dbPath.exists()
