cards = [chr(x) for x in range(127136, 127199)]

with open('cards.html', 'w') as f:
     f.writelines('<p style="font-size: 6.4em;">')
     for char in cards:
         f.writelines(f'{char}\n')
     f.writelines('</p>')
