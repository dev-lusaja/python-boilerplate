import json
from flask import Flask, request
from interface.rest.handlers import owner as owner_handler, health as health_handler
from interface.helpers.format import format_response


class Api:

    def __init__(self):
        self.app = Flask(__name__)
        self.__load_routes()

    def __load_routes(self):
        # Health route
        @self.app.route("/health", methods=['GET'])
        def health():
            rsp, error, message, http_code = health_handler.get()
            return response(rsp, error, message, http_code)

        # Owner routes
        @self.app.route("/owners", methods=['GET', 'POST'])
        def owners():
            if request.method == 'GET':
                rsp, error, message, http_code = owner_handler.get()
            elif request.method == 'POST':
                rsp, error, message, http_code = owner_handler.post(request.json)
            return response(rsp, error, message, http_code)

        @self.app.route("/owners/<string:id>", methods=['GET', 'DELETE'])
        def owner_id(id=None):
            if request.method == 'GET':
                rsp, error, message, http_code = owner_handler.get_by_id(id)
            return response(rsp, error, message, http_code)

        @self.app.route("/owners/<string:id>/actions/<action>", methods=['PUT'])
        def owner_action(id=None, action=None):
            if request.method == 'PUT':
                if action == 'enable':
                    rsp, error, message, http_code = owner_handler.enable(id)
                elif action == 'disable':
                    rsp, error, message, http_code = owner_handler.disable(id)
            return response(rsp, error, message, http_code)

        def response(data, error, message, code):
            return json.dumps(format_response(data=data, error=error, message=message)), code
