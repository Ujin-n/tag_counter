import unittest
from DbLoader import DbLoader
from datetime import datetime
import sqlite3


class TestDbLoader(unittest.TestCase):
    """ Tests for the class DbLoader """

    def setUp(self):
        """ Create DbLoader object for use in all tests """

        tag_dict = {"tag1": 1, "tag2": 2}
        url = "www.test.com"
        current_date = datetime.now().date()

        self.dl = DbLoader(tag_dict, url, current_date, 'W')

        self.con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.con.cursor()

    def test_create_schema(self):
        """ Test Create Table statement """

        self.dl.create_schema(self.cur)

        db_table_name = self.cur.execute("SELECT name "
                                         "FROM sqlite_master "
                                         "WHERE type='table' "
                                         "AND name='{}';".format(self.dl.table_name)).fetchone()[0]

        self.assertEqual(self.dl.table_name, db_table_name)

    def test_insert_into_db(self):
        """ Test Insert statement """
        self.dl.create_schema(self.cur)

        db_object_expected = ("test_insert_into_db", "test2", "test3", "test4")

        self.dl.insert_into_db(self.cur, db_object_expected, self.con)

        db_object_actual = self.cur.execute("SELECT site_name, url, check_date, tag_dict "
                                            "FROM {} "
                                            "WHERE site_name = '{}'".format(self.dl.table_name,
                                                                            db_object_expected[0])).fetchone()

        self.assertEqual(db_object_expected, db_object_actual)

    def test_get_obj_from_db(self):
        """ Test Select statement """

        self.dl.create_schema(self.cur)

        db_object_expected = ("test_get_obj_from_db", "test2", "test3", "test4")
        self.dl.insert_into_db(self.cur, db_object_expected, self.con)

        db_object_actual = self.cur.execute("SELECT site_name, url, check_date, tag_dict "
                                            "FROM {} "
                                            "WHERE site_name = '{}' ".format(self.dl.table_name,
                                                                             db_object_expected[0])).fetchone()

        self.assertEqual(db_object_expected, db_object_actual)


unittest.main(exit=False)
