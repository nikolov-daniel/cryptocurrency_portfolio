from cryptocurrency import db


def save_data(data):

    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise


def delete_data(data):

    try:
        db.session.delete(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise


def flush_and_commit_changes():

    try:
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        raise


def rollback_and_close():

    try:
        db.session.rollback()
        db.session.close()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()

