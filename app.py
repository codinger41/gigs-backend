import os
from flask import Flask
from flask_graphql import GraphQLView
from api.gigs.schema import schema
from mongoengine import connect
from settings import settings

app = Flask(__name__)
app.config.from_object(settings)
app.add_url_rule(
	'/graphql',
	view_func=GraphQLView.as_view(
		'graphql',
		schema=schema,
		graphiql=True
	)
)

if __name__ == '__main__':
    connect(host=settings.MONGODB_URL, alias='default')
    app.run()
