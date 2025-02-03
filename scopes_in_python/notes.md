## Scoping in python
### Global Scoping
1. **Global scoping** is done in the main body of the code. The global variables are available from with in any scope of the code.


### Local Scoping
1. **Local Scoping** is done within a function of a code. The Local variables are available in the local scope.


---
suppose there is a city, which is a global scope and in city there are many houses which are local scopes. Now a variable nikhil_1 present in global scope and variable with nikhil_2 present in local scope, even if the variables have similar names they are not same.\
The work done in local scope will treat variable nikhil_2, and work done in global scope will treat variable nikhil_1.\
Now inside a house, rooms could be present; the variables in this room or scope can be accessed by main scope i.e in local scope, but cannot be accessed by global scope. But Global scope variables can be accessed by houses and even rooms.

---