#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask import render_template
from flask import jsonify
import MySQLdb
from xml.sax.saxutils import escape

db = MySQLdb.connect(host='localhost', user='root', passwd='12345',
                     db='newshunt')


from chat import talk

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('documentation.html', title='Documentation')


@app.route('/api/msg/', methods=['GET'])
@app.route('/api/msg/<msg>', methods=['GET'])
def talk_to_bot(msg='no input'):
    message = ' '.join(msg.split('+'))

    # message = "what are you"

    bot_response = talk(message)

    cur = db.cursor()
    h = bot_response.lower().strip()
    cur.execute("SELECT * FROM news WHERE category='"+h+"'")

    rows = cur.fetchall()
    # checking if a matched response is found.

    news_output = {}
    news_list = []
    news_final_output = {}
    for r in rows:

    if not bot_response:
        bot_response = 'error'
    return jsonify(news_final_output)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

			
