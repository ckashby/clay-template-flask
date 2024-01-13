from flask import Flask, jsonify, request
from soffos.service.exceptions import ServiceException, InternalServerErrorException
from service import ExampleService

import traceback
import settings

app = Flask(__name__)
service = ExampleService()

@app.errorhandler(ServiceException)
def handle_service_exception(ex):
    response = jsonify(ex.to_response())
    response.status_code = ex.status_code
    return response

@app.errorhandler(Exception)
def handle_unknown_exception(ex):
    trace = traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)
    error =  InternalServerErrorException(
        service=settings.SERVICE,
        message=' '.join(ex.args),
        details=''.join(trace)
    )
    response = jsonify(error.to_response())
    response.status_code = error.status_code
    return response

@app.route('/', methods=['POST'])
def service_endpoint():
    """Service endpoint"""
    data = service.Data(**request.json)
    return jsonify(service.run(data))
