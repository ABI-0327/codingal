def test(l):
    result={}
    for item in l :
        result[item[0]]=item[1:]
    return result
student=[[1,"Abisathana",9],[2,"Niranya",9],[3,"Mehavarsha",9]] 
print("original list",student) 
print("converted list to dictionary",test(student))  
