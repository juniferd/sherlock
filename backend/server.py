from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from models import CaseFile, Lead, Clue, app, db
from random import randint
import flask_restless

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# APIs here
manager.create_api(CaseFile, methods=['GET', 'POST', 'DELETE', 'PUT'])
manager.create_api(Lead, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Clue, methods=['GET', 'POST', 'DELETE', 'PUT'])

@app.route('/')
def hello_world():
    return render_template('app.html')

@app.route('/case/<int:id>')
def show_case(id):
    return render_template('app.html')

@app.route('/timeline')
def show_timeline():
    return render_template('app.html')

@app.route('/leads')
def show_leads():
    return render_template('app.html')

@app.route('/seed/casefile', methods=['POST'])
def create_dummy_case_file():
    dummy_case = CaseFile(
        title='The Magically Appearing File %s' % randint(1, 100),
        description='We are called to investigate %s mysterious files' % randint(2, 100),
        status_solved=False
    )
    db.session.add(dummy_case)
    db.session.commit()
    return jsonify({ 'case': dummy_case.title }), 200

if __name__ == '__main__':
    app.run(debug=True)