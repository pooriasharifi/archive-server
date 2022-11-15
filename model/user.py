import datetime
from mongoengine import Document,StringField,IntField,DateField,EmailField,EmbeddedDocument,EmbeddedDocumentField,ListField,DateTimeField



class UserSpase(EmbeddedDocument):
    title=StringField()
    file=StringField()
    perm=ListField()
    _created_at=DateTimeField(default=lambda: datetime.datetime.now())



class Trash(EmbeddedDocument):
    title=StringField()
    file=StringField()
    _created_at=DateTimeField(default=lambda: datetime.datetime.now())







class User(Document):
    name=StringField(required=True)
    last_name=StringField(required=True)
    father_name=StringField(required=True)
    nationalـcode=IntField(required=True,unique=True)
    birthـcertificate_code=IntField(required=True,unique=True)
    birth_date=DateField(required=True)
    birth_certificate_serial_number=StringField(required=True)
    phone=IntField(required=True,unique=True)
    mobile=IntField(required=True,unique=True)
    insurance_number=IntField(required=True,unique=True)
    address=StringField(required=True)
    birthـcertificate_date=DateField(required=False)
    birthـcertificate_location=StringField(required=False)
    placeـofـIssue=StringField(required=False)
    recruitmentـcode=IntField(required=True,unique=True)
    education=StringField(required=False)
    last_educational_certificate=StringField(required=False)
    major=StringField(required=False)
    military_service_situation=StringField()
    username=StringField(required=True,unique=True)
    password=StringField(required=True)
    level=IntField(default=1)
    company_identification_email=EmailField(required=True,unique=True)
    user_space=ListField(EmbeddedDocumentField(UserSpase))
    trash=ListField(EmbeddedDocumentField(Trash))