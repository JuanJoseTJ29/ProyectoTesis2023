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
    if list[7] == '1' and list[8] == '1' and list[9] == '1':

    if list[7] == '1' and list[8] == '1':

    if list[7] == '1' and list[9] == '1':

    if list[8] == '1' and list[9] == '1':

    if list[7] == '1':
        return 'Usted esta sufriendo de VIOLENCIA VERBAL, lo cual puede llevar a una VIOLENCIA FAMILIAR mayor, comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'
    if list[8] == '1':
        return 'Usted esta siendo amenazada y atentada contra su bienestar y esta apunto de sufrir VIOLENCIA FAMILIAR, urgentemente comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'
    if list[9] == '1':
        return 'Usted esta siendo amenazada y esta sufrir VIOLENCIA FAMILIAR, urgentemente comuniquese con el CHAT-100 del Ministerio de la Mujer y Poblacion Vulnerable https://chat100.aurora.gob.pe/ o el centro de ayuda de su localidad mas cercana'

    if list[0] == '1':
    
    if list[1] == '1':
    
    if list[2] == '1':
    
    if list[3] == '1':
        
    if list[4] == '1':

    if list[5] == '1':
        
    if list[6] == '1':  

    if list[0] == '1' or list[1] == '1' or list[2] == '1' or list[3] == '1' or list[4] == '1' or list[5] == '1' or list[6] == '1':
        return 'Posiblemente este comenzando a sufrir Violencia Familiar'