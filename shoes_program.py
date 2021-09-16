import time
pair = 0
cost = 0
print("|---------------------|")
print("  AMAN SHOES STORE  ")
print("|---------------------|")
name = str(input("Enter your name here\n"))
phone = (input("Enter your mobile number here\n"))
adress = str(input("Enter your address\n"))
time.sleep(0.5)
print("THANK YOU!")
print("for entering information here!")

i = 1
print("we have many types of varities available for our shoes. like:\n")
print("[1]. Sports [2]. Sneakers [3].Formal  [4].Informal [5].Dancing and many more")
type = str(input("Enter the type of shoes do you want?\n"))
if type == "sports" :
        print("How Much pair do you want?")
        pair = int(input())
        price = int(500)
        cost = pair*price
        print("The price of your",type,"shoes is",cost)
        # f = open("shoes.txt","a")
        # f.write(type)
        # f.close()

elif type == "sneakers" :
        print("How Much pair do you want?")
        pair = int(input())
        price = int(600)
        cost = pair*price
        print("The price of your",type,"shoes is",cost)

elif type == "formal" :
        print("How Much pair do you want?")
        pair = int(input())
        price = int(800)
        cost = pair*price
        print("The price of your",type,"shoes is",cost)

elif type == "informal" :
        print("How Much pair do you want?")
        pair = int(input())
        price = int(1000)
        cost = pair*price
        print("The price of your",type,"shoes is",cost)

elif type == "dancing" :
        print("How Much pair do you want?")
        pair = int(input())
        price = int(1200)
        cost = pair*price
        print("The price of your",type,"shoes is",cost)

time.sleep(2)
def print_bill() :
        print("|---------------------|")
        print("  AMAN SHOES STORE  ")
        print("|---------------------|")
        print("|Name :-",name)
        print("|Phone :-",phone)
        print("|Address :-",adress)
        print("|Shoes :-",type)
        print("|Pair :-",pair)
        print("|Cost :-",cost)

print_bill()

f = open("shoes.txt","a")
f.write(name)
f.write("\n")
f.write(phone)
f.write("\n")
f.write(adress)
f.write("\n")
f.write(type)
f.write("\n")
f.write(str(pair))
f.write("\n")
f.write(str(cost))
f.write("\n")


f.close()



















    






