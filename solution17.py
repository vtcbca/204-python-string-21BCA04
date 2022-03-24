#WAS to enter 5 string in a list and check and print string those lenth has even no of char.
#NOTE.:Do this UDF.... 
        #This is For only 1 string
def strlen(s):
    count=0
    for i in s:
        count+=1
    return(count)
str=input("string:")
ans=strlen(str)
print("length of {} is {}".format(str,ans))
if(ans%2==0):
    print(str)

