with open('input/numbers.txt', 'r') as file:
    sonlar= file.read().strip().split()

    resalt = sorted(sonlar)
with open('Output/output10.txt', 'w') as file:
    file.write(f"faylar yozildi {resalt}")