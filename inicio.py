from flask import Flask, session, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'testingdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'





@app.route('/')
def index():
    return render_template("index.html")










@app.route('/area')
def area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area order by idArea')
    datos = cursor.fetchall()
    return render_template("area.html", area = datos)


@app.route('/area_editar/<string:id>')
def area_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area where idArea = %s', (id))
    dato = cursor.fetchall()
    return render_template("area_edi.html", area=dato[0])

@app.route('/area_fedita/<string:id>',methods=['POST'])
def area_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update area set descripcion=%s where idArea=%s', (desc,id))
        conn.commit()
    return redirect(url_for('area'))

@app.route('/area_borrar/<string:id>')
def area_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))

@app.route('/area_agregar')
def area_agregar():
    return render_template("area_agr.html")

@app.route('/area_fagrega', methods=['POST'])
def area_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into area (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('area'))






@app.route('/carrera')
def carrera():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera order by idCarrera')
    datos = cursor.fetchall()
    return render_template("carrera.html", carrera = datos)

@app.route('/carrera_editar/<string:id>')
def carrera_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera where idCarrera = %s', (id))
    dato = cursor.fetchall()
    return render_template("carrera_edi.html", carrera=dato[0])

@app.route('/carrera_fedita/<string:id>',methods=['POST'])
def carrera_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update carrera set descripcion=%s where idCarrera=%s', (desc,id))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route('/carrera_borrar/<string:id>')
def carrera_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from carrera where idCarrera = {0}'.format(id))
    conn.commit()
    return redirect(url_for('carrera'))

@app.route('/carrera_agregar')
def carrera_agregar():
    return render_template("carrera_agr.html")

@app.route('/carrera_fagrega', methods=['POST'])
def carrera_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into carrera (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('carrera'))




@app.route('/escolaridad')
def escolaridad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad order by idEscolaridad')
    datos = cursor.fetchall()
    return render_template("escolaridad.html", escolaridad = datos)

@app.route('/escolaridad_editar/<string:id>')
def escolaridad_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad where idEscolaridad = %s', (id))
    dato = cursor.fetchall()
    return render_template("escolaridad_edi.html", escolaridad=dato[0])

@app.route('/escolaridad_fedita/<string:id>',methods=['POST'])
def escolaridad_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update escolaridad set descripcion=%s where idEscolaridad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('escolaridad'))
    
@app.route('/escolaridad_borrar/<string:id>')
def escolaridad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from escolaridad where idEscolaridad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('escolaridad'))

@app.route('/escolaridad_agregar')
def escolaridad_agregar():
    return render_template("escolaridad_agr.html")

@app.route('/escolaridad_fagrega', methods=['POST'])
def escolaridad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into escolaridad (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('escolaridad'))
    




@app.route('/gradoavance')
def gradoavance():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idGradoavance, descripcion from gradoavance order by idGradoavance')
    datos = cursor.fetchall()
    return render_template("gradoavance.html", gradoavance = datos)

@app.route('/gradoavance_editar/<string:id>')
def gradoavance_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idGradoavance, descripcion from gradoavance where idGradoavance = %s', (id))
    dato = cursor.fetchall()
    return render_template("gradoavance_edi.html", gradoavance=dato[0])

@app.route('/gradoavance_fedita/<string:id>',methods=['POST'])
def gradoavance_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update gradoavance set descripcion=%s where idGradoavance=%s', (desc,id))
        conn.commit()
    return redirect(url_for('gradoavance'))
    
@app.route('/gradoavance_borrar/<string:id>')
def gradoavance_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from gradoavance where idGradoavance = {0}'.format(id))
    conn.commit()
    return redirect(url_for('gradoavance'))

@app.route('/gradoavance_agregar')
def gradoavance_agregar():
    return render_template("gradoavance_agr.html")

@app.route('/gradoavance_fagrega', methods=['POST'])
def gradoavance_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into gradoavance (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('gradoavance'))


 

 

