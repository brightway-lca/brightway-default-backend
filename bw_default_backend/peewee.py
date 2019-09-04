# -*- coding: utf-8 -*-
from peewee import SqliteDatabase, Model, TextField
import os
import json


class JSONField(TextField):
    def db_value(self, value):
        return super(JSONField, self).db_value(
            json.dumps(value)
        )

    def python_value(self, value):
        return json.loads(value)


class SubstitutableDatabase(object):
    def __init__(self, filepath, tables):
        self._filepath = filepath
        self._tables = tables
        self._database = self._create_database()

    def _create_database(self):
        db = SqliteDatabase(self._filepath)
        for model in self._tables:
            model.bind(db, bind_refs=False, bind_backrefs=False)
        db.connect()
        db.create_tables(self._tables)
        return db

    @property
    def db(self):
        return self._database

    def change_path(self, filepath):
        self.db.close()
        self._filepath = filepath
        self._database = self._create_database()

    def atomic(self):
        return self.db.atomic()

    def execute_sql(self, *args, **kwargs):
        return self.db.execute_sql(*args, **kwargs)

    def transaction(self):
        return self.db.transaction()

    def vacuum(self):
        print("Vacuuming database ")
        self.execute_sql('VACUUM;')
