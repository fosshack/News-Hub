#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(25), index=True, unique=True,
                         nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True,
                      nullable=False)

    def __init__(
            self,
            username,
            password,
            email,
    ):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class news_data(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    author = db.Column(db.String(5012), nullable=True)
    title = db.Column(db.String(5012), nullable=False)
    desc = db.Column(db.String(5012), nullable=True)
    url = db.Column(db.String(5012), nullable=True)
    urlToImage = db.Column(db.String(5012), nullable=True)
    publishedAt = db.Column(db.String(5012), nullable=True)
    downvotes = db.Column(db.INTEGER, nullable=True)
    upvotes = db.Column(db.INTEGER, nullable=True)
    category = db.Column(db.String(5012),nullable=True)

    def __init__(self, author, title, desc, url, urlToImage, publishedAt, category):
        self.author = author
        self.title = title
        self.desc = desc
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.category = category

    def upvote(self):
        if not self.upvotes:
            self.upvotes = 1
        else:
            self.upvotes +=1

    def downvote(self):
        if not self.downvotes:
            self.downvotes = 1
        else:
            self.downvotes +=1

class user_vote_data(db.Model):
    __tablename__ = 'vote_data'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    downvotes = db.Column(db.INTEGER, nullable=True)
    upvotes = db.Column(db.INTEGER, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))


    def __init__(self,upvote=None,downvote=None,user_id=None,news_id=None):
        self.downvote = downvote
        self.upvotes = upvote
        self.user_id = user_id
        self.news_id = news_id

class Post(db.Model):
    __tablename__="news_db"
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    user_id = db.Column(db.String(255))
    upvotes = db.Column(db.String(255))
    downvotes = db.Column(db.Integer)
    news_id = db.Column(db.String(255))
    check_votes = db.Column(db.String(255))
    def __init__(self, user_id=None, upvotes=None, downvotes=None, news_id=None,check_votes=None):
        self.user_id= user_id
        self.news_id = news_id
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.check_votes = check_votes

    def upvote(self):
        if not self.upvotes:
            self.upvotes = 1
        else:
            self.upvotes +=1

    def downvote(self):
        if not self.downvotes:
            self.downvotes = 1
        else:
            self.downvotes +=1