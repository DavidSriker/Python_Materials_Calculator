# Materials Calculator
This simple implementation is meant for the easy calculation of reactants amount 
when the product amount is given.

This was created on Mac OS using python 3.X.

Dependncies:
**re**

#Usage:
1. Enter the product formula
2. Enter the amount in gram/milli-gram
3. Confirm the inputs
4. Enter the units desired
5. Enter the number of reactants
6. Enter each reactant formula

##Assumptions:
1. Each element that is not {H, C, O, N} can appear only in one reactants
2. The formulas are simple, meaning that there is no brackets etc.
3. It only support gram and milli-gram for now.

##Dummy Example:
Please provide the desired product formula: 
    Li7La3Zr2O12
    
Please provide the desired product amount: 
    1
    
product:  Li7La3Zr2O12  amount:  1.0
is this correct? [y/n]
    y

Which unit of measure for the amount entered:

1 - gram
2 - milli-gram

1

How many reactants there is? 

answer: 
4

Please enter the 1 reactant out of 4 :
Li2CO3

Please enter the 2 reactant out of 4 :
La2O3

Please enter the 3 reactant out of 4 :
ZrO2

Please enter the 4 reactant out of 4 :
Gd2O3

The reactant Gd2O3 is unnecessary

><===========================================>
>
>The amount of each reactant is as follows:
>
>0 : Li2CO3 - 0.3079699574035328 gram
>
>1 : La2O3 - 0.5819812299268465 gram
>
>2 : ZrO2 - 0.293476202781572 gram
>
>3 : Gd2O3 - 0.0 gram
>
><===========================================>
