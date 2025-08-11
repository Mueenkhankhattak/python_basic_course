pasword = "ab1"
result = {
    "length_ok" : False,
    "has_upper" : False,
    "has_lower" : False,
    "has_digit" : False,
    "has_special" : False,
    "strength"  : None,
    "score"  : None ,
    "issue" : [],
    "suggestions"   : []
} 

count = 0 
length_ok = len(pasword)
if length_ok >= 8:
    result["length_ok"] = length_ok
    count+=20
if length_ok >=12:
    result["length_ok"] = length_ok
    count+=10   
if length_ok < 8:
    result["length_ok"] = "pasword is too short"
 
for char in pasword:
    if char.isupper() and not result["has_upper"]:
        result["has_upper"] = True
        count = count + 15
    else:
        result["suggestions"] = "Kindly increase Your length"
        
        
    if char.islower() and not result["has_lower"]:
        result["has_lower"] = True
        count +=15
    else:
        result["suggestions"] = "pasword has no lowercase letter"
    
    if char.isdigit() and not  result["has_digit"]:
        result["has_digit"] = True
        count +=15
    else:
        result["suggestions"] = "pasword has no digit kindly add digit!"
        
    if not char.isalnum() and not result["has_special"]:
        result["has_special"] = True
        count +=15
    else:
        result["suggestions"] = "pasword has no special character!"  
        
result["score"] = count

#count strength       
if count >=80:
    result["strength"] = "Very Strong"
    result["suggestions"] = "Consider making it longer for better security"
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