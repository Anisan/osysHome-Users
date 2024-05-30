"""
# Плагин управления пользователями

Упрощает управление учетными записями пользователей. 
Плагин предоставляет администратору полный контроль над пользовательскими данными,
позволяя легко вносить изменения и управлять доступом.   
"""

from app.core.main.BasePlugin import BasePlugin
from app.core.models.Users import User
from plugins.Users.forms.UserForm import UserForm
from plugins.Users.forms.PasswordForm import PasswordForm
from app.core.lib.object import getObjectsByClass, addObject, getObject, deleteObject
from flask import redirect

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
                obj.setProperty("image", form.image.data)
                obj.setProperty("role", form.role.data)
                obj.setProperty("home_page", form.home_page.data)
                return redirect(self.name)
            else:
                return self.render('user.html', {"form":form})
        elif op == 'edit':
            obj = getObject(user_name)
            user = User(obj)
            form = UserForm(obj=user)
            if form.validate_on_submit():
                obj.setProperty("image", form.image.data)
                obj.setProperty("role", form.role.data)
                obj.setProperty("home_page", form.home_page.data)
                return redirect(self.name)
            else:
                return self.render('user.html', {"form":form})
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
        
        users = getObjectsByClass("Users")

        content = {
            'users': users,
        }
        return self.render('users.html', content)
    