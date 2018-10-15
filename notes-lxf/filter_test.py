nums = [1,2,3,4,5,6,7,8,9]

def is_odd(n):
	return n % 2 == 1
    
f = filter(is_odd,nums)
print(f)
print(list(f))

s = sorted(nums,reverse=True)
print(list(s))

s = ["Aabc","cd","ddd","abd","cf","aa","acd","c3","de","acs","ccc","ss"]

s = sorted(s,key=str.lower)
print(list(s))
