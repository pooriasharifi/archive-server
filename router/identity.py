import sys
from flask import make_response,Blueprint,request
from model.user import User
from module.password import check_encrypted_password,encrypt_password
from module.respons_str import respons_str
from flask_jwt_extended import create_access_token, get_jwt_identity,jwt_required
import logging
from mongoengine import errors
import os

sys.path.append('../')


user=Blueprint('user',__name__)


def signin():
    content = request.json
    try:
        user_model=User.objects(username=content['username'].lower()).first()
        if user_model:
            if check_encrypted_password(content['password'],user_model.password):
                access_token=create_access_token(identity=user_model.username,fresh=True)
                return make_response(respons_str('logged',{'access_token': access_token}), 200)
        return make_response(respons_str('incorrect_username_or_password', None), 404)
    except OSError as err:
        return make_response(respons_str('internal_server_error', err), 500)



@jwt_required()
def update_user():
    content = request.json
    try:
        user_model=User.objects(username=get_jwt_identity()).first()
        user_model.update(
            set__username=content['username']
        )
        return make_response(respons_str('updated', None), 200)
    except OSError as err:
        return make_response(respons_str('internal_server_error', err), 500)
    




@jwt_required()
def remove_user():
    user_model=User.objects(username=get_jwt_identity()).first()
    try:
        if user_model:
            user_model.delete()
            return make_response(respons_str('deleted', None), 200)
        return make_response(respons_str('user_not_found', None), 404)
    except OSError as err:
        return make_response(respons_str('internal_server_error', err), 500)
    

image_format=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'ico']


@jwt_required()
def profile():
    user_model = User.objects(username=get_jwt_identity()).first()
    try:
        if user_model:
            res=[]
            res.append(
                dict(
                    name=user_model.name,
                    username=user_model.username,
                    last_name=user_model['last_name'],
                    father_name=user_model['father_name'],
                    national??code=user_model['national??code'],
                    birth??certificate_code=user_model['birth??certificate_code'],
                    birth_date=user_model['birth_date'],
                    birth_certificate_serial_number=user_model['birth_certificate_serial_number'],
                    phone=user_model['phone'],
                    mobile=user_model['mobile'],
                    insurance_number=user_model['insurance_number'],
                    address=user_model['address'],
                    birth??certificate_date=user_model['birth??certificate_date'] if user_model['birth??certificate_date']!=None else '?????????????? ?????? ????????',
                    birth??certificate_location=user_model['birth??certificate_location'] if user_model['birth??certificate_location']!=None else  '?????????????? ?????? ????????',
                    place??of??Issue=user_model['place??of??Issue']if user_model['place??of??Issue']!=None else  '?????????????? ?????? ????????',
                    recruitment??code=user_model['recruitment??code'],
                    education=user_model['education']if user_model['education']!=None else  '?????????????? ?????? ????????',
                    last_educational_certificate=user_model['last_educational_certificate']if user_model['last_educational_certificate']!=None else  '?????????????? ?????? ????????',
                    major=user_model['major']if user_model['major']!=None else  '?????????????? ?????? ????????',
                    military_service_situation=user_model['military_service_situation']if user_model['military_service_situation']!=None else  '?????????????? ?????? ????????',
                    level=user_model['level'],
                    company_identification_email=user_model['company_identification_email'],
                )
            )
            return make_response(respons_str('wait', res), 200)
        return make_response(respons_str('user_not_found', None), 404)
    except OSError as err:
        return make_response(respons_str('internal_server_error', err), 500)


