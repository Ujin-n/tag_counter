import sqlite3
import pickle


class DbLoader:
    def __init__(self, tag_dict, url_address):
        sqlite3.register_converter("pickle", pickle.loads)
        sqlite3.register_adapter(list, pickle.dumps)
        sqlite3.register_adapter(set, pickle.dumps)

        self.tag_dict = tag_dict
        self.url_address = url_address
        self.table_name = "tags_dictionary"

        self.insert_string = "INSERT into %s values (?, ?, ?, ?)" % self.table_name
        # self.update_string = "UPDATE %s SET lines=?, parents=? WHERE id=?" % self.table_name
        self.select_string = "SELECT site_name, url, check_date, tag_dict FROM %s" % self.table_name

    def create_schema(self, cursor):
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
        try:
            cursor.execute(self.insert_string, obj)
        except sqlite3.IntegrityError:
            print("Duplicate key")
        conn.commit()

    # def update_in_db(self, cursor, obj):
        # cursor.execute(self.update_string, obj)

    def get_obj_from_db(self, cursor):
        cursor.execute(self.select_string)
        data = cursor.fetchone()
        return data

    def run(self):
        conn = sqlite3.connect('tag_statistics.db', detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = conn.cursor()

        self.create_schema(cursor)

        some_object = (self.url_address, self.url_address, 'test', 'test')
        self.insert_into_db(cursor, some_object, conn)

        #print(get_obj_from_db(c, (key,)))
        #update_in_db(c, (key, [1, 2, 4], {1, 2, 3}))
        print(self.get_obj_from_db(cursor))

        print("saved object")

