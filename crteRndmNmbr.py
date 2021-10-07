# import random
import random as rand
import math

# print(rand.random())

# *** 100 udaa shoo hayahad suld buuh magadlaliig ol ***

"""count = 0

for i in range(100):
    if rand.random() > 0.5:
        count += 1
print(
    "100 udaa shoo hayahad suld buuh magadlal n {} buyu {}% baina.".format(
        count, math.ceil(count)
    )
)"""

# *** Uniform function ***
# Jigd tarhaltiin function

"""print(rand.uniform(1, 11))

count = 0

for i in range(10000):
    if rand.random() > 0.5:
        count = rand.uniform(1, 5)
print(
    "100 udaa shoo hayahad suld buuh magadlal n {} buyu {}% baina.".format(
        count, math.ceil(count)
    )
)"""

# *** Expovariate function ***
# Exponential tarhalt buyu hazailtiig ilerhiileh function

print(rand.expovariate(lambd=32))

# *** With Range ***

"""print(rand.randrange(10, 100))

print(rand.randrange(0, 100, 3))"""

## *** Example with Deck ***

"""deck = list(range(2, 11)) * 4
print(deck)
rand.shuffle(deck)
print(deck)

my_deck = []

while True:
    my_deck.append(deck.pop())
    if sum(my_deck) > 19:
        break
print((my_deck))"""

## *** Lottery ***

lottery = ["chinzo", "ulzii", "enkhee", "puje", "enzo"]

index = rand.randrange(0, 3)
print(index)
print("The human buy a drink from shop is {}.".format(lottery[index]))


print("The human buy a drink from shop is {}.".format(rand.choice(lottery)))
