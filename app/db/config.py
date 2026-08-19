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
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            name         TEXT NOT NULL,
            pass_hash    TEXT
        )
    """

    SEED_DATA = """
            INSERT INTO users (id, name, pass_hash) VALUES
            (1, "BiggRigg", "scrypt:32768:8:1$n7eJTucLbaGmUpAM$c1776374a8d456a6eaf61bccc08db5e1fcc4ff3b3983d364c45ab13074255eeae0a393afb11f99a9fe63fb1d980992ace17a72ba70324523b11e92e36cbe4252"),
            (2, "Clieran Kark", "scrypt:32768:8:1$n7eJTucLbaGmUpAM$c1776374a8d456a6eaf61bccc08db5e1fcc4ff3b3983d364c45ab13074255eeae0a393afb11f99a9fe63fb1d980992ace17a72ba70324523b11e92e36cbe4252"),
            (3, "Hachlan Lunt", "scrypt:32768:8:1$n7eJTucLbaGmUpAM$c1776374a8d456a6eaf61bccc08db5e1fcc4ff3b3983d364c45ab13074255eeae0a393afb11f99a9fe63fb1d980992ace17a72ba70324523b11e92e36cbe4252")
    """ 

class MoveTable:

    NAME = "moves"

    SCHEMA = """
        CREATE TABLE moves (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id        INTEGER,
            address        TEXT NOT NULL,
            date           TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """

    SEED_DATA = """
            INSERT INTO moves (id, user_id, address, date) VALUES
            (1, 1, "5318008 street street", "2026-07-27"),
            (2, 1, "1 john street", "0001-01-01"),
            (3, 2, "4A Flightly Avenue", "2014-05-01"),
            (4, 2, "68 Ranzau Road", "2026-08-10"),
            (5, 3, "47389124321 Black Hole Galaxy", "3571-05-23"),
            (6, 3, "2 Jane Street", "0001-01-02")
    """

class BoxTable:

    NAME = "boxes"

    SCHEMA = """
        CREATE TABLE boxes (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            move_id        INTEGER,
            name           TEXT NOT NULL,
            location       TEXT,
            FOREIGN KEY(move_id) REFERENCES moves(id)
        )
    """

    SEED_DATA = """
        INSERT INTO boxes (id, move_id, name, location) 
            VALUES
                (1, 1, "Kitchen trays", "kitchen"),
                (2, 1, "Kitchen utensils", "kitchen"),
                (3, 2, "Uggrugs stuff", "Uggrugs room"),
                (4, 2, "Grugugs stuff", "Grugugs room"),
                (5, 3, "Kierans crap", "Attic"),
                (6, 3, "Gun pieces", "Garage"),
                (7, 4, "PC components", "Kierans room"),
                (8, 4, "Geryon Watcher of the Skies", "the 8th layer of hell"),
                (9, 5, "secrets of the universe", "n-th dimension hyperplane"),
                (10, 5, "interstellar objects", "bathroom"),
                (11, 6, "regrets", "the deepest darkest recesses of the human mind"),
                (12, 6, "pain.", "everywhere")
    """

class ItemTable:

    NAME = "items"

    SCHEMA = """
        CREATE TABLE items (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            box_id         INTEGER,
            name           TEXT NOT NULL,
            count          INTEGER,
            fragile        BOOLEAN,
            FOREIGN KEY(box_id) REFERENCES boxes(id)
        )
    """

    SEED_DATA = """
            INSERT INTO items (id, box_id, name, count, fragile) VALUES
            (1, 1, "baking tray", 4, false),
            (2, 1, "wire rack", 3, false),
            (3, 2, "oven mitt", 3, false),
            (4, 2, "1000 degree knife", 5, true),
            (5, 2, "slaptula", 1, false),
            (6, 3, "rocks", 51, false),
            (7, 3, "expensive rocks", 11, true),
            (8, 3, "DISINTEGRATION LOOP", 13, false),
            (9, 4, "sticks", 18, false),
            (10, 4, "sticks (VERY EXPENSIVE)", 2, false),
            (11, 5, "school blazer", 1, false),
            (12, 5, "Flopparena collectors edition", 1, true),
            (13, 5, "dino plushie :D", 1, true),
            (14, 6, "10x scope", 2, true),
            (15, 6, "50 BMG rifle", 32, false),
            (16, 6, "cara", 574832, true),
            (17, 6, "bullet singular", 51, false),
            (18, 6, "bullet x51", 1, false),
            (19, 7, "GPU", 1, true),
            (20, 7, "monitor", 2, true),
            (21, 7, "everything else lmao", 1, true),
            (22, 8, "providence", 3, true),
            (23, 8, "virtue", 3, true),
            (24, 8, "souls of the damned", 10, false),
            (25, 9, "42", 1, true),
            (26, 10, "black hole", 14, false),
            (27, 10, "sun", 10, false),
            (28, 10, "red dwarf", 39, false),
            (29, 10, "rocky planet capable of life", 1, false),
            (30, 11, "never talking to that girl you liked in highschool", 13, true),
            (31, 11, "never attempting for that promotion", 2, false),
            (32, 11, "not spending enough time with grandparents before they died", 83, false),
            (33, 11, "not jumping for the beef", 1, true),
            (34, 12, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", 1, false),
            (35, 12, "THE LAVAAAAAAAAAA IT BURNSSSSSSSSSSSS", 2, true),
            (36, 12, "HELP MEEEEE PLEASEEEEEEEE", 3, true),
            (37, 12, "poster", 4, false)
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
    UserTable,
    MoveTable,
    BoxTable,
    ItemTable
]

