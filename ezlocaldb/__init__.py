from pathlib import Path

import appdirs
from sqlalchemy import Engine, create_engine as _create_engine

DEFAULT_NAME = "Database.db"


def get_engine(app_name: str, db_name: str = DEFAULT_NAME) -> Engine:
    """Return an SQlAlchemy Engine for a specific app"""
    db_path = _setupDB(app_name, db_name)
    engine = _create_engine(f"sqlite:///{str(db_path)}")
    return engine


def _setupDB(app_name: str, db_name: str) -> Path:
    """Setup the database file in the appropriate location.
    If the file already exists, nothing is changed.
    Returns a Path object to the database"""

    db_dir = Path(appdirs.user_data_dir(appname=app_name))
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / db_name
    db_path.touch(exist_ok=True)
    return db_path


def removeDatabase(app_name: str, db_name: str = DEFAULT_NAME):
    """Remove database file.

    Also removes the data folder tree, if it is empty."""
    db_path = _setupDB(app_name, db_name)
    db_path.unlink(missing_ok=True)
    temp = db_path.parent
    try:
        while temp != temp.parent:
            temp.rmdir()
            temp = temp.parent
    except OSError:
        # Something else is still in the directory.
        # Ignore this, assume someone else put something here.
        pass


if __name__ == "__main__":
    get_engine("MyScractchApp")
