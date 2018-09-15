from flask_wtf import FlaskForm
from wtforms import  StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
   title = StringField('MinutePitch title',validators=[Required()])
   content = StringField('content',validators=[Required()])
   category = SelectField('Category', choices=[('Choose Category', 'Choose Category'),('business', 'business pitch'),('Interview Pitch', 'Interview Pitch'),('Political Pitch', 'Political Pitch')])
   review = TextAreaField('pitch review', validators=[Required()])
   submit = SubmitField('Submit')



class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[Required()])
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')
