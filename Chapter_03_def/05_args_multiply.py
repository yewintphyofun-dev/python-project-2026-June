# အမြှောက် def တစ်ခုရေးကြည့်မည်

def multi(*nums):
    total = 1
    for num in nums:
        total *= num
    return total

ans = multi(4,5,3,5,6)
print(ans)