# ထုတ်လိုသော ပုံစံများ

# form 1
#             *
#         *   *
#     *   *   *
# *   *   *   *

print("first")
for i in range(1,5):
    print("    "*(4-i)+"*   "*i)        

# form 2
# *   *   *   *   
#     *   *   *  
#         *   *
#             *
print("second")
for i in range(4):
    print("    "*i+"*   "*(4-i))

# form 3
#             *
#         *   *   *
#     *   *   *   *   *
# *   *   *   *   *   *   *

print("third")
for i in range(1,5):
    print("   "*(4-i)+"*  "*((2*i)-1))