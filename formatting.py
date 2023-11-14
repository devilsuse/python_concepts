s1 = 'aaa'
s2 = 'bbb'

i = 100
f = 0.25

s = s1 + '_' + format(i, '05') + '_' + s2 + '_' + format(f, '.5f')
print(s)
# aaa_00100_bbb_0.25000

s = '{}_{:05}_{}_{:.5f}'.format(s1, i, s2, f)
print(s)
# aaa_00100_bbb_0.25000