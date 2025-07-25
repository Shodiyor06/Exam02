with open('input/numbers.txt', 'r') as file:
    sonlar= file.read().strip().split()

    resalt = max(sonlar,key=lambda x: int(x))
   
with open('Output/output09.txt', 'w') as file:
    file.write(f"faylar yozildi {resalt}")