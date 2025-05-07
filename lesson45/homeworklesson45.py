my_tupple=(3,4,5)
print(my_tupple)

my_tupple=(3,"ABINIMEHI",5.5)
print(my_tupple)

print(my_tupple[0])
print(my_tupple[-1])

my_tupple=("mango","cherry","strawberry","watermelon")
print(my_tupple[1:5])
for i in (my_tupple):
    print(i)


    my_set={1,2,3,3,5,6}
print("my_set",my_set)

my_set.add(8)
print(my_set)

set1={1,2,3,4}
set2={5,5,7,9}
print("difference")
print(set1.difference(set2))
print("symmetric_difference")
print(set1.symmetric_difference(set2))


set1={"Asia","Australia"}
set2={"Europe","Asia"}
set3=set1.intersection(set2)
print(set3)


set1={"purple","pink"}
set2={"blue","purple"}
set3=set1.union(set2)
print(set3)