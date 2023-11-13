# Policy and CarPolicy Example

When designing larger systems it is often necessary to assign the implementation of different components to different individual programmmers or programming teams. 

If those programmers or teams do not follow the design specification precisely the resultant components/modules will not be able to talk to each other/pass messages to each other and the system will not work


The following assignment has two objectives
- To ensure you can follow a UML specification precisely to create the class that is described
- To ensure you can follow a UML specification to create a superclass i.e. a class that inherits from the base class or subclass
- To ensure you can implement the \__str__( ) method.
  
\__str__() is one of a number of magic methods - sometimes called "dunder" methods which can be overridden in order to make the resultant object behave in a particular way when used in a particular context.
in the case of the \__str__( ) function we control how the object behaves when used like a string - e.g. printed or concatenated.

The following UML diagrams describe different types of Insurance Policy. A general Policy and a CarPolicy which inherits the attributes and methods of the Policy class.

# Part 1
Create the classes as described in the UML diagram for the Policy Object

![alt text](Policy.png)

Follow the names of the classes, attributes and methods exactly as in the diagram

In the policy class the \__str__() function should return the policy number followed by a colon, then a space, followed by the name of the policy holder. So policy number 1234 held by John Smith should retrun "1234: John Smith"
The other two functions of the class are simple getters which will return the attributes they are associated with.

To run the test_policy.py program that is supplied type 

python -m ptyest test_policy.py

at the command prompt. You may have to run

pip install pytest 

to ensure pytest is installed

# Part 2
Create the Van class as it is described in the following diagram

![alt text](CarPolicy.png)

The get_engine_size_cc() and get_years_no_claims() functions are simple getters and return the attributes they are associated with.

The get_discount() function will return a figure representing the percentage discount to be applied if the driver have a certain number of years without claims. The function should return 20 if the drive has more than 5 years no claims and 0 in all other circumstances.

The get_discounted_premium() function applies the discount to the policy premium and return the discounted premium. E.g. if a driver's premium is €1000 but they have 7 years no claims the get_discounted_premium() funciton should apply a discount of 20 percent so the function should return 800. 

To run the test_car_policy.py program that is supplied type 

python -m ptyest test_car_policy.py
