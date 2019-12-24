# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# instantiate the app
app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# instantiate db
db = SQLAlchemy(app)

# create model class
class TestTable(db.Model):
    #__tablename__ = 'test_table_custom'
    id = db.Column(db.Integer, primary_key=True)
    string_field = db.Column(db.String(80))
    text_field = db.Column(db.Text)
    date_field = db.Column(db.DateTime)
    float_field = db.Column(db.Float)
    boolean_field = db.Column(db.Boolean)

# index route
@app.route('/')
def index():
    # return 'CRUD with Flask-SQLAlchemy!'

    # pretend this is a submit data
    # string_input = 'Test string'
    # text_input = 'Test text'
    # date_input = datetime.utcnow()
    # float_input = 99.99
    # boolean_input = True

    # new_record = TestTable(string_field=string_input,
    #     text_field=text_input,
    #     date_field=date_input,
    #     float_field=float_input,
    #     boolean_field=boolean_input)
    # db.session.add(new_record)
    # db.session.commit()
    # return 'added!'

    # first_record = TestTable.query.filter_by(id=1).first()
    # return f'{first_record.id} {first_record.string_field} {first_record.date_field} {first_record.float_field} {first_record.boolean_field}'

    # update_record = TestTable.query.filter_by(id=1).first()
    # update_record.string_field = 'Romel updated this string field'
    # update_record.text_field = 'text field has been changed!'
    # update_record.date_field = datetime.utcnow()
    # update_record.float_field = 11.11
    # update_record.boolean_field = False

    # db.session.commit()
    # return 'updated!'

    delete_record = TestTable.query.filter_by(id=1).first()
    db.session.delete(delete_record)
    db.session.commit()
    return 'deleted!'

if __name__ == '__main__':
    app.run(debug=True)