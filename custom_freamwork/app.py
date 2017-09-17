import Tyrion
import tornado.web
import tornado.ioloop



Tyrion.setup('tornado')

from Tyrion.Forms import Form
from Tyrion.Fields import StringField,IntegerField
from Tyrion.Fields import EmailField
from Tyrion.Widget import InputPassword,InputMultiCheckBox,InputRadio,SingleSelect,InputSingleCheckBox,TextArea

class LoginForm(Form):
    username=StringField(error={'required':'不能为空'})
    password=StringField(error={'required':'密码不能为空'},widget=InputPassword())
    email=EmailField(error={'required':'邮箱不能为空','invalid':'邮箱格式错误'})
   

class LoginHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        print(*args,)
        form=LoginForm(self)
        self.render('login.html',form=form)

    def post(self,*args,**kwargs):
        form=LoginForm(self)

        if form.is_valid():
            print(form.error_dict)
            self.render('index.html',)
        else:
            print(form.value_dict)

        self.render('login.html',form=form) #


class Register(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        form=RegisterForm(self)
        self.render('register.html',form=form)
    def post(self,*args,**kwargs):
        form=RegisterForm(self)
        if form.is_valid():
            self.render('register.html')



class RegisterForm(tornado.web.RequestHandler):
    class RegisterForm(Form):
        username = StringField(max_length=32,
                               min_length=6,
                               error={'required': '用户名不能为空',
                                      'min_length': '用户名不能少于6位',
                                      'max_length': '用户名不能超过32位'})

        password = StringField(max_length=32,
                               min_length=6,
                               error={'required': '密码不能为空'},
                               widget=InputPassword())

        gender = IntegerField(error={'required': '请选择性别',
                                     'invalid': '性别必须为数字'},
                              widget=InputRadio(text_value_list=[{'value': 1, 'text': '男', },
                                                                 {'value': 2, 'text': '女', }],
                                                checked_value=2))

        age = IntegerField(max_value=500,
                           min_value=0,
                           error={'required': '年龄不能为空',
                                  'invalid': '年龄必须为数字',
                                  'min_value': '年龄不能小于0',
                                  'max_value': '年龄不能大于500'})

        email = EmailField(error={'required': '邮箱不能为空',
                                  'invalid': '邮箱格式错误'})

        city = IntegerField(error={'required': '城市选项不能为空', 'invalid': '城市选项必须为数字'},
                            widget=SingleSelect(text_value_list=[{'value': 1, 'text': '上海'},
                                                                 {'value': 2, 'text': '北京'},
                                                                 {'value': 3, 'text': '广州'}])
                            )
        protocol = IntegerField(error={'required': '请选择协议', 'invalid': '协议格式错误'},
                                widget=InputSingleCheckBox(attr={'value': 1}))

        memo = StringField(required=False,
                           max_length=150,
                           error={'invalid': '备注格式错误', 'max_length': '备注最大长度为150字'},
                           widget=TextArea())


setting={
    'template_path':'template',
}


applicaton=tornado.web.Application(
    [
        (r'/login',LoginHandler),
        (r'/register',Register),

    ],**setting)

if __name__ == '__main__':
    applicaton.listen(8888)
    tornado.ioloop.IOLoop.instance().start()















