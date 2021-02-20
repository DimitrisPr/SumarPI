from sumarpi.models import Document
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import Response
import json
import os


def create_app(test_config=None):
    ''' Flask application factory '''

    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        ''' Route for summary retrieval 
        '''
        if request.method == 'GET':
            return render_template('base.html')
        if request.method == 'POST':
            try:
                response = {}
                text = request.form['data']
                document = Document()
                document.generate_summary(text)
                response['document_id'] = document.save()
                return Response(json.dumps(response), status=201, mimetype='application/json')
            except Exception as e:
                print(e)
                return Response(None, status=500)

    @app.route('/summary/<int:document_id>', methods=['GET', 'POST'])
    def summary(document_id):
        ''' Route for summary retrieval 
            Arguments:
                - document_id (str): The id of the document to be retrieved
        '''
        try:
            response = {}
            document = Document()
            summary = document.retrieve_summary(document_id)

            if summary == None:
                return Response(status=404)
            else:
                response['id'] = document_id
                response['summary'] = document.retrieve_summary(document_id)
                return Response(json.dumps(response), status=302, mimetype='application/json')
        except Exception as e:
            return Response(status=500)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
