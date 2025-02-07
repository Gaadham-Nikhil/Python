file1 = open('files/test_file1.txt','w')
try:
    file1.write('Creating my First file using python Command shell')
finally:
    file1.close()

with open('files/test_file2.txt','w') as file2:
    file2.write('Creating my Second file using python Command shell')


with open('files/test_file3.txt','w') as file2:
    file2.write('Creating my Second file using python Command shell')