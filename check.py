import csv
import os.path
missing = answer = 0

if os.path.isfile("follower.csv") == False:
    print("\"follower.csv\" is missing")
    missing=1
if os.path.isfile("following.csv") == False:
    print("\"following.csv\" is missing")
    missing=1
    
if missing == 1:
    print("Something went wrong, refer to \"readme.txt\" for further informations.")
    input()
    exit()

same = []
invert = []

follower = []
with open('follower.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for ligne in spamreader:
        follower.append(ligne)
following = []
with open('following.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for ligne in spamreader:
        following.append(ligne)

if follower >= following:
    #print("more follower than following")
    biggest = follower
    smallest = following
else:
    #print("more following than follower")
    biggest = following
    smallest = follower

for i in range(len(biggest)):
    for j in range(len(smallest)):
        if biggest[i][0] == smallest[j][0]:
            same.append(biggest[i][0])
            pass
    invert.append(biggest[i][0])

print(f"Follow Back: {len(same)} | Don't follow Back: {len(invert)} | Total: {len(same)+len(invert)}\n----")

answer = input("save these results as  files ? y/n \n")
print("Follow Back:")

if answer == "y":
    with open('Follow Back.txt', 'w') as f:
        for i in range(len(same)):
            print(f"{same[i]} | https://www.instagram.com/{same[i]}/")
            f.write(f"{same[i]} | https://www.instagram.com/{same[i]}/ \n")
else:
    for i in range(len(same)):
        print(f"{same[i]} | https://www.instagram.com/{same[i]}/")

            
if answer == "y":
    with open('X Follow Back.txt', 'w') as f:
        for i in range(len(invert)):
            f.write(f"{invert[i]} | https://www.instagram.com/{invert[i]}/ \n")
if answer == "y":
    print("\nFollow Back saved as \"Follow Back.txt\".\nDon't follow Back saved as \"X Follow Back.txt\".")
input("")
