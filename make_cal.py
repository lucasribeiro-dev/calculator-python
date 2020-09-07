a = []
b = a 
c = 0 
e = 0 
f = 0 
x = 0 
z = 1 
y = 1

print('n1 = input("Place the first number: ")')
print('n2 = input("Place the second number: ")')
print('n = input("Choice: + - * /")')
print('if str(n1) == "0" and str(n2) == "0" and n == "/": \n    print("0")')


while c != 9999:
  a.append(c)
  c = c + 1

while x != 9999:
  for item in a:
    print('elif int(n1)'  '==', a[e],'and int(n2) ==',b[f], 'and n == "+": \n   print("',a[e] +  b[f], '")')
    print('elif int(n1)'  '==', a[e],'and int(n2) ==',b[f], 'and n == "-": \n   print("',a[e] -  b[f], '")')
    print('elif int(n1)'  '==', a[e],'and int(n2) ==',b[f], 'and n == "*": \n   print("',a[e] *  b[f], '")')
    print('elif int(n1)'  '==', a[z],'and int(n2) ==',b[y], 'and n == "/": \n   print("',a[z] /  b[y], '")')
    e = e + 1
    if e == 9999:
      e = 0 
      x = x + 1
      f = f + 1
      z = z + 1
      y = y +1