from tedev.app import app

#
if __name__ == "__main__":
    from tedev.core.models.db_initializer import db_drop_and_create_all  # Test model

    db_drop_and_create_all()
    #app.run()