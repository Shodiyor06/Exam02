with open('input/numbers.txt', 'r') as file:
    sonlar= file.read().strip().split()
son_y = 0
for i in sonlar:
    son_y += int(i)

with open('Output/output08.txt', 'w') as file:
    file.write(f"faylar yozildi {son_y}")