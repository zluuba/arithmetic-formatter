## Scientific Computing with Python - projects

Final projects of the "Scientific Computing with Python" course by [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/#scientific-computing-with-python-projects):
- [Arithmetic Formatter](https://github.com/zluuba/free-code-camp-projects/tree/main/arithmetic_formatter)
- [Time Calculator](https://github.com/zluuba/freeCodeCamp-projects/tree/main/time_calculator)
- [Budget App](https://github.com/zluuba/freeCodeCamp-projects/tree/main/budget_app)
- [Polygon Area Calculator](#)
- [Probability Calculator](#)


### Arithmetic Formatter
Receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 
The optional second argument displays the answers when set to True.
Examples:

```ch
# Function Call
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

# Output
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

```ch
# Function Call
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

# Output
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```


### Time Calculator
Takes in start time, duration time and starting day of the week (optional), add the duration time to the start time and return the result.
Written in pure python (without any libraries).
Examples:

```ch
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

### Budget App
The Budget App has a Category class that has:
- Deposit method - adds an object (amount and description) to the ledger list;
- Withdraw method - adds an object (amount and description) to the ledger list, but with a negative amount;
- Get balance method - returns the current balance of the budget category;
- Transfer method - adds a withdrawal and a deposit to the other budget category (if there are enough funds);
- Check funds method - returns False if the amount is greater than the balance of the budget category and returns True otherwise;

When the budget object is printed, it displays check of the following type:
```ch
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the Category class, there is a function (outside the class) called create_spend_chart.
The chart shows the percentage of spending in each category passed to the function:
```ch
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

### Polygon Area Calculator

Not ready yet


<br>

##### by [zluuba](https://www.freecodecamp.org/zluuba)