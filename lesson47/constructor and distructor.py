class employ:
    def __init__(self):
        print("employ created")

    def __del__(self):
        print("distructor called")

obj=employ()
del obj
print(obj)