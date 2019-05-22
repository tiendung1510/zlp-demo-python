from peewee import Model, MySQLDatabase, CharField, IntegerField
from config import config

cfg = config['db']
db = MySQLDatabase(cfg['dbname'], host=cfg['host'], port=cfg['port'], user=cfg['user'], passwd=cfg['password'])

class Order(Model):
  class Meta:
    database = db
    table_name = "orders"

  apptransid = CharField(primary_key=True)
  zptransid = CharField()
  description = CharField()
  amount = IntegerField()
  timestamp = IntegerField()
  channel = IntegerField()

db.connect()
db.create_tables([Order])