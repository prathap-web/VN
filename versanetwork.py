def ispalindrome(str2):
    if str2 == str2[::-1]:
        return True
    return False


def check(str1):
    revers = str1[::-1]
    if ispalindrome(str1):
        return 0
    else:
        for i in range(len(str1)):
            if ispalindrome(str1 + revers[len(str1)-i:]):
                return i
                
print(check("abc"))
print("-" * 50)
print("code from geeks")


import sys
def findMinInsertions(str, l, h):  
	if (l > h): 
		return sys.maxsize
	if (l == h): 
		return 0
	if (l == h - 1): 
		return 0 if(str[l] == str[h]) else 1 
	if(str[l] == str[h]): 
		return findMinInsertions(str, l + 1, h - 1) 
	else: 
		return (min(findMinInsertions(str, l, h - 1),findMinInsertions(str, l + 1, h)) + 1) 

str = "abc"
print(findMinInsertions(str, 0, len(str) - 1)) 

    