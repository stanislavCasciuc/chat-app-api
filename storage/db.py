from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, ARRAY, ForeignKey
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://postgres:stas@localhost:5432/postgres'
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('password', String),
)

discussions_contacts = Table('discussions_contacts', metadata,
    Column('id', Integer, primary_key=True),
    Column('discussion_id', Integer, ForeignKey('discussions.id')),
    Column('user_id', Integer, ForeignKey('users.id')),
)

discussions = Table('discussions', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)


metadata.create_all(engine)

new_user = {'name': 'Vasile', 'password': 'test123'}
insert_statement = users.insert().values(new_user)
session.execute(insert_statement)
session.commit()
new_discussion={'name':'Vasile'}
insert_statement= discussions.insert().values(new_discussion)
session.execute(insert_statement)
session.commit()
new_discussion_contacts={'discussion_id': 1, 'user_id': 1}
insert_statement = discussions_contacts.insert().values(new_discussion_contacts)
session.execute(insert_statement)
session.commit()

session.close()




