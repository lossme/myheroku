from flask_restful import Resource


class App(Resource):

    def get(self):
        return 'hello'
