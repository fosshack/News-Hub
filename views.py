#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import app, db
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from twitter_lib import TwitterClient
from newsapi import _news
import requests
from reduction import reduce
from models import User, news_data, user_vote_data,Post


@app.route('/')
def main():
    return render_template('index.html', title='Index')


# This is the login route

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('main'))
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            if user.verify_password(password):
                session['logged_in'] = True
                session['uid'] = user.id
                session['username'] = user.username
                check_user = Post.query.filter_by(user_id=username).first()
                user_id=username
                upvotes=0
                downvotes=0
                check_votes=0
                if not check_user:
                    for i in xrange(1,10):
                        news_id='G'+str(i)
                        c = Post(user_id, upvotes, downvotes, news_id, check_votes)
                        db.session.add(c)

                    for i in xrange(1,10):
                        news_id='S'+str(i)
                        c = Post(user_id, upvotes, downvotes, news_id, check_votes)
                        db.session.add(c)

                    for i in xrange(1,10):
                        news_id='B'+str(i)
                        c = Post(user_id, upvotes, downvotes, news_id, check_votes)
                        db.session.add(c)

                    for i in xrange(1,10):
                        news_id='T'+str(i)
                        c = Post(user_id, upvotes, downvotes, news_id, check_votes)
                        db.session.add(c)

                    for i in xrange(1,10):
                        news_id='X'+str(i)
                        c = Post(user_id, upvotes, downvotes, news_id, check_votes)
                        db.session.add(c)

                    for i in xrange(1,10):
                        news_id='Y'+str(i)
                        c = Post(user_id, upvotes, downvotes, news_id, check_votes)
                        db.session.add(c)
                    
                    db.session.commit()
                flash('You are successfully logged in!')
                return redirect(url_for('main'))
        error = 'Invalid credentials!'
    return render_template('login.html', error=error)


# This is the signup route

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('logged_in'):
        return redirect(url_for('dash'))

    error = None
    user = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_pass = request.form['confirm_pass']


        user = User.query.filter_by(username=username).first()

        if user:
            error = 'Username already used.'
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                error = 'Email already used.'
            elif password != confirm_pass:
                error = "Passwords don't match."
            else:
                u = User(username, password, email)
                db.session.add(u)
                db.session.commit()
                flash('Registration successfull')
                return redirect(url_for('register'))

    return render_template('signup.html', error=error)


@app.route('/forgot')
def forgot():
    return 'forgot'

@app.route('/settings')
def settings():
    return 'settings'


@app.route('/api/general')
def general():
    news_obj = _news()
    news_dict = news_obj.get_json('the-telegraph')

    for news in news_dict['articles']:
        author =  news['author']
        title = news['title']
        desc = news['description']
        url = news['url']
        urlToImage = news['urlToImage']
        publishedAt = news['publishedAt']
        category = 'general'

        news_obj = news_data.query.filter_by(title=title).first()
        if not news_obj:
            news_obj = news_data(author,title,desc,url,urlToImage,publishedAt, category)
            db.session.add(news_obj)
            db.session.commit()

    news_obj = news_data.query.filter_by(category='general').all()
    return render_template('general.html', news_dict=news_dict,news_obj=news_obj)


@app.route('/api/sports')
def sports():
    news_obj = _news()
    news_dict = news_obj.get_json('fox-sports')

    for news in news_dict['articles']:
        author =  news['author']
        title = news['title']
        desc = news['description']
        url = news['url']
        urlToImage = news['urlToImage']
        publishedAt = news['publishedAt']
        category = 'sports'

        news_obj = news_data.query.filter_by(title=title).first()
        if not news_obj:
            news_obj = news_data(author,title,desc,url,urlToImage,publishedAt, category)
            db.session.add(news_obj)
            db.session.commit()
    return render_template('sports.html', news_dict=news_dict)


