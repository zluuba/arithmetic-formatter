## Scientific Computing with Python - projects

Final projects of the "Scientific Computing with Python" course by [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/#scientific-computing-with-python-projects):
- [Arithmetic Formatter](https://github.com/zluuba/free-code-camp-projects/tree/main/arithmetic_formatter)
- [Time Calculator](https://github.com/zluuba/freeCodeCamp-projects/tree/main/time_calculator)
- [Budget App](https://github.com/zluuba/freeCodeCamp-projects/tree/main/budget_app)
- [Polygon Area Calculator](https://github.com/zluuba/freeCodeCamp-projects/tree/main/polygon_area_calculator)
- [Probability Calculator](https://github.com/zluuba/freeCodeCamp-projects/tree/main/probability_calculator)


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
Takes in start time, duration time and starting day of the week (optional), adds the duration time to the start time and returns the result.
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

The Polygon Area Calculator has a Rectangle class and a Square class (subclass of Rectangle) that has:
- Width and height attributes;
- Set width method - change width attribute;
- Set height method - change height attribute;
- Get area method - returns shape area;
- Get perimeter method - returns shape perimeter;
- Get diagonal method - returns shape diagonal;
- Get picture method - returns a string that represents the shape using lines of "*";
- Get amount inside method - returns the number of times the passed in shape could fit inside the shape (with no rotations);
- Set side method - only in a Square class, set width and height;

Usage example:
```ch
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
# 50

rect.set_height(3)
print(rect.get_perimeter())
# 26

print(rect)
# Rectangle(width=10, height=3)

print(rect.get_picture())
# **********
# **********
# **********

sq = shape_calculator.Square(9)
print(sq.get_area())
# 81

sq.set_side(4)
print(sq.get_diagonal())
# 5.656854249492381

print(sq)
# Square(side=4)

print(sq.get_picture())
# ****
# ****
# ****
# ****

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
# 8
```

### Probability Calculator

The Probability Calculator is a program to determining the approximate probability of drawing certain balls randomly from a hat.
The Hat class takes a variable number of arguments that specify the number of balls of each color that are in the hat.
Drew method accepts an argument indicating the number of balls to draw from the hat, removes balls at random from contents and returns those balls as a list of strings:
```ch
hat = Hat(yellow=3, blue=2, green=6)
print(hat.drew(2))
# ["blue", "green"]
```
Experiment function (outside the Hat class) returns a probability of certain balls falling out.
This is example of probability of two red and one green ball falling out of a hat that contains 6 black, 4 red and 3 green balls:
```ch
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
# 0.45
```

<br>

##### by [zluuba](https://www.freecodecamp.org/zluuba)