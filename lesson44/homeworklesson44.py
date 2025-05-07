l=["mouse","monitor","CPU","keyboard","speaker"]
print("lenght of list ",len(l))
print("first element ",l[0])
print("last element ",l[-1])
l.append("CPU")
print("updated list",l)
l.remove("keyboard")
print("updated list",l)
l.sort()
print("updated list",l)
l.reverse()
print("updated list",l)


d={1:"pink",2:"purple","Name":"Abisathana"}
print(d[1])
print(d["Name"])
d[2]=27
print(d)
d["colour"]="blue"
print(d)
d.pop(1)
print(d)


def test(l):
    result={}
    for item in l :
        result[item[0]]=item[1:]
    return result
student=[[1,"Abisathana",9],[2,"Niranya",9],[3,"Mehavarsha",9]] 
print("original list",student) 
print("converted list to dictionary",test(student))  
