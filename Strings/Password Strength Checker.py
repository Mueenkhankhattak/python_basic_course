pasword = "MySecure123aaaa!"
result = {
    "length_ok" : False,
    "has_upper" : False,
    "has_lower" : False,
    "has_digit" : False,
    "has_special" : False,
    "strength"  : None,
    "score"  : None ,
    "issue" : [],
    "suggestions"   : [],
    "repeted_char" : []
} 

count = 0 

length_ok = len(pasword)
if length_ok >= 8:
    result["length_ok"] = True
    count += 20
else:
    result["suggestions"].append("Password is too short")
    
if length_ok >=12:
    result["length_ok"] = True
    count+=10   

        
if any(c.isupper() for c in pasword):
    result["has_upper"] = True
    count += 15
else:
    result["suggestions"].append("Password has no uppercase letter")
        
if any(c.islower() for c in pasword):
    result["has_lower"] = True
    count +=15
else:
    result["suggestions"].append("no lowercase letter")

if any(c.isdigit() for c in pasword):
    result["has_digit"] = True
    count +=15
else:
    result["suggestions"].append("pasword has no digit")
    
if any(not c.isalnum() for  c in pasword):
    result["has_special"] = True
    count +=15
else:
    result["suggestions"].append("no special character!")  
    
for char in pasword:
    if pasword.count(char) >= 4:
        result["repeted_char"] = char
        count-=10
        break
result["suggestions"].append("repeted char")
    
result["score"] = count

#count strength       
if count >=80:
    result["strength"] = "Very Strong"
    result["suggestions"].append("Consider making it longer for better security")
elif count >=60 and count < 80:
    result["strength"] = "Strong"
elif count >=40 and count < 60:
    result["strength"] = "Medium"
elif count >=20 and count < 40:
    result["strength"] = "week"
else:
    result["strength"] = "very Week"

print(result)
print(count)