#como hacer un omelette
def sacarobjetodelacocina():
    return "objeto"
def prenderfuego(objeto, cantidad):
    return cantidad
esprimeravez = True
def ponerindgredientes(objeto, ingrediente):
    return True

#paso 1 
def primerpaso(mantequilla):
    sarten = sacarobjetodelacocina()
    if (esprimeravez):
        prenderfuego(sarten, "bajo")
    else:
        prenderfuego(sarten,"medio")
    
    ponerindgredientes(sarten,mantequilla)
    return sarten


def ponerindgredientes2(objeto, huevos,sal,pimienta,cebollin):
    return True
def batiringredientes(valor):
    return valor
#paso 2
def segundopaso(huevos, sal, pimienta, cebollin):
    bol = sacarobjetodelacocina()
    bol = ponerindgredientes2(bol, huevos,sal,pimienta,cebollin)
    bol = batiringredientes(20)
    return bol


def sacaringredientes(sarten):
    return sarten

def bordecocido(sarten):
    return sarten
def mover(sarten):
    return sarten
def omeletsuelto(omelet):
    return omelet
#paso 3 
def tercerpaso(sarten,bol):
    omelet = sacaringredientes(sarten)
    if(bordecocido(sarten)):
        omelet = mover(sarten)
    if (omeletsuelto(omelet)):
        return sarten


def doblaren3():
    return True
def poneringredientesenlamitad(sarten, queso, champinones):
    return sarten
def poneringredientes3(sarten, queso, champinones):
    return sarten
#paso 4 
def cuartopaso(sarten, queso, champinones):
    if (doblaren3):
        sarten = poneringredientesenlamitad(sarten, queso, champinones)
    else:
        sarten = poneringredientes3(sarten, queso, champinones)
    return sarten


def plegaromelet(sarten, espatula):
    return sarten
def estacocinado(sarten):
    return True
def pasaraplato(sarten):
    return sarten

#paso 5 
def quintopaso(sarten, espatula, plato):
    plato = sacarobjetodelacocina()
    plegaromelet(sarten, espatula)
    if (estacocinado(sarten)):
        plato = pasaraplato(sarten)