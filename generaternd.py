import random

# The number length should be size of the array * #!/usr/bin/env python3
# In our case this would be 144 * 144 * 3 * 3
num_length = 186624 


str1="1"
for i in range (num_length):
    str1+=(str(random.randint(0,9)))

print(str1)
