from . import main
from flask_login import login_required,current_user
from .forms import PitchForm,CommentForm
from flask import render_template,redirect,url_for,abort,request,flash
from ..models import User,Pitch,Comment
from .. import db

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        add_description = pitch_form.add_description.data
        pitch = pitch_form.pitch_content.data
        category = pitch_form.category.data

        # Updated pitch instance
        new_pitch = Pitch(add_description=add_description,content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    
    return render_template('pitch.html',pitch_form = pitch_form )