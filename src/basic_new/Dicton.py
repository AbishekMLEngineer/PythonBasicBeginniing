import itertools

dict = {45: 'Nandini', 'Age': 19}
# using has_key() to check if dic1 has a key
#key in dict
if 45 in dict:
    print('yes')

print(dict.get(45))

l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

s="geekss"
for i in s:
   # print(i)


    def attachdata(func):
        func.data =3
        return  func

li1 = [1, 4, 5, 7]

print(list(itertools.accumulate(li1)))