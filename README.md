# Tkinter for JSON
This is a mini-project created as a "proof of concept" to show how you could create python tkinter GUIs by configuring widgets in a JSON like structure. In reflection, HTML5 has a similar and complementary data model and would of been a better option. I could of also used JSON itself instead of trying to create a new programming language. While it allows for nested objects (analagous to frames organised in a heirarchical struture in a Tkinter GUI), it only allows a single level of nesting as it doesn't feature recursion. To keep things simple, certain restricted characters were used to indicate the start and end of all objects but in reality, its hardly practical to indicate a number by placing two hashtags either side of it. 

Below you'll find the token rules that define some of the data types for the language. You can find the other data type definitions in `tokenRules.py`.

### String
```mermaid
graph TD;
A["Start String"] -->|1| B["Acceptable Character"];
A -->|2| C["Escape Character"];
A -->|3| D["End String"];
B -->|1| B;
B -->|2| C;
B -->|3| D;
C -->|1| B;
C -->|2| C;
C -->|3| D;
D -->|1| D;
```

### Function
```mermaid
graph TD;
A["Start Function"] --> |1| B["String.tokenRule"];
A --> |4| E["End Function"];
B --> |2| C["."];
C --> |3| D["String.tokenRule"];
D --> |4| E;
D --> |2| C;
E --> |4| E;
```

### Number
```mermaid
graph TD;
A["Start Number"] --> |1| B["-"];
B --> |2| C["[0-9]"];
C --> |3| D["."];
D --> |4| E["[0-9]"];
E --> |5| F["End Number"];
A --> |2| C;
A --> |5| F;
C --> |5| F;
C --> |2| C;
```

### subObject
```mermaid
graph TD;
A["Start  subObject"] --> |1| B["String.tokenRule"];
B --> |2| C[":"];
C --> |3| D["[String.tokenRule, Number.tokenRule, Function.tokenRule]"];
D --> |4| E[","];
E --> |5| F["End subObject"];
A --> |5| F;
D --> |5| F;
E --> |1| B; 
```





