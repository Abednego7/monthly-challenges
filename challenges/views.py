from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from django.template.loader import render_to_string

# Convierte algo a una cadena (como HTML a cadena)
# Ahora, Django tiene un atajo para esta importacion y viene ya con nuestro proyecto y es 'render'
# asi que comentaremos esta importacio y haremos uso de lo que tenemos ya pre-establecido.

# from django.template.loader import render_to_string

# Global Dictionary
monthly_challenges = {
    "january": "Keep learning all about Python",
    "february": "Doing sports",
    "march": "Eat healthy",
    "april": "Celebrate my birthday",
    "may": "Do not eat sugar",
    "june": "Continue learning Python and everything about it",
    "july": "Read books",
    "august": "Drink 1 liter of water a day",
    "september": "Improve my skills in all aspects",
    "october": "Take on LeetCode challenges",
    "november": None,
    "december": "Celebrate Christmas and New Year",
}

# Create your views here.
# Una view puede ser una funcion o una clase
# Las vistas son responsables de procesar las solicitudes y crear una respuesta
"""
def january(request):
    return HttpResponse("Keep learning all about Python")


def february(request):
    return HttpResponse("Have a weight within the healthy standard")
"""


def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})

    """
    for month in months:
        capitalized_month = month.capitalize()

        # Como anteriormente se creo un redirect, solo lo usamos
        month_path = reverse("dynamic_path", args=[month])  # /challenge/january

        # Se usaron caracteres de escape para evitar errores en el doble "" del href
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    """


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    # Suponiendo que el valor de month(parametro) es 1, seria (1 - 1) = 0, 0 es el indice y
    # devuelve 'january' la cual se almacena en la variable de redirect_month
    redirect_month = months[month - 1]

    # reverse crea una url dinamica sin codificarlas (ejm: Comentario de Before) donde se pasa el nombre de la 'url' (/challenges/)
    # y los argumentos que se usan, no todas las url tiene args, en este caso si.
    redirect_path = reverse("dynamic_path", args=[redirect_month])  # /challenge/january

    # La nueva redirección debe ser válida, como la que usamos en el archivo 'urls'
    return HttpResponseRedirect(
        redirect_path
    )  # Before: HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    # month es la variable de ruta dinamica que se creo en urls

    try:
        challenge_text = monthly_challenges[month]
        # Algo curioso es que el HTML esta dentro de una carpeta con el 'nombre de la app'
        # esto se debe a que es buena practica usar ese nombre para que Django sepa identificar
        # los archivos de otros proyectos que puedan tener el mismo nombre de challenge.html

        # Render necesita como argumento 'request', para que internamente pueda extraer datos de alli;
        # y como segundo argumento la plantilla.

        # render = (request + path + args(context))
        return render(
            request,
            "challenges/challenge.html",
            {
                "text": challenge_text,  # variable para usar en nuestra plantilla
                "month_name": month,
            },
        )

        # Se comentara estas lineas para simplificar aun mas el codigo con el uso de 'render'
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # Se hace uso de 'render_to_string' para combertir el HTML a cadena y ser renderizada.
        # El uso de esta funcion tambien es porque 'no estamos enviando ningun dato' a ese HTML como lo hariamos normalmente
        # usando 'render'.

        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        # Http404 buscara automaticamente el archivo con el nombre especifico '404.html' en la carpeta 
        # especifica de 'templates', de esta manera debe siempre 'tener ese nombre de archivo y carpeta'

        # Nota: para que esto funcione, se debe ir a settings y cambiar el valor de DEBUG a 'False', pero... 
        # esto solo sera recomendable cuando se despliegue nuestra aplicacion, ya que el DEBUG 'True' nos mostrara errores 
        # importantes para poder corregir en nuestra aplicacion.
        raise Http404()
