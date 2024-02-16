list = ["V1_abcd","V2_cejn","V300_dnmewx","V300_cenjc","V301_ceiknce"]
j=0
list2=[]
count=len(list2)
list3=[]
count=len(list)
def file_read():
    if len(list)!="null":
        for i in list:
            k=i.split("_")
            list2.append(k[1])
        print(list2)
    else:
        print("list is empty!!")
file_read()