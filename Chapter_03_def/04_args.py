# ပုံမှန်　def များတွင် parameters တစ်ခုလျှင် argument တစ်ခုထက်ပိုထည့်၍ မရ
# ဉပမာ def add(num1,num2) ဆိုပါက add(2,3,4) ဆိုပြီး arguments 3 ခုထည့်မရပေ

# number of arguments (args) များတွင်တော့ ထိုပြဿနာမရှိပေ 
# arguments ကြိုက်သလောက်ထည့်နိုင်သည်

def args_sample(*nums):
    print(nums)
    # nums ကို output ထုတ်သောအခါ ()ပုံစံ tuple form ဖြင့်ထုတ်ပေးသည်

args_sample(5,45,63,5,6)