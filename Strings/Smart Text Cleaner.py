s =  "  hello world!!!   this is    a test.how are you?i am fine.  123remove numbers456  "
#handling edge case
if not s:
    print("")
    
#step 1 remove extra space
s = s.strip()
print("remove leading space:" , s)
print()
#step2 split text 
s = s.split()
print("spilit text into words:" ,s)
print()

#step 3 join back
s = " ".join(s)
print("jion back:",s)
 #step 4 remove number


result = "".join(char for char in s if char.isalpha() or char.isspace())
print(result)

n = "123456789"
punctuation = "!@"
for char in s:
    if char in n or char in punctuation:
        s = s.replace(char ,"") 

print(s)


