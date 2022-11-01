from flask import Flask
from flask_restful import Api, Resource, reqparse

from helpers import get_summary

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, location='form', help="Provide text to extract summary.")
parser.add_argument('sentences', type=int, location='form', help="Provide number sentences you want in summary.")


class BertSummary(Resource):
    def get(self):
        return {"message": "Welcome to Bert Summarizer.", "status": 200}

    def post(self):
        args = parser.parse_args()
        print(args)

        if args["text"] != "":
            if args["sentences"]:
                return get_summary(text=args["text"], sentences=args["sentences"])
            else:
                return get_summary(text=args["text"], sentences=3)
        else:
            return {"error": "Text is missing"}


api.add_resource(BertSummary, '/summary')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
