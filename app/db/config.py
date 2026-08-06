#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class UserTable:

    NAME = "users"

    SCHEMA = """
        CREATE TABLE users (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            text           TEXT NOT NULL,
            pass_hashed    TEXT
        )
    """

    SEED_DATA = """
    """

class MoveTable:

    NAME = "moves"

    SCHEMA = """
        CREATE TABLE moves (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id        INTEGER FOREIGN KEY,
            address        TEXT NOT NULL,
            date           DATE
        )
    """

    SEED_DATA = """
    """

class BoxTable:

    NAME = "boxes"

    SCHEMA = """
        CREATE TABLE boxes (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            move_id        INTEGER FOREIGN KEY,
            name           TEXT,
            location       TEXT
        )
    """

    SEED_DATA = """
    """

class ItemTable:

    NAME = "items"

    SCHEMA = """
        CREATE TABLE items (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            box_id         INTEGER FOREIGN KEY,
            name           TEXT,
            fragile        BOOLEAN
        )
    """

    SEED_DATA = """
    """


#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    NoteTable,
    # Add more tables here...
]

