
# Python Comparison Operators

### 1. Equal to **==**
- Checks if the value on the left is equal to value on the right.
**Example**
```py
print (11==11)
```

**Output:
#### Note! Comparison operators always result in a boolean value.
- For the code above since 11 is the same as the output of the code will be `True`.

### 2. Not Equal To **!=**
- Checks if the left side is **not equal to ** right side.
```py
print(6 != '6')   #Since text can not be equal to numbers, this line will print True
print(6 != 6)     #Both side equation is same,this will print False
```

### 3. Greater Sign **>**
- Checks if the left side is bigger than right side.
```py
print(5.0>5)  #False
print(3>4)    #False
print(10>9)   #True
```

### 4. Lower Sign **<**
- Checks if the left side is lower than right side.
```py
print(5.0<5)  #False
print(3<4)    #True
print(10<9)   #False
```

### 5. Less that equal <= || Greater Equal Sign >=
- Checks if the left side is smaller OR equal  **<=**
- Checks if the left side is bigger OR equal   **>=**
```py
print(5.0<=5)  #True
print(3<=4)    #True
print(10<=9)   #False
```

## Note !
- **Type Matters:**
- When comparing values types of the values also important:
For example: `5== '5' `  is `False` because one is str and one is number
 
- ** We can chain the comparison operators in python**
```py
print(1 < 2 < 3)  #True
```



