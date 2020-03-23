import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

def save_album(user_data):
    

    year = user_data["year"]
    artist = user_data["artist"]
    genre = user_data["genre"]
    album = user_data["album"]
    session = connect_db()
 
    album_ = Album(
        
        year=year,
        artist=artist,
        genre=genre,
        album=album,
    )
    # запрашиваем данные пользоватлея
    # добавляем нового пользователя в сессию
    session.add(album_)
    # сохраняем все изменения, накопленные в сессии
    session.commit()
    # возвращаем созданного пользователя
    return album_

find("Tommy Vice")
