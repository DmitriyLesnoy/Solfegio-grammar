class tonality():
    def __init__(self):
        pass
    
    def C_dur(self,kind='n',dir='up'):
        t=[['','c'],['','d'],['','e'],['','f'],['','g'],['','a'],['','g']]
        if kind=='n':
            return t
        if kind=='g':
            t[5][0]='ᵇ'
            return t
        if kind=='m':
            t[6][0]='ᵇ'
            t[5][0]='ᵇ'
            if dir=='down':
                t=[['','c'],['','d'],['','e'],['','f'],['','g'],['','a'],['','g']]
            return t

