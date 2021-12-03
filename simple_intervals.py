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