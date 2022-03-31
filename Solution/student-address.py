#CA list student and add. which contain name of std and their add. print std name with his add.

# SIMPAL
std=['Sushant','Ajay','Mithun','Vivek','Anupam']
add=['kamrej','mumbai','banglore','kolkata','kashmir']
for i in range(5):
    print(std[i],"-",add[i])
print("--------------------------")

# UDF AND APPEND FUNCTION
std=[]
add=[]
def stdadd():
    for i in range(5):
        s=input("Student : ")
        std.append(s)
        a=input("Address : ")
        add.append(a)
stdadd();
for i in range(5):
    print(std[i],"-",add[i])



     
