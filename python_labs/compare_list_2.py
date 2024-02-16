list2=['V1', 'V2', 'V300', 'V300', 'V301','V301']
for i in range(len(list2)):   
     for j in range(i+1,len(list2)): 
          if(list2[i]==list2[j]):
              print("SAME")