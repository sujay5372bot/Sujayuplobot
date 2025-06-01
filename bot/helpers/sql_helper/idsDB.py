from sqlalchemy import Column, String, Numeric, create_engine
from bot.helpers.sql_helper import SESSION, BASE

engine = create_engine("postgresql://neondb_owner:npg_8w2EuyZpJWSK@ep-odd-wave-a8rqj0vz-pooler.eastus2.azure.neon.tech/neondb?sslmode=require") #Example sqlite//yourdb.db
class ParentID(BASE):
    __tablename__ = "ParentID"
    chat_id = Column(Numeric, primary_key=True)
    parent_id = Column(String)


    def __init__(self, chat_id, parent_id):
        self.chat_id = chat_id
        self.parent_id = parent_id

ParentID.__table__.create(bind=engine, checkfirst=True)


def search_parent(chat_id):
    try:
        return SESSION.query(ParentID).filter(ParentID.chat_id == chat_id).one().parent_id
    except:
        return 'root'
    finally:
        SESSION.close()


def _set(chat_id, parent_id):
    adder = SESSION.query(ParentID).get(chat_id)
    if adder:
        adder.parent_id = parent_id
    else:
        adder = ParentID(
            chat_id,
            parent_id
        )
    SESSION.add(adder)
    SESSION.commit()


def _clear(chat_id):
    rem = SESSION.query(ParentID).get(chat_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
