from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient


class API():

    app = Flask('vegas_events')

    #Give our server an easy way to reference Mongo in each function
    mongo = MongoClient()

    def __init__(self):
        pass

    # API endpoint that parses date string and queries mongo
    @staticmethod
    @app.route('/api/<string:date>', methods=['GET'])
    def get_event(date):
        events = API.mongo.event_db['event_collection']
        doc = events.find_one({'_id':date})
        if not doc:
            doc = {
              'message': "{} not found".format(date)
            }
        return jsonify(doc)


    # error handling
    @staticmethod
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    # Running the flask server
    def run(self,debug=True,port=5000):
        self.app.run(host="0.0.0.0",port=port, debug=debug,threaded=True)


ab = API()
ab.run(True)


