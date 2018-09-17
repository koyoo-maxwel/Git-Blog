from flask_wtf import FlaskForm
from wtforms import  StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    blog = StringField('Your name',validators=[Required()])
    body = TextAreaField('blog')
    category = SelectField('category', choices=[('choose', 'choose'),('business', 'business blog'),('Tech blog', 'Tech blog'),
    ('Health blog', 'Health blog')])
    submit = SubmitField('blog')

class CommentForm(FlaskForm):

    post = StringField('Comment title',validators=[Required()])
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')


class BusinessForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('blog')
    submit = SubmitField('blog')



class TechForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('blog')
    submit = SubmitField('blog')
    


class HealthForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('blog')
    submit = SubmitField('blog')
    
