import sqlite3
import pickle
from tld import get_tld


class DbLoader:
    """ SQLite database. """
    def __init__(self, tag_dict, url_address, current_date, mode):
        """ Initialize sqlite db object. """
        sqlite3.register_converter("pickle", pickle.loads)
        sqlite3.register_adapter(list, pickle.dumps)
        sqlite3.register_adapter(set, pickle.dumps)

        self.tag_dict = tag_dict
        self.url_address = url_address
        self.table_name = "tags_dictionary"
        self.current_date = current_date
        self.mode = mode

        self.insert_string = "INSERT INTO {}(site_name, url, check_date, tag_dict) " \
                             "VALUES (?, ?, ?, ?)".format(self.table_name)
        self.select_string = "SELECT tag_dict " \
                             "FROM {0} " \
                             "WHERE url = '{1}'" \
                             "AND id = (SELECT MAX(ID) " \
                             "FROM {0} WHERE url = '{1}')".format(self.table_name, self.url_address)

    def create_schema(self, cursor):
        """ Method creates sqlite database schema. """
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS %s (
                    id INTEGER PRIMARY KEY,
                    site_name text,
                    url text,
                    check_date text,
                    tag_dict text
                    )""" % self.table_name)
        except sqlite3.OperationalError as e:
            print(e)

    def insert_into_db(self, cursor, obj, conn):
        """ Method inserts data into sqlite database. """
        cursor.execute(self.insert_string, obj)
        conn.commit()

    def get_obj_from_db(self, cursor):
        """ Method selects data from sqlite database. """
        try:
            cursor.execute(self.select_string)
        except sqlite3.OperationalError:
            print("No data is available in a database for the given URL: " + self.url_address)
        else:
            data = cursor.fetchall()
            return data

    def url_parser(self):
        """ Method retrieve second-level domain from given url. """
        url = self.url_address

        if not url.lower().startswith('https://'):
            url = 'https://' + url

        res_domain = get_tld(url, as_object=True)

        return res_domain.domain

    def run(self):
        """ Method runs main functionality. """
        conn = sqlite3.connect('tag_statistics.db', detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = conn.cursor()

        # INSERT INTO DB
        if self.mode == 'W':
            # creating database table
            self.create_schema(cursor)

            # Getting second level domain
            second_level_domain = str(self.url_parser())

            # inserting tag dictionary
            db_object = (second_level_domain, self.url_address, self.current_date, str(self.tag_dict))
            self.insert_into_db(cursor, db_object, conn)

        # SELECT FROM DB
        elif self.mode == 'R':
            return self.get_obj_from_db(cursor)

