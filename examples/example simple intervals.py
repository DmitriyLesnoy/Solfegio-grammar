from simple_intervals import simple_intervals

intervals=simple_intervals()

note=['','c']

print(intervals.prima(note[0],note[1]),' - prima')
print(intervals.small_secunda(note[0],note[1]),' - small secunda')
print(intervals.big_secunda(note[0],note[1]),' - big secunda')
print(intervals.small_tercia(note[0],note[1]),' - small tercia')
print(intervals.big_tercia(note[0],note[1]),' - big tercia')
print(intervals.free_cvarta(note[0],note[1]),' - free cvarta')
print(intervals.free_cvinta(note[0],note[1]),' - free cvinta')
print(intervals.small_sexta(note[0],note[1]),' - small sexta')
print(intervals.big_sexta(note[0],note[1]),' - big sexta')
print(intervals.small_septima(note[0],note[1]),' - small septima')
print(intervals.big_septima(note[0],note[1]),' - big septima')
print(intervals.octava(note[0],note[1]),' - octava')