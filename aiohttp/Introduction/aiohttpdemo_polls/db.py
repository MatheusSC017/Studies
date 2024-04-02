from sqlalchemy import (MetaData, Table, Column, ForeignKey, Integer, String, Date, select)
from aiomysql.sa import create_engine

meta = MetaData()

question = Table(
    'question', meta,

    Column('id', Integer, primary_key=True),
    Column('question_text', String(200), nullable=False),
    Column('pub_date', Date, nullable=False)
)

choice = Table(
    'choice', meta,

    Column('id', Integer, primary_key=True),
    Column('choice_text', String(200), nullable=False),
    Column('votes', Integer, server_default="0", nullable=False),

    Column('question_id', Integer, ForeignKey('question.id', ondelete='CASCADE'))
)


async def mysql_context(app):
    conf = app['config']['mysql']
    engine = await create_engine(
        db=conf['database'],
        user=conf['username'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
    )
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()


async def get_question(conn, question_id):
    cursor_question = await conn.execute(select(question).where(question.columns.id == question_id))
    question_record = await cursor_question.fetchone()
    if not question_record:
        raise RecordNotFound
    cursor_choice = await conn.execute(select(choice).where(choice.columns.question_id == question_id))
    choice_records = await cursor_choice.fetchall()
    choice_records = [dict(c) for c in choice_records]
    return question_record, choice_records


class RecordNotFound(Exception):
    pass
