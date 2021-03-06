from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, RadioField, DateTimeField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import EmailField, DateField


class CertificateForm(FlaskForm):
    
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    scoreForTrueFalse = IntegerField("Score For True False", validators=[DataRequired(), NumberRange(min=0)] ) 
    scoreForSimpleSelection = IntegerField("Score For Simple Selection", validators=[DataRequired(), NumberRange(min=0)] )
    numQuestions = IntegerField("numQuestions", validators=[DataRequired(), NumberRange(min=0)] )
    timeForTest = StringField("timeForTest", validators=[DataRequired(), NumberRange(min=0)] )
    submit = SubmitField('Save Changes')
    

class QuestionTFForm(FlaskForm):

    description = TextAreaField("Description", validators=[DataRequired()])

    submit = SubmitField('Save Changes')

class QuestionCreateForm(FlaskForm):
    
    certificate = StringField("Certificate", validators=[DataRequired()])
    question = StringField("Question", validators=[DataRequired()])
    typeQuestion = RadioField("Type", choices=[("TrueFalse", "TrueFalse"), ("Simple Selection", "Simple Selection")] ,validators=[DataRequired()])
    routeImg = StringField("Image route")
    code = StringField("Code")
    opcionCorrect = StringField("Answer", validators=[DataRequired()])
    opcion2 = StringField("Second option", validators=[DataRequired()])
    opcion3 = StringField("Third option")
    opcion4 = StringField("Fourth option")
    submit = SubmitField("Save")

# class Question4