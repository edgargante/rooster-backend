import peewee
from peewee import *

database = peewee.MySQLDatabase(
    'rooster',
    user='root',
    password='admin',
    host='localhost',
    port=3306
)


class User(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)
    role = IntegerField(1)

    def __str__(self):
        return self.name

    class Meta:
        database = database


