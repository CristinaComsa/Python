# Exercitiu 1 - declar o lista cu note muzicale
print('Exercitiu 1')
note_muzicale = ['Do', 'Re, Mi', 'Fa', 'Sol', 'La', 'Si','Do']
print(note_muzicale)
new_note_muzicale = note_muzicale[::-1] # suprascriem prima lista prin slicing
print(new_note_muzicale)
new_note_muzicale.reverse() # se inverseaza lista prin metoda reverse
print(new_note_muzicale)
print()

# Exercitiu 2 - decate ori apare 'do'
print('Exercitiu 2')
print(f"'Do' apare de {note_muzicale.count('Do')} ori.")
print()

# Exercitiu 3 - avem 2 liste, sa le unim prin 2 metode
print('Exercitiu 3')
l_1 = [3, 1, 0, 2]
l_2 = [6, 5, 4]
l_1.extend(l_2) # metoda extend - se adauga lista 2 la lista 1 , ca elemente noi ( nu lista in lista)
print(l_1)
l_1[4:] = l_2 # slicing - adaugam lista 2 la o pozitie anume in lista 1, ca elemente noi ( nu lista in lista)
print(l_1)
print()

# Exercitiu 4 - sorteaza lista generata la exercitiu 3
print('Exercitiu 4')
l_1 = [3, 1, 0, 2]
l_2 = [6, 5, 4]
l_1.extend(l_2) # metoda extend - se adauga lista 2 la lista 1 , ca elemente noi ( nu lista in lista)
print(l_1)
l_1.sort() # sortam crescator lista 1(formata din l1+l2)
print(l_1)
l_1.pop(l_1[0]) # am folosit pop prentru a elimina '0', adica primul index
print(l_1)
print()

# # Exercitiu 5 - folosind if afisam daca lista este goala sau nu, lista de la ex 3-aici lista nu e goala
print('Exercitiu 5')
if len(l_1) == 0:
    print('List is empty')
else:
    print('List is not empty')
print()

# # Exercitiu 6 - folosim o metoda pentru a sterge lista generata la ex 3
print('Exercitiu 6')
l_1.clear() # am folosit metoda clear pentru a sterge lista 1
print(l_1)
print()


# # Exercitiu 7 - sa copiem exercitiu 5 si sa vedem ce afiseaza - acuma lista e goala
print('Exercitiu 7')
if  len(l_1) == 0:
    print('List is empty')
else:
    print('List is not empty')
print()

# Exercitiu 8 - avem un dict, sa afisam doar key
print('Exercitiu 8')
dict_1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict_1.keys()) # metoda keys- afisam doar keys(adica elevii in exemplul dat)
print()

# Exercitiu 9 - afisam cei 3 elevi si notele lor
print('Exercitiu 9')
dict_1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# for x, y in dict_1.items():
#     print(f"{x} are nota {y}")
for i in dict_1:
    print(f" {i} are nota {dict_1[i]}")
print()

# Exercitiu 10- Dorel primeste nota 6
print('Exercitiu 10')
dict_1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict_1['Dorel'] = 6
print(f"'Dorel a facut contestatie si a primit nota {dict_1['Dorel']}")
print()

# Exercitiu 11 -Gigel se muta din clasa, vine alt elev Ionica cu nota 9
print('Exercitiu 11')
dict_1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict_1['Dorel'] = 6
dict_1.pop('Gigel') # metoda pop- scoatem un element anume, in ex de fata Gigel
print(dict_1)
dict_1.update({'Ionica' : 9}) # metoda update, se adauga element nou la dict
print(dict_1)
print()

# Exercitiu 12 - avem un set
print('Exercitiu 12')
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni') # adaugam 'luni' setului, acesta nu permite duplicate, deci nu o afiseaza de 2 ori
print(zile_sapt)
print()

# Exercitiu 13 - sa afisam daca weekend este un subset al zile_sapt
print('Exercitiu 13')
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt): # issubset - se regaseste in setul zile_sapt
    print('Yes, weekend is subset of zile_sapt')
else:
    print('No, weekend is not a subset of zile_sapt')
print()

# Exercitiu 14 - sa afisam diferentele dintre cele 2 seturi
print('Exercitiu 14')
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
z = zile_sapt.difference(weekend) # afiseaza elementele care se regasesc doar in setul zile_sapt si nu si in set weekend
print(z)
print()

# Exercitiu 15 - sa afisam intersectia celor 2 seturi
print('Exercitiu 15')
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
z = zile_sapt.intersection(weekend) # afisam elementele comune ale celor 2 seturi
print(z)
print()

# Exercitiu optional - echipa de fotbal(lista), 3 schimbari admise
print('Exercitiu optional')
echipa_fotbal = ['J1_Mircea', 'J2_Gabi', 'J3_Alin', 'J4_Iulian', 'J5_Ion']
echipa_rezerve = ['R1_Adel', 'R2_Ionut', 'R3_Flaviu', 'R4_Dan', 'R5_Radu']
z = 3
print(echipa_fotbal)
print(echipa_rezerve)
x = echipa_fotbal.pop(1)
y = echipa_rezerve.pop(1)
echipa_fotbal.append(y)
echipa_rezerve.append(x)
print(echipa_fotbal)
print(echipa_rezerve)
z -= 1
print(f"Mai sunt {z} schimbari.")
x = echipa_fotbal.pop(2)
y = echipa_rezerve.pop(2)
echipa_fotbal.append(y)
echipa_rezerve.append(x)
print(echipa_fotbal)
print(echipa_rezerve)
z -= 1
print(f"Mai sunt {z} schimbari.")
if 'J4_Iulian' in echipa_fotbal and z > 0:
    x = echipa_fotbal.pop(0)
    y = echipa_rezerve.pop(0)
    echipa_fotbal.append(y)
    echipa_rezerve.append(x)
    z -= 1
    print(f" A iesit {x} si a intrat {y} si mai am {z} mutari.")
else:
    print(f"Nu se poate efectua schimbarea, jucatorul {x} nu este in teren.")
    print(f"Mai ai {z} mutari.")
print(echipa_fotbal)
print(echipa_rezerve)














