def encode(message):
    encoded=""
    i=0
    while(i<len(message)):
        count=1
        ch=message[i]
        j=i
        while(j<len(message)-1):
            if(message[j]==message[j+1]):
                count=count+1
                j=j+1
            else:
                break
        encoded+=str(count)+ch
        i=j+1
    return encoded 
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
