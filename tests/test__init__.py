from typing import Optional

import pytest  # noqa: F401

from sqlalchemy import Engine, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

import ezlocaldb as ezdb

appName = "MyAppName"
dbName = "MyTestDatabase.db"


def test_create_and_remove_db():
    engine = ezdb.get_engine(appName)
    assert isinstance(engine, Engine)


def test_db_path_setup_and_removal():
    dbPath, _ = ezdb._setupDB(appName, dbName)
    assert dbPath.exists()
    ezdb.removeDatabase(appName, dbName)
    assert not dbPath.exists()


@pytest.fixture
def test_metadata():
    class Base(DeclarativeBase):
        pass

    class TestObjects(Base):
        __tablename__ = "TestingTable"
        id: Mapped[int] = mapped_column(primary_key=True)
        testfield: Mapped[str]
        optfield: Mapped[Optional[str]]

    return Base.metadata


def test_create_wMetadata_and_delete(test_metadata):
    """Test Database creationg with metadata emission, then DB removal"""
    # Test only works if database doesn't exist ahead of time.
    ezdb.removeDatabase(appName, dbName)
    dbPath = ezdb._getDBPath(appName, dbName)
    assert not dbPath.exists()

    eng = ezdb.get_engine("MyTestDatabase.db", metadata=test_metadata)
    newMetadata = MetaData()
    newMetadata.reflect(bind=eng)
    assert "TestingTable" in newMetadata.tables
    testingTable = newMetadata.tables["TestingTable"]
    assert "id" in testingTable.c

    ezdb.removeDatabase(appName, dbName)

    assert not dbPath.exists()

    # Try using disposed engine and see what happens!
    newMetadata.create_all(eng)
    assert not dbPath.exists()
