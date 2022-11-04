from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico
# Create your views here.
# renderizar es PINTAR
def Home(request):
    return render(request,'index.html')

def Medicos(request):

    #debo utilizar la clase formularios Medicos
    #Creamos asi un objeto
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario
    }

    #Activar la recepcion de datos 
    if request.method=='POST':
        #Valiar si los datos son correctos 
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos 
            datos=datosRecibidos.cleaned_data
            print(datos)

    return render(request,'registromedicos.html',diccionario)