@app.route('/estadocivil')
def estadocivil():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idEstadocivil, descripcion from estadocivil order by idEstadocivil')
    datos = cursor.fetchall()
    return render_template("estadocivil.html", estadocivil = datos)

@app.route('/estadocivil_editar/<string:id>')
def estadocivil_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idEstadocivil, descripcion from estadocivil where idEstadocivil = %s', (id))
    dato = cursor.fetchall()
    return render_template("estadocivil_edi.html", estadocivil=dato[0])

@app.route('/estadocivil_fedita/<string:id>',methods=['POST'])
def estadocivil_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update estadocivil set descripcion=%s where idEstadocivil=%s', (desc,id))
        conn.commit()
    return redirect(url_for('estadocivil'))
    
@app.route('/estadocivil_borrar/<string:id>')
def estadocivil_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from estadocivil where idEstadocivil = {0}'.format(id))
    conn.commit()
    return redirect(url_for('estadocivil'))

@app.route('/estadocivil_agregar')
def estadocivil_agregar():
    return render_template("estadocivil_agr.html")

@app.route('/estadocivil_fagrega', methods=['POST'])
def estadocivil_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into estadocivil (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('estadocivil'))






@app.route('/habilidades')
def habilidades():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idHabilidades, descripcion from habilidades order by idHabilidades')
    datos = cursor.fetchall()
    return render_template("habilidades.html", habilidades = datos)

@app.route('/habilidades_editar/<string:id>')
def habilidades_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idHabilidades, descripcion from habilidades where idHabilidades = %s', (id))
    dato = cursor.fetchall()
    return render_template("habilidades_edi.html", habilidades=dato[0])

@app.route('/habilidades_fedita/<string:id>',methods=['POST'])
def habilidades_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update habilidades set descripcion=%s where idHabilidades=%s', (desc,id))
        conn.commit()
    return redirect(url_for('habilidades'))
    
@app.route('/habilidades_borrar/<string:id>')
def habilidades_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from habilidades where idHabilidades = {0}'.format(id))
    conn.commit()
    return redirect(url_for('habilidades'))

@app.route('/habilidades_agregar')
def habilidades_agregar():
    return render_template("habilidades_agr.html")

@app.route('/habilidades_fagrega', methods=['POST'])
def habilidades_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into habilidades (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('habilidades'))




@app.route('/idioma')
def idioma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma order by idIdioma')
    datos = cursor.fetchall()
    return render_template("idioma.html", idioma = datos)

@app.route('/idioma_editar/<string:id>')
def idioma_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma where idIdioma = %s', (id))
    dato = cursor.fetchall()
    return render_template("idioma_edi.html", idioma=dato[0])

@app.route('/idioma_fedita/<string:id>',methods=['POST'])
def idioma_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update idioma set descripcion=%s where idIdioma=%s', (desc,id))
        conn.commit()
    return redirect(url_for('idioma'))
    
@app.route('/idioma_borrar/<string:id>')
def idioma_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from idioma where idIdioma = {0}'.format(id))
    conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_agregar')
def idioma_agregar():
    return render_template("idioma_agr.html")

@app.route('/idioma_fagrega', methods=['POST'])
def idioma_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into idioma (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('idioma'))




@app.route('/mediopublicidad')
def mediopublicidad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idMediopublicidad, descripcion from mediopublicidad order by idMediopublicidad')
    datos = cursor.fetchall()
    return render_template("mediopublicidad.html", mediopublicidad = datos)

@app.route('/mediopublicidad_editar/<string:id>')
def mediopublicidad_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idMediopublicidad, descripcion from mediopublicidad where idMediopublicidad = %s', (id))
    dato = cursor.fetchall()
    return render_template("mediopublicidad_edi.html", mediopublicidad=dato[0])

