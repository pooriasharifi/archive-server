import os
import sys
from module.respons_str import respons_str
from flask import current_app, make_response, request, Blueprint, send_file
from model.user import User, UserSpase
from flask_jwt_extended import get_jwt_identity, jwt_required
import logging
from werkzeug.utils import secure_filename

sys.path.append('../')
upload_file = Blueprint('upload_file', __name__)


def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path


@upload_file.route('/api/upload-file', methods=['POST', 'GET'])
@jwt_required()
def handle_user_file():
    logging.info('<---------user IpAddress :' + request.remote_addr + '--------->')
    user_model = User.objects(username=get_jwt_identity()).first()
    # print(user_model.pk)
    # print(user_model.user_space[3].perm[0])
    if user_model:
        if request.method == 'POST':
            try:
                file = request.files['file']
                data = dict(request.form)
                if file.filename.split('.')[-1] in current_app.config['AllOWED_EXTENSIONS_FILE']:
                    path = os.path.join('user-file/' + str(user_model.username) + '/')

                    if data['path'] is None:

                        os.makedirs(path, exist_ok=True)
                        file_name = secure_filename(file.filename)
                        ma = path.replace('', '') + uniquify(file_name)
                        a = uniquify(ma)
                        print(a)
                        if len(user_model.user_space) == 0:
                            user_model.user_space.append(UserSpase(
                                title=data['title'],
                                file=a,
                                perm=data['perm']
                            ))
                            user_model.save()
                            file.save(os.path.join(a))
                        else:
                            for i in user_model.user_space:
                                if i.title == data['title']:
                                    return make_response(respons_str('duplicate_title', None), 400)
                            user_model.user_space.append(UserSpase(
                                title=data['title'],
                                file=a,
                                perm=data['perm']

                            ))

                            user_model.save()
                            file.save(os.path.join(a))
                            return make_response(respons_str('upload_succes', None), 200)
                    else:

                        new_path = path + data['path'] + '/'
                        os.makedirs(new_path, exist_ok=True)
                        file_name = secure_filename(file.filename)
                        ma = new_path.replace('', '') + uniquify(file_name)
                        a = uniquify(ma)
                        print(a)
                        if len(user_model.user_space) == 0:
                            user_model.user_space.append(UserSpase(
                                title=data['title'],
                                file=a,
                                # perm=data['perm']

                            ))
                            user_model.save()
                            file.save(os.path.join(a))
                        else:
                            for i in user_model.user_space:
                                if i.title == data['title']:
                                    return make_response(respons_str('duplicate_title', None), 400)
                            user_model.user_space.append(UserSpase(
                                title=data['title'],
                                file=a,
                                perm=[user_model.pk]

                            ))
                            user_model.save()
                            file.save(os.path.join(a))
                            return make_response(respons_str('upload_succes', None), 200)

                return make_response(respons_str('file_type_not_allowed', None), 404)
            except KeyError as err:
                if 'title' in str(err):
                    return make_response(respons_str('title_required', None), 400)
                else:
                    print('<--------------------key error-------------------->')
                    return make_response(respons_str('internal_server_error', None), 500)
            except OSError as err:
                print('<--------------------OS error-------------------->')
                return make_response(respons_str('internal_server_error', err), 500)

    else:
        return make_response(respons_str('incorrect_username_or_password', None), 404)


@upload_file.route('/api/fetch-rout', methods=['POST'])
@jwt_required()
def get_rout():
    try:
        logging.info('<---------user IpAddress :' + request.remote_addr + '--------->')
        user_model = User.objects(username=get_jwt_identity()).first()

        if user_model:
            ctx = request.json
            temp = []
            print(ctx)

            path = os.path.join('user-file/' + str(user_model.username) + '/')

            if ctx['path'] is None:

                content = os.listdir(path)
                for i in content:
                    if '.' not in i:
                        temp.append(i)
            else:

                content = os.listdir(path + ctx['path'])
                for i in content:
                    if '.' not in i:
                        temp.append(i)
            return make_response(respons_str('wait', temp), 200)
        else:
            return make_response(respons_str('incorrect_username_or_password', None), 404)
    except KeyError as err:
        if 'path' in str(err):
            return make_response(respons_str('title_required', None), 400)
        else:
            print('<--------------------key error-------------------->')
            return make_response(respons_str('internal_server_error', None), 500)
    except OSError as err:


        print('<--------------------OS error-------------------->')
        return make_response(respons_str('internal_server_error', err), 500)


