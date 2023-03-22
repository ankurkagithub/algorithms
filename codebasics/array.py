# 1.Let us say your expense for every month are listed below,

# January - 2200

# February - 2350

# March - 2600

# April - 2130

# May - 2190


################################# Solution #################################
task = 0
# Create a list to store these monthly expenses and using that find out,
expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
task += 1
print("Task: ", task )
feb_variance = expense[1] - expense[0]
print("Feb Variance: ", feb_variance)

# 2. Find out your total expense in first quarter (first three months) of the year.
task += 1
print("Task: ", task )
quarter_sum = 0
for i in range(3):
    quarter_sum += expense[i]
print("Quarter sum: ", quarter_sum)

# 3. Find out if you spent exactly 2000 dollars in any month
task += 1
print("Task: ", task )
# linear search or brute force
target = 2000
found = False
i = 0
while not found and i < len(expense):
    if expense[i] == target:
        found = True
        print("Value found!")
    i += 1


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
task += 1
print("Task: ", task )
june = 1980
print("Expenses Before: ", expense)
expense.append(june)
print("Expenses After: ", expense)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
task += 1
print("Task: ", task )
new_april = expense[3] - 200
print("Expenses Before: ", expense)
expense[3] = new_april
print("Expenses After: ", expense)
