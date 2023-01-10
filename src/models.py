# import os
# import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    name = Column(String(64), nullable=False)
    lastname = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(16), nullable=False)


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    caption = Column(String(256))
    comments = Column(String(256))
    image_url = Column(String(256))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)  # Los relationship van siempre en mayúscula porque hacen referencia a la class


class Follow(Base):
    __tablename__ = "follow"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship(User)
    post = relationship(Post)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e