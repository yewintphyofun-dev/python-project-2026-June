# args ရော kwarg ကိုပါ ရောခေါ်သုံးခြင်း
# *args သည် tuple form ဖြစ်ပြီး
# **kwarg သည် dictionary form ဖြစ်လိမ့်မည်

def student_info(*args,**kwarg):
    print(args)
    print(kwarg)

student_info(23,43,54,54,"Mg Mg",id=1,name ="Maung Maung",age=18)
