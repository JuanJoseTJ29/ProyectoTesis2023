def servicio_prediccion(list):
    #if list == ['0','0','0','0','0','0','0','0','0']:
    #    return 'NO sufre de ningun caso de Violencia Familiar, \npero en caso de que tenga alguna duda solicite ayuda al "CHAT100" del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/'
    #if list == ['1','0','0','0','0','0','0','0','0'] or list == ['0','1','0','0','0','0','0','0','0'] or list == ['0','0','1','0','0','0','0','0','0'] or list == ['0','0','0','1','0','0','0','0','0'] or list == ['0','0','0','0','1','0','0','0','0'] or list == ['0','0','0','0','0','1','0','0','0']: 
    #    return 'Posiblemente este comenzando a sufrir Violencia Familiar'
    #if list == ['0','0','0','0','0','0','1','0','0'] or list == ['0','0','0','0','0','0','0','1','0'] or list == ['0','0','0','0','0','0','0','0','1'] :
    #    return 'Usted '
    #print(list)
    #return list

    if list == ['1','1','1','1','1','1','1','1','1']:
        return 'Usted SI sufre VIOLENCIA FAMILIAR, urgentemente comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'
    if list[6] == '1' and list[7] == '1' and list[8] == '1':
        return 'Usted Sufre de VIOLENCIA FAMILIAR, Comuniquese urgente con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana  '
    if list[6] == '1' and list[7] == '1':
        return 'Usted posiblemente sea victima de violencia familiar fisica, Comuniquese urgente con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana   '
    if list[6] == '1' and list[8] == '1':
        return 'Usted posiblemente sea victima de violencia familiar fisica y verbal, Comuniquese urgente con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana   '
    if list[7] == '1' and list[8] == '1':
        return 'Usted posiblemente sea victima de violencia familiar fisica y constantes amenzas verbale, Comuniquese urgente con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana   '
    if list[7] == '1':
        return 'Usted esta sufriendo de VIOLENCIA VERBAL, lo cual puede llevar a una VIOLENCIA FAMILIAR mayor, comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'
    if list[8] == '1':
        return 'Usted esta siendo amenazada(o) y atentada(o) contra su bienestar y esta apunto de sufrir VIOLENCIA FAMILIAR, urgentemente comuniquese con el CHAT-100  https://chat100.aurora.gob.pe/ o con el centro de ayuda de su localidad mas cercana para realizar su denuncia'
   # if list[9] == '1':
    #    return 'Usted esta siendo amenazada y esta sufrir VIOLENCIA FAMILIAR, urgentemente comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'

    if list[0] == '1':
        return 'Posiblemente sufra de acoso constante lo que puede llevar a la violencia , comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'
    if list[1] == '1':
        return 'Posiblemente sufra de acoso constante por parte de su pareja lo que puede llevar a la violencia, comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana '
    if list[2] == '1':
        return 'Posiblemente sufra de acoso y hostigamiento constante por parte de su pareja lo que puede llevar a la violencia, comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana '
    if list[3] == '1':
        return 'Posiblemente no tenga libertad para salir lo que puede llevar al hostigamiento y  violencia, comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana '  
    if list[4] == '1':
        return 'Usted sufre de acoso por parte de su pareja lo que puede llevar a la violencia, comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'
    if list[5] == '1':
        return 'Usted  sufre de hostigamiento y desconfianza por parte de su pareja lo que puede llevar a la violencia, comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana '
    
   # if list[0] == '1' or list[1] == '1' or list[2] == '1' or list[3] == '1' or list[4] == '1' or list[5] == '1' or list[6] == '1':
    #    return 'Posiblemente este comenzando a sufrir Violencia Familiar'
    else :
        return 'Posiblemente este comenzando a sufrir Violencia Familiar , comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'