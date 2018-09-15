from flask import Flask
from . import main
from flask import render_template,redirect,url_for,abort,request
from flask_login import login_required
#from .forms import ReviewForm,UpdateProfile
from .. import db,photos
from .forms import PitchForm
from ..models import  User, Pitch , Comment
from .forms import UpdateProfile




app = Flask(__name__)


# views
@main.route("/")
@login_required
def index():
    '''
    title = "pitch || pitch it here"
    '''
    title = 'pitch || pich it here'
    pitches = Pitch.query.all()

    return render_template('index.html', title= title, pitches = pitches)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

        
    return redirect(url_for('main.profile',uname=uname))  

@main.route('/Pitch',methods = ['GET','POST'])
@login_required
def MyPitch():
    form =PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(post=form.post.data,body=form.body.data,category=form.category.data)
        pitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('pitch.html', form=form)


@main.route('/comment',methods = ['GET','POST'])
@login_required
def comment():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'pitch ||Comment'

    return render_template('comment.html', title = title )



@main.route('/pitch',methods = ['GET','POST'])
@login_required
def pitch():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'pitch ||pitch'
    return render_template('pitch.html', title = title )




@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


    
     