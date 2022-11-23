# На вход программе подается строка, состоящая из чисел, разделенных одним пробелом. 
# Необходимо переместить все числа 0 в конец, сохраняя относительный порядок ненулевых элементов. 

import re
 
line = input()
new_nums = []
nums = re.findall(r'\d+', line)
nums = [int(element) for element in nums]
 
for num in nums:
    if num != 0:
        new_nums.append(num)
print(*new_nums, '0 ' * nums.count(0))
