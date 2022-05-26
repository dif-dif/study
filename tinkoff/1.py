# ab = input()
# ac = input()
# bc = input()

def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)

answ = 'abc'

if ab == '>':
    answ = swap(answ, 0, 1)
if ac == '>':
    answ = swap(answ, 0, 2)
if bc == '>':
    answ = swap(answ, 1, 2)
    
print(answ)

#test-case
ab = '>'
ac = '>'
bc = '>'
if answ == 'bac':
    print('Test 1: Ok')
else:
    print('Test 1: No')
    
ab = '='
ac = '>'
bc = '>'
if answ == 'cab':
    print('Test 1: Ok')
else:
    print('Test 1: No')
    
    
ab = '<'
ac = '<'
bc = '<'
if answ == 'bac':
    print('Test 1: Ok')
else:
    print('Test 1: No')
    
ab = '='
ac = '='
bc = '='
if answ == 'abc/n acb/n bac/n bca/n /ncab /ncba':
    print('Test 1: Ok')
else:
    print('Test 1: No')
    
ab = '='
ac = '='
bc = '>'
if answ == 'bac':
    print('Test 1: Ok')
else:
    print('Test 1: No')