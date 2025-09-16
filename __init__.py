"""
# Плагин управления пользователями

Упрощает управление учетными записями пользователей. 
Плагин предоставляет администратору полный контроль над пользовательскими данными,
позволяя легко вносить изменения и управлять доступом.   
"""

import os
from app.configuration import Config
from app.core.main.BasePlugin import BasePlugin
from app.core.models.Users import User
from app.core.lib.object import setProperty
from plugins.Users.forms.UserForm import UserForm
from plugins.Users.forms.PasswordForm import PasswordForm
from app.core.lib.object import getObjectsByClass, addObject, getObject, deleteObject
from flask import redirect, jsonify

class Users(BasePlugin):

    def __init__(self,app):
        super().__init__(app,__name__)
        self.title = "Users"
        self.description = """This is a plugin edit users"""
        self.version = "0.3"
        self.category = "System"

    def initialization(self):
        pass

    def admin(self, request):
        op = request.args.get("op",None)
        user_name = request.args.get("user",None)
        if op == 'add':
            form = UserForm()
            if form.validate_on_submit():
                obj = addObject(form.username.data, "Users")
                obj.setProperty("role", form.role.data)
                obj.setProperty("home_page", form.home_page.data)
                obj.setProperty("apikey", form.apikey.data)
                obj.setProperty("timezone", form.timezone.data)
                return redirect(self.name)
            else:
                return self.render('user.html', {"form":form, "lastLogin": "..."})
        elif op == 'edit':
            obj = getObject(user_name)
            user = User(obj)
            form = UserForm(obj=user)
            if form.validate_on_submit():
                obj.setProperty("role", form.role.data)
                obj.setProperty("home_page", form.home_page.data)
                obj.setProperty("apikey", form.apikey.data)
                obj.setProperty("timezone", form.timezone.data)
                return redirect(self.name)
            else:
                return self.render('user.html', {"form":form, "lastLogin": obj.getProperty("lastLogin")})
        elif op == 'delete':
            deleteObject(user_name)
            return redirect(self.name)
        elif op == 'setPassword':
            formPass = PasswordForm()
            if formPass.validate_on_submit() and formPass.password.data == formPass.repeat_password.data:
                obj = getObject(user_name)
                user = User(obj)
                user.set_password(formPass.password.data)
                obj.setProperty("password", user.password)
                return redirect('/')
            else:
                return self.render('password.html', {"form":formPass})
        elif op == 'upload_image':
            if 'file' not in request.files:
                return jsonify({'error': 'No file part'})

            file = request.files['file']
            if file.filename == '':
                return jsonify({'error': 'No selected file'})

            user = request.form.get('user', '')

            dir = os.path.join(Config.FILES_DIR,"private","avatars")
            os.makedirs(dir, exist_ok=True)
            filepath = os.path.join(dir, file.filename)
            file.save(filepath)
            url_image = "/files/private/avatars/" + file.filename
            setProperty(user + ".image", url_image)

            return jsonify({'url': url_image})

        users = getObjectsByClass("Users")

        content = {
            'users': users,
        }
        return self.render('users.html', content)
