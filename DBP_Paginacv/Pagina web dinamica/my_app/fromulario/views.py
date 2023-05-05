from flask import Blueprint, render_template, request

login = Blueprint('login', __name__)

def upload_image():
    image = request.files['myImage']
    return {image.filename}


@login.route('/')
def inicio():
    return render_template('login.html')

@login.route('/login',methods=['POST'])
def usuario():
    data = {
        #Datos de usuario
        'email' : request.form['email'],
        'pswr' : request.form["pswr"],
        #Prensentacion y datos
        'myImage' : request.files['myImage'],
        'name' : request.form["name"],
        'apellidos' : request.form["apellidos"],
        'dni' : request.form["dni"],
        'presentacion' : request.form["presentacion"],
        #Formas de contacto
        'nmr' : request.form["nmr"],
        'cod_pos' : request.form["cod_pos"],
        'fb' : request.form["fb"],
        'ig' : request.form["ig"],
        'lkdn' : request.form["lkdn"],
        #Habilidades
        'skill1' : request.form["skill1"],
        'skill2' : request.form["skill2"],
        'skill3' : request.form["skill3"],
        'skill4' : request.form["skill4"],
        'skill5' : request.form["skill5"],
        #Experiencia laboral
        'work1' : request.form["work1"],
        'work2' : request.form["work2"],
        'work3' : request.form["work3"],
        #Experiencias laborales
        'workexp1_1' : request.form["workexp1_1"],
        'workexp1_2' : request.form["workexp1_2"],
        'workexp1_3' : request.form["workexp1_3"],
        'workexp2_1' : request.form["workexp2_1"],
        'workexp2_2' : request.form["workexp2_3"],
        'workexp3_1' : request.form["workexp3_1"],
        'workexp3_2' : request.form["workexp3_2"],
        'workexp3_3' : request.form["workexp3_3"],

        #Estudios 
        'sec' : request.form["sec"],
        'sup' : request.form["sup"],
        'mstr' : request.form["mstr"],
        'doc' : request.form["doc"],
        #Hobbies
        'hobbie1' : request.form["hobbie1"],
        'hobbie2' : request.form["hobbie2"],
        'hobbie3' : request.form["hobbie3"],
        'hobbie4' : request.form["hobbie4"]    
    }     
    
    return render_template('cv.html', data=data)