@app.route('/mediopublicidad_fedita/<string:id>',methods=['POST'])
def mediopublicidad_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update mediopublicidad set descripcion=%s where idMediopublicidad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('mediopublicidad'))
    
@app.route('/mediopublicidad_borrar/<string:id>')
def mediopublicidad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from mediopublicidad where idMediopublicidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('mediopublicidad'))

@app.route('/mediopublicidad_agregar')
def mediopublicidad_agregar():
    return render_template("mediopublicidad_agr.html")

@app.route('/mediopublicidad_fagrega', methods=['POST'])
def mediopublicidad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into mediopublicidad (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('mediopublicidad'))





























@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()
    return render_template("puesto.html", pue=datos, dat=' ', catArea=' ', catEdoCivil=' ',catEscolaridad=' ',catGradoAvance=' ', catCarrera=' ', catIdioma=' ', catHabilidad=' ')

@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,funciones,edad,sexo,idEstadocivil,idEscolaridad,idGradoavance,idCarrera,experiencia,conocimientos,manejoEquipo,reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idEstadocivil, a.descripcion from estadocivil a, puesto b where a.idEstadocivil = b.idEstadocivil and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idGradoavance, a.descripcion from gradoavance a, puesto b where a.idGradoavance = b.idGradoavance and b.idPuesto = %s', (idP)) 
    datos4 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c ''where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s',(idP))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidades, b.descripcion from puesto a, habilidades b, puesto_has_habilidad c ''where a.idPuesto = c.idPuesto and b.idHabilidades = c.idHabilidades and a.idPuesto = %s',(idP))
    datos7 = cursor.fetchall()
    return render_template("puesto.html", pue=datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0], catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    return redirect(url_for('puesto'))