@app.route('/api/business')
def business():
    news_obj = _news()
    news_dict = news_obj.get_json('business-insider')

    for news in news_dict['articles']:
        author =  news['author']
        title = news['title']
        desc = news['description']
        url = news['url']
        urlToImage = news['urlToImage']
        publishedAt = news['publishedAt']
        category = 'business'

        news_obj = news_data.query.filter_by(title=title).first()
        if not news_obj:
            news_obj = news_data(author,title,desc,url,urlToImage,publishedAt, category)
            db.session.add(news_obj)
            db.session.commit()
    return render_template('bussiness.html', news_dict=news_dict)


@app.route('/api/technology')
def technology():
    news_obj = _news()
    news_dict = news_obj.get_json('engadget')
    for news in news_dict['articles']:
        author =  news['author']
        title = news['title']
        desc = news['description']
        url = news['url']
        urlToImage = news['urlToImage']
        publishedAt = news['publishedAt']
        category = 'technology'

        news_obj = news_data.query.filter_by(title=title).first()
        if not news_obj:
            news_obj = news_data(author,title,desc,url,urlToImage,publishedAt, category)
            db.session.add(news_obj)
            db.session.commit()

        news_obj = news_data.query.filter_by(title=title).first()

        if not news_obj:
            db.session.add(news_obj)
            db.session.commit()
    return render_template('technology.html', news_dict=news_dict)


@app.route('/api/gaming')
def gaming():
    news_obj = _news()
    news_dict = news_obj.get_json('ign')
    for news in news_dict['articles']:
        author =  news['author']
        title = news['title']
        desc = news['description']
        url = news['url']
        urlToImage = news['urlToImage']
        publishedAt = news['publishedAt']
        category = 'gaming'

        news_obj = news_data.query.filter_by(title=title).first()
        if not news_obj:
            news_obj = news_data(author,title,desc,url,urlToImage,publishedAt, category)
            db.session.add(news_obj)
            db.session.commit()
    return render_template('gaming.html', news_dict=news_dict)


@app.route('/api/science_nature')
def science_nature():
    news_obj = _news()
    news_dict = news_obj.get_json('daily-mail')
    for news in news_dict['articles']:
        author =  news['author']
        title = news['title']
        desc = news['description']
        url = news['url']
        urlToImage = news['urlToImage']
        publishedAt = news['publishedAt']
        category = 'science_nature'

        news_obj = news_data.query.filter_by(title=title).first()
        if not news_obj:
            news_obj = news_data(author,title,desc,url,urlToImage,publishedAt, category)
            db.session.add(news_obj)
            db.session.commit()
    return render_template('science_nature.html', news_dict=news_dict)


# This is the logout route
@app.route('/logout')
def logout():
    if not session.get('logged_in'):
        flash("You are not logged in!")
        return redirect(url_for('index'))

    session['logged_in'] = False
    session['uid'] = ""
    session['username'] = ""
    flash("You are successfully logged out!")
    return redirect(url_for('index'))


@app.route('/api/upvote/id/<string:id>/cat/<cat>')
def upvote(id,cat):
    if not session.get('logged_in'):
        flash("You are not logged in!")
        return redirect(url_for(cat))

    print id
    print session.get('uid')
    n = Post.query.filter_by(news_id=id).filter_by(user_id='jose')
    n = Post('jose',1,0,'G1',1)
    db.session.add(n)
    db.session.commit()

    flash("Upvotted..!")
    return redirect(url_for(cat))


@app.route('/api/downvote/id/<int:id>/cat/<cat>')
def downvote(id,cat):
    if not session.get('logged_in'):
        flash("You are not logged in!")
        return redirect(url_for(cat))

    print id
    print session.get('uid')

    n = Post.query.filter_by(id=id).filter_by(user_id=session.get('uid')).first()
    if not n:
        n = Post(1,None,session.get('uid'),id)
        db.session.add(n)
        db.session.commit()

    flash("Downvotted..!")
    return redirect(url_for(cat))