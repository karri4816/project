num = int(input("enter a reading:"))

l,s = [],[]

if num % 10 > num // 10 and 12 < num < 90 :

    for i in range(12,90):
        
         if i % 10 > i // 10 and i > num :

            l.append(i)
     
         if i % 10 > i // 10 and i < num:
    
            s.append(i)

    print("next reading",min(l),"previous reading",max(s))

else:

    print("invalid reading")
     

