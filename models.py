from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import DateTimeField, EmbeddedDocumentField, ListField, StringField, EmailField


class Email(EmbeddedDocument):
    data = EmailField(default=None)


class Phone(EmbeddedDocument):
    data = StringField(default=None)


class AddressBook(Document):
    name = StringField()
    address = StringField(default=None)
    birthday = DateTimeField(default=None)
    phone = ListField(EmbeddedDocumentField(Phone))
    email = ListField(EmbeddedDocumentField(Email))
    meta = {'allow_inheritance': True}