@user.route('/api/signup',methods=['POST'])
def register_user():
    logging.info('<---------user IpAddress :' + request.remote_addr + '--------->')
    try:
        content = request.json
        user_model=User(
            username=content['username'].lower(),
            password=encrypt_password(content['password']),
            company_identification_email=content['company_identification_email'],
            name=content['name'],
            last_name=content['last_name'],
            father_name=content['father_name'],
            national??code=content['national??code'],
            birth??certificate_code=content['birth??certificate_code'],
            birth_date=content['birth_date'],
            birth_certificate_serial_number=content['birth_certificate_serial_number'],
            phone=content['phone'],
            mobile=content['mobile'],
            insurance_number=content['insurance_number'],
            address=content['address'],
            recruitment??code=content['recruitment??code'],
        ).save()
        return make_response(respons_str('registered', None), 201)
    except errors.ValidationError as err:
        if 'Invalid email address' in err.message:
            return make_response(respons_str('invalid_email_address', None), 400)
        else:
            print('<----------------------validation error------------------------>')
            return make_response('internal_sever_error', None, 500)
    except errors.NotUniqueError as err:
        if "username" in str(err):
            return make_response(respons_str('duplicate_username', None), 400)
        elif "company_identification_email" in str(err):
            return make_response(respons_str('duplicate_company_identification_email',None),400)
        elif "national??code" in str(err):
            return make_response(respons_str('duplicate_national??code',None),400)
        elif "birth??certificate_code" in str(err):
            return make_response(respons_str('duplicate_birth??certificate_code',None),400)
        elif "phone" in str(err):
            return make_response(respons_str('duplicate_phone',None),400)
        elif "mobile" in str(err):
            return make_response(respons_str('duplicate_mobile',None),400)
        elif "insurance_number" in str(err):
            return make_response(respons_str('dulpicate_insurance_number',None),400)
        elif "recruitment??code" in str(err):
            return make_response(respons_str('dulpicate_recruitment??code',None),400)
        else:
            print('<----------------------not unique error------------------------>')
            return make_response(respons_str('internal_server_error', str(err)), 500)
    except KeyError as err:
        if "username" in str(err):
            return make_response(respons_str('username_required', None), 400)
        elif "password" in str(err):
            return make_response(respons_str('password_required', None), 400)
        elif "company_identification_email" in str(err):
            return make_response(respons_str('company_identification_email_required', None), 400)
        elif "name" in str(err):
            return make_response(respons_str('name_required', None), 404)
        elif "last_name" in str(err):
            return make_response(respons_str('last_name_required', None), 400)
        elif "father_name" in str(err):
            return make_response(respons_str('father_name_required', None), 400)
        elif "national??code" in str(err):
            return make_response(respons_str('national??code_required', None), 400)
        elif "birth??certificate_code" in str(err):
            return make_response(respons_str('birth??certificate_code_required', None), 400)
        elif "birth_date" in str(err):
            return make_response(respons_str('birth_date_required', None), 400)
        elif "birth_certificate_serial_number" in str(err):
            return make_response(respons_str('birth_certificate_serial_number??required', None), 400)
        elif "phone" in str(err):
            return make_response(respons_str('phone_required', None), 400)
        elif "mobile" in str(err):
            return make_response(respons_str('mobile_required', None), 400)
        elif "insurance_number" in str(err):
            return make_response(respons_str('insurance_number_required', None), 400)
        elif "recruitment??code" in str(err):
            return make_response(respons_str('recruitment??code_required', None), 400)
        elif "address" in str(err):
            return make_response(respons_str('address_required', None), 400)
        else:
            print('<----------------------key error------------------------>')  
            return make_response(respons_str('internal_server_error', None), 500)
    except OSError as err:
        print('<----------------------OS error------------------------>')
        return make_response(respons_str('internal_server_error', err), 500)
    
    
@user.route('/api/user',methods=['GET','POST','PUT','DELETE'])
def handle_user():
    logging.info('<---------user IpAddress :' + request.remote_addr + '--------->')

    if request.method=='POST':
        return signin()
    elif request.method=="GET":
        return profile()
    elif request.method=="PUT":
        return update_user()
    elif request.method=="DELETE":
        return remove_user()
    
    
    
@user.route('/api/avatar',methods=['GET','POST'])
@jwt_required()
def user_avatar():
    if request.method=="POST":
        file = request.files['file']
        try:
            user_model=User.objects(username=get_jwt_identity()).first()
            if user_model:
                if file.filename.split('.')[1].lower() in image_format:
                    path=os.path.join("uploads_file/avatar/"+user_model.username)
                    os.makedirs(path,exist_ok=True)
                    file.save(os.path.join(path,file.filename))
                    
                    return make_response(respons_str('updated', None), 200)

        except OSError as err:
            return make_response(respons_str('internal_server_error', err), 500)