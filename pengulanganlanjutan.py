# 1
# for i in range(1,11) :
#     if i % 2 != 0 :
#         print("angka ganjil pertama 1 sampai 10 adalah", i)
#         break        

# 2
# total = 0
    
# while True :    
#     i = int(input("masukan bilangan bulat positif (atau negatif untuk keluar): "))
    
#     if i < 0 : 
#         break
#     total += i 
# print("jumlah dari bilangan positif yang dimasukan adalah: ", total)

3
count = 0

for i in range(1, 51) :
    if i % 5 == 0 :
        print(i)            
        count += 1

    if count == 10 :
        break

