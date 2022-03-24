#WAS to enter 5 string in a list and check and print string those lenth has even no of char.
#NOTE.:Do this UDF.... 
def strlen(s):
    count=0
    for i in s:
        count+=1
    return(count)
for i in range(5):
        str=input("string:")
        ans=strlen(str)
        if(ans%2==0):
                print(str)

