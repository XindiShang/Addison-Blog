from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, EqualTo
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("标题", validators=[DataRequired()])
    subtitle = StringField("副标题", validators=[DataRequired()])
    img_url = StringField("图片链接", validators=[DataRequired(), URL()])
    body = CKEditorField("内容", validators=[DataRequired()])
    submit = SubmitField("发布")


class RegisterForm(FlaskForm):
    email = StringField("邮箱", validators=[DataRequired()])
    name = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired(), EqualTo("confirm", message="Password must match")])
    confirm = PasswordField("确认密码")
    submit = SubmitField("注册")


class LoginForm(FlaskForm):
    email = StringField("邮箱", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField("登录")


class CommentForm(FlaskForm):
    comment = CKEditorField("评论", validators=[DataRequired()])
    submit = SubmitField("发布评论")