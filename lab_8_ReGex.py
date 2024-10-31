import re

#1. [] – Square Brackets
pattern = "[abc]"
string = "abcabc"
result = re.match(pattern, string)
print(result)


#2. . – Period (menghitung/mencocokkan karakter)
pattern = "..."
string = "abc"
result = re.match(pattern, string)
print(result)

 
#3. ^ – Caret
pattern = "^a...s$" #$ untuk mengecek jika string diakhiri oleh karakter tertentu
string = "aris"
result = re.match(pattern, string)
print(result)


#5. * – Star
pattern = "a[0-9]*[0-9]" 
string = "H071241065"
result = re.match(pattern, string)
print(result)


#6. + – Plus
#Simbol + akan mencocokkan satu atau lebih kemunculan pola yang tersisa
pattern = "mak+n" 
string = "makkkkn"
result = re.match(pattern, string)
print(result)


#7. ? – Question Mark
# Simbol ? akan mencocokkan nol atau lebih kemunculan string sebelum pola
# pada regex.
pattern = "mak?n" 
string = "makkkkn"
result = re.match(pattern, string)
print(result)


#8. {m, n} – Braces
# RegEx ini akan mencari repetisi setidaknya n dan sebanyak m dari pola yang
# tersisa.
pattern = "a{2,3}" #tidak boleh ada spasi antara {2,3}
string = "makan"
result = re.match(pattern, string)
print(result)
    
    
#9. | – Alternation
# Simbol | sama seperti operator or
pattern = "a|b"
string = "anm"
result = re.match(pattern, string)
print(result)
    
    
#10. () – Group
# Simbol () digunakan untuk mengelompokkan pola regex. Contoh, (a|b|c)xy
# akan mencocokka
pattern = "(a|b)xy"
string = "axy bxh"
result = re.match(pattern, string)
print(result)
    