@app.route('/puesto_agregar')
def puesto_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    
    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()
    cursor.execute('select idEstadocivil, descripcion from estadocivil ')
    datos2 = cursor.fetchall()
    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()
    cursor.execute('select idGradoavance, descripcion from gradoavance ')
    datos4 = cursor.fetchall()
    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()
    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()
    cursor.execute('select idHabilidades, descripcion from habilidades ')
    datos7 = cursor.fetchall()
    return render_template("puesto_agr.html", catArea=datos1, catEdoCivil=datos2,catEscolaridad=datos3, catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_fagrega', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':
        if 'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        if 'idEstadocivil' in request.form:
            idEC = request.form['idEstadocivil']
        else:
            idEC = '1'
        if 'idEscolaridad' in request.form:
            idEs = request.form['idEscolaridad']
        else:
            idEs = '1'
        if 'idGradoavance' in request.form:
            idGA = request.form['idGradoavance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        if 'sexo' in request.form:
            sex = request.form['sexo']
        else:
            sex = '1'
        codP = request.form['codPuesto']
        
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']
        
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,''funciones,edad,sexo,idEstadocivil,idEscolaridad,idGradoavance,idCarrera,experiencia,conocimientos,manejoEquipo,''reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT))
    conn.commit()
    cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) frompuesto) ')
    dato=cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]
    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1
    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP,i))
            
            conn.commit()
            
    cursor.execute('select count(*) from habilidades ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1
    
    for i in range(1, nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidades) values (%s,%s)',(idP, i))
            
            conn.commit()
        return redirect(url_for('puesto'))


















@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,funciones,edad,sexo,idEstadocivil,idEscolaridad,idGradoavance,idCarrera,experiencia,conocimientos,manejoEquipo,reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idArea, descripcion from area')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadocivil, descripcion from estadocivil')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoavance, descripcion from gradoavance')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidades, descripcion from habilidades')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos11 = cursor.fetchall()

    cursor.execute('select a.idEstadocivil, a.descripcion from estadocivil a, puesto b where a.idEstadocivil = b.idEstadocivil and b.idPuesto = %s', (idP))
    datos12 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
    datos13 = cursor.fetchall()

    cursor.execute('select a.idGradoavance, a.descripcion from gradoavance a, puesto b where a.idGradoavance = b.idGradoavance and b.idPuesto = %s', (idP))
    datos14 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidades, b.descripcion from puesto a, habilidades b, puesto_has_habilidad c where a.idPuesto = c.idPuesto and b.idHabilidades = c.idHabilidades and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()

    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7, Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0], Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        if 'idGradoavance' in request.form:
            idGA = request.form['idGradoavance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadocivil']
        idEs = request.form['idEscolaridad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, idEstadocivil = %s, idEscolaridad = %s, idGradoavance = %s, idCarrera = %s, experiencia = %s, conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()
    return redirect(url_for('puesto'))

















@app.route('/requisicion_pend')
def requisicion_pend():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, folio from requisicion order by idRequisicion')
    datos = cursor.fetchall()
    cursor.execute('select idRequisicion, nomPuesto from requisicion, puesto order by idRequisicion')
    datoss = cursor.fetchall()
    return render_template("requisicion_pend.html", req=datos, pue=datoss, dat=' ', catArea=' ', catPuesto=' ', catPuestoJefeSup=' ', catJornada=' ', catDescripcionGeneral=' ', catFunciones=' ', catEdad=' ', catSexo=' ', catEscolaridad=' ', catEstadoCivil=' ')



@app.route('/requisicion_fdetalle/<string:idR>', methods=['GET'])
def requisicion_fdetalle(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idRequisicion, folio from requisicion order by idRequisicion')
    datos = cursor.fetchall()

    cursor.execute('select idRequisicion, nomPuesto from requisicion, puesto order by idRequisicion')
    datoss = cursor.fetchall()

    cursor.execute('select idRequisicion,folio,fechaElab,fechaRecluta,fechaInicVac,motivoRequisicion,motivoEspecifique,tipoVacante,nomSolicita,nomAutoriza,nomRevisa,autorizada,idPuesto,idArea from requisicion where idRequisicion = %s', (idR))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idR))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.nomPuesto from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos2 = cursor.fetchall()



    cursor.execute('select a.idPuesto, a.puestoJefeSup from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.jornada from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos9 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.descripcionGeneral from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.funciones from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.edad from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.sexo from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos7 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idR))
    datos8 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estadocivil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idR))
    datos10 = cursor.fetchall()

    return render_template("requisicion_pend.html", req=datos, pue=datoss, dat=dato[0], catArea=datos1[0], catPuesto=datos2[0], catPuestoJefeSup=datos3[0], catJornada=datos9[0], catDescripcionGeneral=datos4[0], catFunciones=datos5[0], catEdad=datos6[0], catSexo=datos7[0], catEscolaridad=datos8[0], catEstadoCivil=datos10[0])

