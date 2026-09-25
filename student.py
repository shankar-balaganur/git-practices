
with open("test.txt","r") as f:
    data=f.read()


    new_data= data.replace("shankar","janu")
    print(new_data)

with open("test.txt","w") as f:
    data=f.write(new_data)
    print(data)