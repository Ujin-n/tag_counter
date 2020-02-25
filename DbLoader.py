import sqlite3
import pickle
from tld import get_tld


class DbLoader:
    """ SQL-lite database. """
    def __init__(self, tag_dict, url_address, current_date):
        """ Initialize sql-lite db object. """
        sqlite3.register_converter("pickle", pickle.loads)
        sqlite3.register_adapter(list, pickle.dumps)
        sqlite3.register_adapter(set, pickle.dumps)

        self.tag_dict = tag_dict
        self.url_address = url_address
        self.table_name = "tags_dictionary"
        self.current_date = current_date

        self.insert_string = "INSERT into %s values (?, ?, ?, ?)" % self.table_name
        # self.update_string = "UPDATE %s SET lines=?, parents=? WHERE id=?" % self.table_name
        self.select_string = "SELECT site_name, url, check_date, tag_dict FROM %s" % self.table_name

    def create_schema(self, cursor):
        """ Method creates sql-lite database schema. """
        try:
            cursor.execute("""
                CREATE TABLE %s (
                    site_name text,
                    url text,
                    check_date text,
                    tag_dict text
                    )""" % self.table_name)
        except sqlite3.OperationalError as e:
            print(e)

    def insert_into_db(self, cursor, obj, conn):
        """ Method inserts data into sql-lite database. """
        cursor.execute(self.insert_string, obj)
        conn.commit()

    def get_obj_from_db(self, cursor):
        """ Method selects data from sql-lite database. """
        cursor.execute(self.select_string)
        data = cursor.fetchall()
        return data

    def url_parser(self):
        """ Method retrieve second-level domain from given url. """
        res_domain = get_tld(self.url_address, as_object=True)
        return res_domain.domain

    def run(self):
        """ Method runs main functionality. """
        conn = sqlite3.connect('tag_statistics.db', detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = conn.cursor()

        # creating database table
        self.create_schema(cursor)

        # Getting second level domain
        second_level_domain = str(self.url_parser())

        # inserting tag dictionary
        db_object = (second_level_domain, self.url_address, self.current_date, str(self.tag_dict))
        self.insert_into_db(cursor, db_object, conn)

        # Printing data from database to console (debug purpose)
        print(self.get_obj_from_db(cursor))
