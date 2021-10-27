with open('файл') as f:
    nums = []
    for line in f:
        nums.append(int(line))

med = sorted(nums)[len(nums) // 2]
print(sum(abs(num - med) for num in nums))
