from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from models import CaseFile, Lead
import flask.ext.restless

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(CaseFile, methods=['GET', 'POST', 'DELETE'])


@app.route('/')
def hello_world():
    return render_template('app.html')

@app.route('/casefiles', methods=['GET'])
def get_all_case_files():
    # get all cases from db
    case_files = CaseFile.query.all()
    json_case_files = [case.as_dict() for case in case_files]
    print 'case files %r' % json_case_files
    return jsonify({ 'cases': json_case_files }), 200

@app.route('/seed/casefile', methods=['POST'])
def create_dummy_case_file():
    dummy_case = CaseFile(
        title='The Magically Appearing File',
        description='We are called to investigate a mysterious file',
        status_solved=False
    )
    db.session.add(dummy_case)
    db.session.commit()
    return jsonify({ 'case': 'dummy case'}), 200

if __name__ == '__main__':
    app.run(debug=True)