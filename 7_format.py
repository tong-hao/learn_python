
n = 100
a = 'ht'
s1 = '''
name={name}
age={age}
'''.format(name= n, age=a)
print(s1)


n = 100
a = 'ht'
s1 = '''
name={0}
age={1}
'''.format(n, a)
print(s1)


name = "ht"
age = 200
s1 = f'''
name={name}
age={age}
'''
print(s1)

print(f"double age: {age: .2f}")
