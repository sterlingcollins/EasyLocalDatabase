# ezlocaldb
Version 0.0.0

Easy, local databases for no-sweat persistence. This convinience package wraps
small parts of `appdirs`, `sqlite3`, and `sqlalchemy`, to easily create
databases for local applications. The package saves about 15 lines of code, but
it's 15 lines I find myself writting at the start of many projects, so maybe it
will save you some time too.

## Installation

### PIP
The easiest way to install `ezlocaldb` is with pip

```bash
  pip install ezlocaldb
```

## Usage/Examples

To work with `sqlalchemy` use `getEngine` to get an `engine` object for
database access. The first argument to `getEngine` is the name of your
application, which is used to uniquely specify the database.

```python
from ezlocaldb import get_engine
from sqlalchemy import Session

# Get an sqlalchemy engine to use with sqlalchemy.Session
engine = get_engine("MyAmazingApp")

with Session(engine) as session:
    # Now work with session to initalize database,
    # or execute other CRUD operations.
    pass
```

When you call `getEngine`, ezlocaldb checks to see if your database was created
previously. If it wasn't it creates a new `sqlite` database. Either way, it
returns an `engine` which can be used to access the database.

If you want to remove or refresh the database, use

```python
from ezlocaldb import removeDatabase

removeDatabase("MyAmazingApp")
```
