#/bin/bash

from flask import Flask, render_template
from tcidatabase import db
from tcidatabase.models import *


def create_token():
    db.connect(db='tci_test', username='', password='', host='localhost',
               port=27017)

    database = db.connection.get_connection()
    database.drop_database('tci_test')
    user = User().save()
    token = SurveyToken(survey="tcims", client=Client(lastname='Mochet',
                                                      provider=user).save(),
                        provider=user).save()
    print(token.key)
    return token.key

create_token()
