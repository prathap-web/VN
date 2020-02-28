def bubble_sort(coll,reverse=0):
    for i in range(len(coll)):
        for j in range(0,len(coll)-1):
            if coll[j] > coll[j+1]:
                coll[j],coll[j+1] = coll[j+1],coll[j]
    return coll

str1 = "zebra,xo,volley,ball,cat,dog,cas"
def listofstringsort(str1):
    lis = str1.split(",")
    #lis.sort(reverse = False)
    lisnew = bubble_sort(lis)
    joined = ",".join(lisnew)
    return joined
print(listofstringsort(str1))






