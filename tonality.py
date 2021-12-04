class tonality():
    def __init__(self):
        pass
    
    #  dies tonality  #

    def C_dur(kind='n',dir='up'):
        t=[['','c'],['','d'],['','e'],['','f'],['','g'],['','a'],['','h']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6]=['','b']
                t[5][0]='ᵇ'
            return t
    def a_moll(kind='n',dir='up'):
        t=[['','a'],['','h'],['','c'],['','d'],['','e'],['','f'],['','g']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='#'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='#'
                t[5][0]='#'
            return t

    def G_dur(kind='n',dir='up'):
        t=[['','g'],['','a'],['','h'],['','c'],['','d'],['','e'],['#','f']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]='ᵇ'
            return t
    def e_moll(kind='n',dir='up'):
        t=[['','e'],['#','f'],['','g'],['','a'],['','h'],['','c'],['','d']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='#'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='#'
                t[5][0]='#'
            return t

    def D_dur(kind='n',dir='up'):
        t=[['','d'],['','e'],['#','f'],['','g'],['','a'],['','h'],['#','c']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]='ᵇ'
            return t
    def h_moll(kind='n',dir='up'):
        t=[['','h'],['#','c'],['','d'],['','e'],['#','f'],['','g'],['','a']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='#'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='#'
                t[5][0]='#'
            return t

    def A_dur(kind='n',dir='up'):
        t=[['','a'],['','h'],['#','c'],['','d'],['','e'],['#','f'],['#','g']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t
    def fis_moll(kind='n',dir='up'):
        t=[['#','f'],['#','g'],['','a'],['','h'],['#','c'],['','d'],['','e']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='#'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='#'
                t[5][0]='#'
            return t

    def E_dur(kind='n',dir='up'):
        t=[['','e'],['#','f'],['#','g'],['','a'],['','g'],['#','c'],['#','d']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t
    def cis_moll(kind='n',dir='up'):
        t=[['#','c'],['#','d'],['','e'],['#','f'],['#','g'],['','a'],['','h']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='#'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='#'
                t[5][0]='#'
            return t

    def H_dur(kind='n',dir='up'):
        t=[['','h'],['#','c'],['#','d'],['','e'],['#','f'],['#','g'],['#','a']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t
    def gis_moll(kind='n',dir='up'):
        t=[['#','g'],['#','a'],['','h'],['#','c'],['#','d'],['','e'],['#','f']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='##'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='##'
                t[5][0]='#'
            return t

    def Fis_dur(kind='n',dir='up'):
        t=[['#','f'],['#','g'],['#','a'],['','h'],['#','c'],['#','d'],['#','e']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t
    def dis_moll(kind='n',dir='up'):
        t=[['#','d'],['#','e'],['#','f'],['#','g'],['#','a'],['','h'],['#','c']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='##'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='##'
                t[5][0]='#'
            return t

    def Cis_dur(kind='n',dir='up'):
        t=[['#','c'],['#','d'],['#','e'],['#','f'],['#','g'],['#','a'],['#','h']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t
    def ais_moll(kind='n',dir='up'):
        t=[['#','a'],['#','h'],['#','c'],['#','d'],['#','e'],['','f'],['#','g']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='##'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='##'
                t[5][0]='##'
            return t

    # bemol tonality  ᵇ

    def F_dur(kind='n',dir='up'):
        t=[['','f'],['','g'],['','a'],['','b'],['','c'],['','d'],['','e']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='ᵇ'
                t[5][0]='ᵇ'
            return t
    def d_moll(kind='n',dir='up'):
        t=[['','d'],['','e'],['','f'],['','g'],['','a'],['','b'],['','c']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='#'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='#'
                t[5]=['','h']
            return t
    
    def B_dur(kind='n',dir='up'):
        t=[['','b'],['','c'],['','d'],['ᵇ','e'],['','f'],['','g'],['','a']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='ᵇ'
                t[5][0]='ᵇ'
            return t
    def g_moll(kind='n',dir='up'):
        t=[['','g'],['','a'],['','b'],['','c'],['','d'],['ᵇ','e'],['','f']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]='#'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='#'
                t[5][0]=''
            return t

    def Es_dur(kind='n',dir='up'):
        t=[['ᵇ','e'],['','f'],['','g'],['ᵇ','a'],['','b'],['','c'],['','d']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='ᵇ'
                t[5][0]='ᵇ'
            return t
    def c_moll(kind='n',dir='up'):
        t=[['','c'],['','d'],['ᵇ','e'],['','f'],['','g'],['ᵇ','a'],['','b']]
        if kind=='n':
            return t
        if kind=='g':
            t[6]=['','h']
            return t
        if kind=='m':
            if dir=='up':
                t[6]=['','h']
                t[5][0]=''
            return t

    def As_dur(kind='n',dir='up'):
        t=[['ᵇ','a'],['','b'],['','c'],['ᵇ','d'],['ᵇ','e'],['','f'],['','g']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='ᵇ'
                t[5][0]='ᵇ'
            return t
    def f_moll(kind='n',dir='up'):
        t=[['','f'],['','g'],['ᵇ','a'],['','b'],['','c'],['ᵇ','d'],['ᵇ','e']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t

    def Des_dur(kind='n',dir='up'):
        t=[['ᵇ','d'],['ᵇ','e'],['','f'],['ᵇ','g'],['ᵇ','a'],['','b'],['','c']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='ᵇ'
                t[5][0]='ᵇ'
            return t
    def b_moll(kind='n',dir='up'):
        t=[['','b'],['','c'],['ᵇ','d'],['ᵇ','e'],['','f'],['ᵇ','g'],['ᵇ','a']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t

    def Ges_dur(kind='n',dir='up'):
        t=[['ᵇ','g'],['ᵇ','a'],['','b'],['ᵇ','c'],['ᵇ','d'],['ᵇ','e'],['','f']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='ᵇᵇ'
                t[5][0]='ᵇ'
            return t
    def es_moll(kind='n',dir='up'):
        t=[['ᵇ','e'],['','f'],['ᵇ','g'],['ᵇ','a'],['','b'],['ᵇ','c'],['ᵇ','d']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t

    def Ces_dur(kind='n',dir='up'):
        t=[['ᵇ','c'],['ᵇ','d'],['ᵇ','e'],['ᵇ','f'],['ᵇ','g'],['ᵇ','a'],['','b']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇᵇ'
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]='ᵇᵇ'
                t[5][0]='ᵇ'
            return t
    def as_moll(kind='n',dir='up'):
        t=[['ᵇ','a'],['','b'],['ᵇ','c'],['ᵇ','d'],['ᵇ','e'],['ᵇ','f'],['ᵇ','g']]
        if kind=='n':
            return t
        if kind=='g':
            t[6][0]=''
            return t
        if kind=='m':
            if dir=='up':
                t[6][0]=''
                t[5][0]=''
            return t