@app.route('/requisicion_borrar/<string:idR>')
def requisicion_borrar(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from requisicion where idRequisicion = %s',(idR))
    conn.commit()
    return redirect(url_for('requisicion_pend'))



@app.route('/requisicion_autorizar/<string:idR>', methods=['GET'])
def requisicion_autorizar(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()


    cursor.execute('select idRequisicion,folio,fechaElab,fechaRecluta,fechaInicVac,motivoRequisicion,motivoEspecifique,tipoVacante,nomSolicita,nomAutoriza,nomRevisa,autorizada,idPuesto,idArea from requisicion where idRequisicion = %s', (idR))
    dato = cursor.fetchall()

    cursor.execute('select idRequisicion, folio from requisicion order by idRequisicion')
    datos = cursor.fetchall()

    cursor.execute('select idRequisicion, nomPuesto from requisicion, puesto order by idRequisicion')
    datoss = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.nomPuesto from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos2 = cursor.fetchall()
    return render_template("requisicion_aut.html", dat=dato[0], req=datos, pue=datoss, catPuesto=datos2[0])


@app.route('/requisicion_fautorizar/<string:idR>', methods=['POST']) 
def requisicion_fautorizar(idR):
    if request.method == 'POST':

        nomRevisa = request.form['nomRevisa']
        nomAutoriza = request.form['nomAutoriza']
        
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()


    cursor.execute('update requisicion set nomRevisa = %s, nomAutoriza = %s, autorizada = 1 where idRequisicion = %s', (nomRevisa, nomAutoriza, idR))
    conn.commit()


    return redirect(url_for('requisicion_autorizadas'))
























@app.route('/requisicion_agregar')
def requisicion_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    
    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()
    cursor.execute('select idPuesto, nomPuesto from puesto ')
    datos2 = cursor.fetchall()
    return render_template("requisicion_agr.html", catArea=datos1, catPuesto=datos2)




@app.route('/requisicion_fagrega', methods=['POST'])
def requisicion_fagrega():
    if request.method == 'POST':
        if 'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        
        if 'idPuesto' in request.form:
            idPue = request.form['idPuesto']
        else:
            idPue = '1'
        
        
        
        folio = request.form['folio']
        feRec = request.form['fechaRecluta']
        feIni = request.form['fechaInicVac']
        tipVac = request.form['tipoVacante']
        nomSoli = request.form['nomSolicita']
        
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('insert into requisicion (idArea,idPuesto,folio,fechaRecluta,fechaInicVac,tipoVacante,nomSolicita) values (%s,%s,%s,%s,%s,%s,%s)', (idAr, idPue, folio, feRec, feIni, tipVac, nomSoli))
    conn.commit()
    cursor.execute('select idRequisicion, folio from requisicion where idRequisicion=(select max(idRequisicion) from requisicion) ')
    dato=cursor.fetchall()

    return redirect(url_for('requisicion_pend', req=dato))











@app.route('/requisicion_autorizadas')
def requisicion_autorizadas():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, folio from requisicion where autorizada= 1 order by idRequisicion')
    datos = cursor.fetchall()
    cursor.execute('select idRequisicion, nomPuesto from requisicion, puesto order by idRequisicion')
    datoss = cursor.fetchall()
    return render_template("requisicion_autorizadas.html", req=datos, pue=datoss, dat=' ', catArea=' ', catPuesto=' ', catPuestoJefeSup=' ', catJornada=' ', catDescripcionGeneral=' ', catFunciones=' ', catEdad=' ', catSexo=' ', catEscolaridad=' ', catEstadoCivil=' ')


@app.route('/requisicion_autofdetalle/<string:idR>', methods=['GET'])
def requisicion_autofdetalle(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idRequisicion, folio from requisicion order by idRequisicion')
    datos = cursor.fetchall()

    cursor.execute('select idRequisicion, nomPuesto from requisicion, puesto order by idRequisicion')
    datoss = cursor.fetchall()

    cursor.execute('select idRequisicion,folio,fechaElab,fechaRecluta,fechaInicVac,motivoRequisicion,motivoEspecifique,tipoVacante,nomSolicita,nomAutoriza,nomRevisa,autorizada,idPuesto,idArea from requisicion where idRequisicion = %s', (idR))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idR))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.nomPuesto from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos2 = cursor.fetchall()



    cursor.execute('select a.idPuesto, a.puestoJefeSup from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.jornada from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos9 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.descripcionGeneral from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.funciones from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.edad from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.sexo from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos7 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idR))
    datos8 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estadocivil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idR))
    datos10 = cursor.fetchall()

    return render_template("requisicion_autorizadas.html", req=datos, pue=datoss, dat=dato[0], catArea=datos1[0], catPuesto=datos2[0], catPuestoJefeSup=datos3[0], catJornada=datos9[0], catDescripcionGeneral=datos4[0], catFunciones=datos5[0], catEdad=datos6[0], catSexo=datos7[0], catEscolaridad=datos8[0], catEstadoCivil=datos10[0])












if __name__ == "__main__":
    app.run(debug=True)