@upload_file.route('/api/new-dir', methods=['POST'])
@jwt_required()
def new_folder():
    try:
        logging.info('<---------user IpAddress :' + request.remote_addr + '--------->')
        user_model = User.objects(username=get_jwt_identity()).first()
        if user_model:
            ctx = request.json

            path = os.path.join('user-file/' + str(user_model.username) + '/' + ctx['path'])
            print(path)
            os.makedirs(path, exist_ok=True)
            return make_response(respons_str('succes', None), 200)
        else:
            return make_response(respons_str('incorrect_username_or_password', None), 404)
    except KeyError as err:
        if 'path' in str(err):
            return make_response(respons_str('title_required', None), 400)
        else:
            print('<--------------------key error-------------------->')
            return make_response(respons_str('internal_server_error', None), 500)
    except OSError as err:
        print('<--------------------OS error-------------------->')
        return make_response(respons_str('internal_server_error', err), 500)


@upload_file.route('/api/fetch-rr', methods=['POST'])
@jwt_required()
def get_file():
    try:
        logging.info('<---------user IpAddress :' + request.remote_addr + '--------->')
        user_model = User.objects(username=get_jwt_identity()).first()
        print(len(user_model.user_space))
        if not (user_model.user_space is  None) :
            # print(len(user_model.user_space) is None or len(user_model.user_space) > 0)

            if user_model:
                ctx = request.json
                print(ctx['path'])
                temp = []
                path = os.path.join('user-file/' + str(user_model.username) + '/')
                if None is ctx['path']:
                    content = os.listdir(path)
                    for i in content:
                        if '.' in i:
                            for item in user_model.user_space:
                                if i in item.file:
                                    res = dict(
                                        title=item.title,
                                        path=item.file,
                                        date=item._created_at,
                                    )
                                    temp.append(res)
                else:

                    content = os.listdir(path + ctx['path'])
                    for i in content:
                        if '.' in i:
                            for item in user_model.user_space:
                                if i in item.file:
                                    res = {'title': item.title, 'path': item.file, 'date': item._created_at}
                                    temp.append(res)

                return make_response(respons_str('wait', temp), 200)
            else:
                return make_response(respons_str('incorrect_username_or_password', None), 404)
        else:
            return make_response(respons_str('no_content', None), 204)
    except KeyError as err:
        if 'path' in str(err):
            return make_response(respons_str('title_required', None), 400)
        else:
            print('<--------------------key error-------------------->')
            return make_response(respons_str('internal_server_error', None), 500)
    except OSError as err:
        if len(user_model.user_space) is None or len(user_model.user_space) == 0:
            print('skdjvnskvjnskvdjn')
        print('------------------------------------------')
        print('<--------------------OS error-------------------->')
        return make_response(respons_str('internal_server_error', err), 500)


@upload_file.route('/api/download-file', methods=['GET'])
@jwt_required()
def download_file():
    try:
        logging.info('<---------user IpAddress :' + request.remote_addr + '--------->')
        user_model = User.objects(username=get_jwt_identity()).first()
        if user_model:
            ctx = request.headers['path']
            return send_file(ctx, as_attachment=True)
        else:
            return make_response(respons_str('incorrect_username_or_password', None), 404)
    # except KeyError as err:
    #     if 'path' in str(err):
    #         return make_response(respons_str('title_required', None), 400)
    #     else:
    #         print('<--------------------key error-------------------->')
    #         return make_response(respons_str('internal_server_error', None), 500)
    except OSError as err:
        print('<--------------------OS error-------------------->')
        return make_response(respons_str('internal_server_error', err), 500)
