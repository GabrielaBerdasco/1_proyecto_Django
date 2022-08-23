from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

def hello_world(request) :

    return HttpResponse('HOLA MUNDO')


def dynamic_name(request, name) :

    name = name
    return HttpResponse(f'<h2>Hola {name} !</h2>')


def calculate_year_of_birth(request, year) :

    current_date = datetime.now()
    age = current_date.year - int(year)
    data= """ <div align="center" style="border: 2px solid #d90429;">
    <h1 style="color: #8d99ae">Hola!</h1> </br> <h1 style="color: #8d99ae">Naciste en el año""" + year + """, tienes""" + str(age) + """ años.</h2>
    </div> """
    
    return HttpResponse(data)

def render_template(request) :
    
    user_data= {'nombre': 'Gabriela', 'apellido': 'Berdasco'}
    temp_1 = loader.get_template("template_1.html")
    doc_html = temp_1.render(user_data)

    return HttpResponse(doc_html)