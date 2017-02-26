string = 'Bonjour Madame comment allez-vous ?'
print 'String utilisee: ', string
print '\n'

print 'capitalize'
print string.capitalize()
print '\n'

print 'center'
print string.center(80)
print '\n'

print 'count o'
print string.count('o')
print '\n'

print 'decode'
print string.decode()
print '\n'

print 'encode'
print string.encode('base64')
print '\n'

print 'endswith'
print string.endswith('?')
print '\n'

print 'expandtabs'
str2 = 'allo	test	salut'
print str2.expandtabs()
print '\n'

print 'find Madame'
print string.find('Madame')
print '\n'

print 'format'
str3 = 'la phrase {}'
print str3.format(6)
print '\n'

print 'index'
print string.index('Madame')
print '\n'

print 'isalnum'
newString = 'salutpapa'
print 'Nouvelle String: ', newString
print newString.isalnum()
print '\n'

print 'isalpha'
print string.isalpha()
print '\n'

print 'isdigit'
print string.isdigit()
print '\n'

print 'islower'
print string.islower()
print '\n'

print 'isspace'
print string.isspace()
print '\n'

print 'istitle'
print string.istitle()
print '\n'

print 'isupper'
print string.isupper()
print '\n'

print 'join'
separator = '-'
print separator.join(string)
print '\n'

print 'ljust'
print string.ljust(10)
print '\n'

print 'lower'
print string.lower()
print '\n'

print 'lstrip'
print string.lstrip('oh')
print '\n'

print 'partition'
print string.partition(' ')
print '\n'

print 'replace Madame par Monsieur'
print string.replace('Madame', 'Monsieur')
print '\n'

print 'rfind e'
print string.rfind('e')
print '\n'

print 'rindex Madame'
print string.rindex('Madame')
print '\n'

print 'rjust'
print string.rjust(50, '0')
print '\n'

print 'rpartition'
print string.rpartition(' ')
print '\n'

print 'rsplit'
print string.rsplit(' ')
print '\n'

print 'rstrip'
print string.rstrip('Madame')
print '\n'

print 'split'
print string.split()
print '\n'

print 'splitlines'
print string.splitlines()
print '\n'

print 'startswith'
print string.startswith('b')
print '\n'

print 'strip'
print string.strip('bonjour maman')
print '\n'

print 'swapcase'
print string.swapcase()
print '\n'

print 'title'
print string.title()
print '\n'

print 'upper'
print string.upper()
print '\n'

print 'zfill'
print string.zfill(50)
print '\n'