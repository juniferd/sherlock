from models import db, CaseFile

def init_db():
    # create db
    db.create_all()
    # create a case file
    first_case = CaseFile(
        title='My First Case',
        description='Let us begin!'
    )
    db.session.add(first_case)
    db.session.commit()


if __name__ == '__main__':
    init_db()