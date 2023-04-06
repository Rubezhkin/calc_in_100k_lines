f = open('calculator.txt', "w")
n = int(input())

f.write('''num1 = int(input('1 number: '))
sign = input('operation +, -, /, *, or ^: ')
num2 = int(input('2 number: '))\n''')

operations = {
    '+': lambda x,y:x+y, 
    '-': lambda x,y:x-y,
    '/': lambda x,y:x/y,
    '*': lambda x,y:x*y,
    '^': lambda x,y: x**y,}
def CalcResult(operation, x, y):
    return operations[operation](x,y)


for i in ('+-/*^'):
    for j in range(n+1):
        for k in range(n+1):
            if k == 0 and i == '/':
                Result = 'Undefined'
            else:
                Result = CalcResult(i, j, k)
            str1 = "if num1 == "+str(j)+" and sign == '"+i+"' and num2 == "+str(k)+":\n"
            str2 = '''   print("'''+str(j)+i+str(k)+ " = " + str(Result)+'''")\n'''
            f.write(str1)
            f.write(str2)

f.write("input()")
f.close()   