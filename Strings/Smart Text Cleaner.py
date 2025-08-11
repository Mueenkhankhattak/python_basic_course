s =  "  hello world!!!   this is    a test.how are you?i am fine.  123remove numbers456  "
#handling edge case
if not s:
    print("empty", "")
    
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


result ="".join(i for i in s if i.isalpha())
print(result)




