from flask import render_template, request, abort
from tcidatabase.models import SurveyToken, Score
from tcidata import get_tci
from tcii18n.translator import Translator
from tcii18n.template import flask_methods

from . import app
from app import get_translations_files


@app.route('/')
def home():
    return render_template('error.html'), 401


@app.route('/<string:token>')
def language(token):
    try:
        token = SurveyToken.objects.get(key=token, usage_date=None)
    except SurveyToken.DoesNotExist:
        return render_template('error.html'), 401
    return render_template('language.html', token=token)


@app.route('/<string:language>/<string:token>')
def survey(language, token):
    try:
        translator = Translator(get_translations_files(language))
        token = SurveyToken.objects.get(key=token, usage_date=None)
    except SurveyToken.DoesNotExist:
        return render_template('error.html'), 401
    try:
        tci = get_tci(token.survey)
    except NotImplementedError:
        abort(501, 'The token has a inexisting "{}" survey associated.'.format(
              token.survey))
    questions = tci.get('questions')
    return render_template('survey.html', questions=questions, token=token,
                           trans=translator.translate)


@app.route('/end', methods=['post'])
def end():
    token = SurveyToken.objects.get(key=request.form.get('token'))
    answers = [int(a) for a in request.form.get('answers').split(',')]
    times = [int(t) for t in request.form.get('times').split(',')]
    Score(client=token.client, answers=answers, times=times,
          survey=token.survey).save()
    token.void()
    return render_template('end.html')
