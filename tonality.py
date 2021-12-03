class tonality():
    def __init__(self):
        pass
    
    def C_dur(self,kind='n',dir='up'):
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
    def a_moll(self,kind='n',dir='up'):
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

    def G_dur(self,kind='n',dir='up'):
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
    def e_moll(self,kind='n',dir='up'):
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

    def D_dur(self,kind='n',dir='up'):
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
    def h_moll(self,kind='n',dir='up'):
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

