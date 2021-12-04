class tonality():
    def __init__(self):
        pass
        
    #  dies tonality  #

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

    def A_dur(self,kind='n',dir='up'):
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
    def fis_moll(self,kind='n',dir='up'):
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

    def E_dur(self,kind='n',dir='up'):
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
    def cis_moll(self,kind='n',dir='up'):
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

    def H_dur(self,kind='n',dir='up'):
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
    def gis_moll(self,kind='n',dir='up'):
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

    def Fis_dur(self,kind='n',dir='up'):
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
    def dis_moll(self,kind='n',dir='up'):
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

    def Cis_dur(self,kind='n',dir='up'):
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
    def ais_moll(self,kind='n',dir='up'):
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

    def F_dur(self,kind='n',dir='up'):
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
    def d_moll(self,kind='n',dir='up'):
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
    
    def B_dur(self,kind='n',dir='up'):
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
    def g_moll(self,kind='n',dir='up'):
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

    def Es_dur(self,kind='n',dir='up'):
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
    def c_moll(self,kind='n',dir='up'):
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

    def As_dur(self,kind='n',dir='up'):
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
    def f_moll(self,kind='n',dir='up'):
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

    def Des_dur(self,kind='n',dir='up'):
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
    def b_moll(self,kind='n',dir='up'):
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

    def Ges_dur(self,kind='n',dir='up'):
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
    def es_moll(self,kind='n',dir='up'):
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

    def Ces_dur(self,kind='n',dir='up'):
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
    def as_moll(self,kind='n',dir='up'):
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

notes={1:'a',2:'h',3:'c',4:'d',5:'e',6:'f',7:'g'}
marks={-2:'ᵇᵇ',-1:'ᵇ',0:'',1:'#',2:'##'}

class simple_intervals():
    def __init__(self):
        pass
        
    def prima(self,mark,first_note):
        return mark,first_note

    def small_secunda(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break
        if n_f<=(7-1):
            t_n=notes[n_f+1]
        else:
            t_n=notes[n_f-7+1]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if t_n=='f' or t_n=='c':
            pass
        else:
            mark=marks[n_m-1]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'   

        return  mark, t_n 

    def big_secunda(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break
        if n_f<=(7-1):
            t_n=notes[n_f+1]
        else:
            t_n=notes[n_f-7+1]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if t_n=='f' or t_n=='c':
            mark=marks[n_m+1]

        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'   

        return  mark, t_n  

    def small_tercia(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'            

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break
        if n_f<=(7-2):
            t_n=notes[n_f+2]
        else:
            t_n=notes[n_f-7+2]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break      

        if t_n=='f' or t_n=='c':
            pass
        else:
            mark=marks[n_m-1]
        if first_note=='e' or first_note=='h':
            mark=marks[n_m]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'   

        return  mark, t_n 

    def big_tercia(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break
        if n_f<=(7-2):
            t_n=notes[n_f+2]
        else:
            t_n=notes[n_f-7+2]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if t_n=='f' or t_n=='c':
            mark=marks[n_m+1]
        if first_note=='e' or first_note=='h':
            mark=marks[n_m+1]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'   

        return  mark, t_n 

    def free_cvarta(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break

        if (n_f+3)<=7:
            t_n=notes[n_f+3]
        else:
            t_n=notes[n_f-7+3]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if first_note=='f':
            mark=marks[n_m-1]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'    

        return  mark, t_n 
    
    def free_cvinta(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break

        if (n_f+4)<=7:
            t_n=notes[n_f+4]
        else:
            t_n=notes[n_f-7+4]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if first_note=='h':
            mark=marks[n_m+1]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'    

        return  mark, t_n 

    def small_sexta(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break
        if n_f<=(7-5):
            t_n=notes[n_f+5]
        else:
            t_n=notes[n_f-7+5]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if first_note=='a' or first_note=='h':
            mark=marks[n_m]
        else:
            mark=marks[n_m-1]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'   

        return  mark, t_n 

    def big_sexta(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break
        if n_f<=(7-5):
            t_n=notes[n_f+5]
        else:
            t_n=notes[n_f-7+5]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if first_note=='a' or first_note=='h':
            mark=marks[n_m+1]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'   

        return  mark, t_n 

    def small_septima(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break
        if n_f<=(7-6):
            t_n=notes[n_f+6]
        else:
            t_n=notes[n_f-7+6]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if first_note=='c' or first_note=='f':
            mark=marks[n_m-1]
        else:
            mark=marks[n_m]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'   

        return  mark, t_n 

    def big_septima(self,mark,first_note):
        if first_note=='b':
            if mark=='':
                first_note='h'
                mark='ᵇ'
            elif mark=='ᵇ':
                first_note='h'
                mark='ᵇᵇ'

        for i in notes.keys():
            if notes[i]==first_note:
                n_f=i
                break
        if n_f<=(7-6):
            t_n=notes[n_f+6]
        else:
            t_n=notes[n_f-7+6]

        for a in marks.keys():
            if marks[a]==mark:
                n_m=a
                break

        if first_note=='c' or first_note=='f':
            mark=marks[n_m]
        else:
            mark=marks[n_m+1]
        if t_n=='h' and mark=='ᵇ':
            mark=''
            t_n='b'   

        return  mark, t_n 

    def octava(self,mark,first_note):
        return mark, first_note


# class D_sptacrd():
#     def __init__(self):
#         pass

#     def D7(f_mark,first_note):
#         n1=[f_mark,first_note]
#         n2=simple_intervals.big_tercia(f_mark,first_note)
#         n3=simple_intervals.small_tercia(n2[0],n2[1])
#         n4=simple_intervals.small_tercia(n3[0],n3[1])
#         nots=[n1,n2,n3,n4]
#         print(nots)
#         return nots




