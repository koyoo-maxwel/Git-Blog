from flask import Flask
from . import main
from flask import render_template,redirect,url_for,abort,request
from flask_login import login_required
#from .forms import ReviewForm,UpdateProfile
from .. import db,photos
from .forms import BlogForm,CommentForm,BusinessForm,HealthForm,TechForm
from ..models import  User, Blog , Comment
from .forms import UpdateProfile







# views
@main.route("/")
def index():
    '''
    title = "blog || blog it here"
    '''
    title = 'blog || pich it here'
    blogs = Blog.query.all()

    return render_template('index.html', title= title, blogs = blogs,)

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

        return redirect(url_for('main.index'))

        
    return redirect(url_for('main.profile',uname=uname))  

@main.route('/blog',methods = ['GET','POST'])
@login_required
def MyBlog():
    form =BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog=form.blog.data,body=form.body.data,category=form.category.data)
        blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('blog.html', form=form)


@main.route('/comment',methods = ['GET','POST'])
@login_required
def comment():
    form =CommentForm()
    if form.validate_on_submit():
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('category.html')
    

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


@main.route('/Business',methods = ['GET','POST'])
@login_required
def Business():
    form =BusinessForm()
    if form.validate_on_submit():
        db.session.add(Business)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('Business.html',form = form)


@main.route('/Tech',methods = ['GET','POST'])
@login_required
def Tech():
    form =TechForm()
    if form.validate_on_submit():
        db.session.add(Tech)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('Tech.html',form = form)


@main.route('/Health',methods = ['GET','POST'])
@login_required
def Health():
    form =HealthForm()
    if form.validate_on_submit():
        db.session.add(Health)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('Health.html',form = form)


    
     