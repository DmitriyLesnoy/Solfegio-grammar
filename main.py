from simple_intervals import simple_intervals
from tonality import tonality

intervals=simple_intervals()
tonalnost=tonality()

note=['','c']


print(tonalnost.C_dur('n'))
print(tonalnost.a_moll('n'))
print(tonalnost.G_dur('n'))
print(tonalnost.e_moll('n'))
print(tonalnost.D_dur('n'))
print(tonalnost.h_moll('n'))