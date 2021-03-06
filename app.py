
from flask import Flask
from flask_restx import Api
from controller import RecordHandling
from config import ConfigProduction

app=Flask('__name__')
app.config.from_object('config.ConfigProduction')

api=Api(app)

api.add_resource(RecordHandling, '/histogram')

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])
