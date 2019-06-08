from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
	DateTimeField,
	StringField
)


class Gig(Document):
    meta = {"db_alias":"default", "collection": "gigs"}
    title = StringField()
    price = StringField()
    description = StringField()
    created_at = DateTimeField(default=datetime.now)
    contact_phone = StringField()
    contact_email = StringField()
    contact_name = StringField()
    location = StringField()
