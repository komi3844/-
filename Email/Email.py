from validate_email import validate_email
mailname = input()
is_valid = validate_email (mailname, verify = True)
if is_valid == True:
    print('True')
else:
    print('false')






#Пример со списком
#a = []
#el = 3
#for _ in range(el):
#    a.append(input())
#print(a)