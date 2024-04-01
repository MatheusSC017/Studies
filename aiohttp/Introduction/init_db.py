from sqlalchemy import URL, create_engine, MetaData

from aiohttpdemo_polls.settings import config
from aiohttpdemo_polls.db import question, choice


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])


def sample_data(engine):
    conn = engine.connect()
    result = conn.execute(question.insert(), [
        {'question_text': 'What\'s new?',
         'pub_date': '2015-12-15'}
    ])
    question_id = result.inserted_primary_key[0]
    conn.execute(choice.insert(), [
        {'choice_text': 'Not much', 'votes': 0, 'question_id': question_id},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': question_id},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': question_id},
    ])
    conn.commit()
    conn.close()


if __name__ == '__main__':
    db_url = URL.create("mysql+pymysql", **config['mysql'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
