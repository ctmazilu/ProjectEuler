total = []
for i in range(10):
    if i%3==0 or i%5==0:
        total.append(i)
print(max(total))
print(sum(total))


