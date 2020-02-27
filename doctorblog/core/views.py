# core/views.py

from flask import render_template,request,Blueprint,flash,send_file
from flask_login import login_user, current_user, logout_user, login_required
from doctorblog.models import Medicine
from flask_qrcode import QRcode

core = Blueprint('core',__name__)


@core.route('/')
def index():
    
    
    page=request.args.get('page',1,type=int)
    posts=Medicine.query.order_by(Medicine.date.desc()).paginate(page=page,per_page=100000)
        
            
    return render_template('index.html',posts=posts)

@core.route('/info')
def info():
    return render_template('info.html')
'''
@core.route("/qrcode",methods=['GET'])
def qrcode():
    data=request.args.get("data",'')
    return send_file(QRcode(data,mode='raw'),mimetype="image/png")
'''