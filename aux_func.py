def sueldo_a_int(sueldo:object):
    if 'a' not in sueldo and 'o' not in sueldo:
        s = sueldo.replace('PA.', '')
        s = s.replace(' ','')
        s = s.replace(',','')
        res =int(s)
        return res