def binarysearch(l,x):
    mid=len(l)//2
    if x==l[mid]:
        return mid
    elif x<l[mid]:
        # print("list",l[:mid])
        # print("length",len(l[:mid])//2)
        return binarysearch(l[:mid],x)
    elif x>l[mid]:
        # print("list",l[mid:])
        # print("length",len(l[mid+1:]) // 2)
        return binarysearch(l[mid:],x)+mid


s=[2,8,7,6,1,9,52,17,3,5]
s.sort()
print(s)
num=int(input("enter the number you want ot search:-"))
print(binarysearch(s,num))

