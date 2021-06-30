---
title: Operators
description: Expressions are sequences of variables and literals punctuated by operators.
ms.assetid: c31aa0b8-1284-48aa-b000-d72433f0f5cc
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Operators

Expressions are sequences of [variables](dx-graphics-hlsl-variable-syntax.md) and literals punctuated by [operators](dx-graphics-hlsl-statement-blocks.md). Operators determine how the variables and literals are combined, compared, selected, and so on. The operators include:



| Operator name                                                                                | Operators                                                                   |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [Additive and Multiplicative Operators](#additive-and-multiplicative-operators) | +, -, \*, /, %                                                     |
| [Array Operator](#array-operator)                                               | \[i\]                                                              |
| [Assignment Operators](#assignment-operators)                                   | =, +=, -=, \*=, /=, %=                                             |
| [Binary Casts](#binary-casts)                                                   | C rules for float and int, C rules or HLSL intrinsics for bool     |
| [Bitwise Operators](#bitwise-operators)                                         | ~, <<, >>, &, \|, ^, <<=, >>=, &=, \|=, ^= |
| [Boolean Math Operators](#boolean-math-operators)                               | & &, \|\|, ?:                                                      |
| [Cast Operator](#cast-operator)                                                 | (type)                                                             |
| [Comma Operator](#comma-operator)                                               | ,                                                                  |
| [Comparison Operators](#comparison-operators)                                   | <, >, ==, !=, <=, >=                                   |
| [Prefix or Postfix Operators](#prefix-or-postfix-operators)                     | ++, --                                                             |
| [Structure Operator](#structure-operator)                                       | .                                                                  |
| [Unary Operators](#unary-operators)                                             | !, -, +                                                            |



 

Many of the operators are per-component, which means that the operation is performed independently for each component of each variable. For example, a single component variable has one operation performed. On the other hand, a four-component variable has four operations performed, one for each component.

All of the operators that do something to the value, such as + and \*, work per component.

The comparison operators require a single component to work unless you use the [**all**](dx-graphics-hlsl-all.md) or [**any**](dx-graphics-hlsl-any.md) intrinsic function with a multiple-component variable. The following operation fails because the if statement requires a single bool but receives a bool4:


```
if (A4 < B4)
```



The following operations succeed:


```
if ( any(A4 < B4) )
if ( all(A4 < B4) )
```



The binary cast operators [**asfloat**](dx-graphics-hlsl-asfloat.md), [**asint**](dx-graphics-hlsl-asint.md), and so on work per component except for [**asdouble**](asdouble.md) whose special rules are documented.

Selection operators like period, comma, and array brackets do not work per component.

Cast operators change the number of components. The following cast operations show their equivalence:


```
(float) i4 ->   float(i4.x)
(float4)i ->   float4(i, i, i, i)
```



## Additive and Multiplicative Operators

The additive and multiplicative operators are: +, -, \*, /, %


```
int i1 = 1;
int i2 = 2;
int i3 = i1 + i2;  // i3 = 3
i3 = i1 * i2;        // i3 = 1 * 2 = 2
```




```
i3 = i1/i2;       // i3 = 1/3 = 0.333. Truncated to 0 because i3 is an integer.
i3 = i2/i1;       // i3 = 2/1 = 2
```




```
float f1 = 1.0;
float f2 = 2.0f;
float f3 = f1 - f2; // f3 = 1.0 - 2.0 = -1.0
f3 = f1 * f2;         // f3 = 1.0 * 2.0 = 2.0
```




```
f3 = f1/f2;        // f3 = 1.0/2.0 = 0.5
f3 = f2/f1;        // f3 = 2.0/1.0 = 2.0
```



The modulus operator returns the remainder of a division. This produces different results when using integers and floating-point numbers. Integer remainders that are fractional will be truncated.


```
int i1 = 1;
int i2 = 2;
i3 = i1 % i2;      // i3 = remainder of 1/2, which is 1
i3 = i2 % i1;      // i3 = remainder of 2/1, which is 0
i3 = 5 % 2;        // i3 = remainder of 5/2, which is 1
i3 = 9 % 2;        // i3 = remainder of 9/2, which is 1
```



The modulus operator truncates a fractional remainder when using integers.


```
f3 = f1 % f2;      // f3 = remainder of 1.0/2.0, which is 0.5
f3 = f2 % f1;      // f3 = remainder of 2.0/1.0, which is 0.0
```



The % operator is defined only in cases where either both sides are positive or both sides are negative. Unlike C, it also operates on floating-point data types, as well as integers.

## Array Operator

The array member selection operator "\[i\]" selects one or more components in an array. It is a set of square brackets that contain a zero-based index.


```
int arrayOfInts[4] = { 0,1,2,3 };
arrayOfInts[0] = 2;
arrayOfInts[1] = arrayOfInts[0];
```



The array operator can also be used to access a vector.


```
float4 4D_Vector = { 0.0f, 1.0f, 2.0f, 3.0f  };         
float 1DFloat = 4D_Vector[1];          // 1.0f
```



By adding an additional index, the array operator can also access a matrix.


```
float4x4 mat4x4 = {{0,0,0,0}, {1,1,1,1}, {2,2,2,2}, {3,3,3,3} };
mat4x4[0][1] = 1.1f;
float 1DFloat = mat4x4[0][1];      // 0.0f
```



The first index is the zero-based row index. The second index is the zero-based column index.

## Assignment Operators

The assignment operators are: =, +=, -=, \*=, /=

Variables can be assigned literal values:


```
int i = 1;            
float f2 = 3.1f; 
bool b = false;
string str = "string";
```



Variables can also be assigned the result of a mathematical operation:


```
int i1 = 1;
i1 += 2;           // i1 = 1 + 2 = 3
```



A variable can be used on either side of the equals sign:


```
float f3 = 0.5f;
f3 *= f3;          // f3 = 0.5 * 0.5 = 0.25
```



Division for floating-point variables is as expected because decimal remainders are not a problem.


```
float f1 = 1.0;
f1 /= 3.0f;        // f1 = 1.0/3.0 = 0.333
```



Be careful if you are using integers that may get divided, especially when truncation affects the result. This example is identical to the previous example, except for the data type. The truncation causes a very different result.


```
int i1 = 1;
i1 /= 3;           // i1 = 1/3 = 0.333, which gets truncated to 0
```



## Binary Casts

Casting operation between int and float will convert the numeric value into the appropriate representations following C rules for truncating an int type. Casting a value from a float to an int and back to a float will result in a lossy conversion based on the precision of the target.

Binary casts may also be performed using [**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md), which reinterpret the bit representation of a number into the target data type.


```
asfloat() // Cast to float
asint()   // Cast to int 
asuint()  // Cast to uint
```



## Bitwise Operators

HLSL supports the following bitwise operators, which follow the same precedence as C with regard to other operators. The following table describes the operators.

> [!Note]  
> Bitwise operators require [Shader Model 4\_0](dx-graphics-hlsl-sm4.md) with Direct3D 10 and higher hardware.

 



| Operator          |  Function                 |
|-----------|-------------------|
| ~         | Logical Not       |
| <<  | Left Shift        |
| >>  | Right Shift       |
| &         | Logical And       |
| \|        | Logical Or        |
| ^         | Logical Xor       |
| <<= | Left Shift Equal  |
| >>= | Right Shift Equal |
| &=        | And Equal         |
| \|=       | Or Equal          |
| ^=        | Xor Equal         |



 

Bitwise operators are defined to operate only on int and uint data types. Attempting to use bitwise operators on float, or struct data types will result in an error.

## Boolean Math Operators

The Boolean math operators are: &&, \|\|, ?:


```
bool b1 = true;
bool b2 = false;
bool b3 = b1 && b2 // b3 = true AND false = false
b3 = b1 || b2                // b3 = true OR false = true
```



Unlike short-circuit evaluation of &&, \|\|, and ?: in C, HLSL expressions never short-circuit an evaluation because they are vector operations. All sides of the expression are always evaluated.

Boolean operators function on a per-component basis. This means that if you compare two vectors, the result is a vector containing the Boolean result of the comparison for each component.

For expressions that use Boolean operators, the size and component type of each variable are promoted to be the same before the operation occurs. The promoted type determines the resolution at which the operation takes place, as well as the result type of the expression. For example an int3 + float expression would be promoted to float3 + float3 for evaluation, and its result would be of type float3.

## Cast Operator

An expression preceded by a type name in parenthesis is an explicit type cast. A type cast converts the original expression to the data type of the cast. In general, the simple data types can be cast to the more complex data types (with a promotion cast), but only some complex data types can be cast into simple data types (with a demotion cast).

Only right hand side type casting is legal. For example, expressions such as `(int)myFloat = myInt;` are illegal. Use `myFloat = (float)myInt;` instead.

The compiler also performs implicit type cast. For example, the following two expressions are equivalent:


```
int2 b = int2(1,2) + 2;
int2 b = int2(1,2) + int2(2,2);
```



## Comma Operator

The comma operator (,) separates one or more expressions that are to be evaluated in order. The value of the last expression in the sequence is used as the value of the sequence.

Here is one case worth calling attention to. If the constructor type is accidentally left off the right side of the equals sign, the right side now contains four expressions, separated by three commas.


```
// Instead of using a constructor
float4 x = float4(0,0,0,1); 

// The type on the right side is accidentally left off
float4 x = (0,0,0,1); 
```



The comma operator evaluates an expression from left to right. This reduces the right hand side to:


```
float4 x = 1; 
```



HLSL uses scalar promotion in this case, so the result is as if this were written as follows:


```
float4 x = float4(1,1,1,1);
```



In this instance, leaving off the float4 type from the right side is probably a mistake that the compiler is unable to detect because this is a valid statement.

## Comparison Operators

The comparison operators are: <, >, ==, !=, <=, >=.

Compare values that are greater than (or less than) any scalar value:


```
if( dot(lightDirection, normalVector) > 0 )
   // Do something; the face is lit
```




```
if( dot(lightDirection, normalVector) < 0 )
   // Do nothing; the face is backwards
```



Or, compare values equal to (or not equal to) any scalar value:


```
if(color.a == 0)
   // Skip processing because the face is invisible

if(color.a != 0)
   // Blend two colors together using the alpha value
```



Or combine both and compare values that are greater than or equal to (or less than or equal to) any scalar value:


```
if( position.z >= oldPosition.z )
   // Skip the new face because it is behind the existing face
```




```
if( currentValue <= someInitialCondition )
   // Reset the current value to its initial condition
```



Each of these comparisons can be done with any scalar data type.

To use comparison operators with vector and matrix types, use the [**all**](dx-graphics-hlsl-all.md) or [**any**](dx-graphics-hlsl-any.md) intrinsic function.

This operation fails because the if statement requires a single bool but receives a bool4:


```
if (A4 < B4)
```



These operations succeed:


```
if ( any(A4 < B4) )
if ( all(A4 < B4) )
```



## Prefix or Postfix Operators

The prefix and postfix operators are: ++, --. Prefix operators change the contents of the variable before the expression is evaluated. Postfix operators change the contents of the variable after the expression is evaluated.

In this case, a loop uses the contents of i to keep track of the loop count.


```
float4 arrayOfFloats[4] = { 1.0f, 2.0f, 3.0f, 4.4f };

for (int i = 0; i<4; )
{
    arrayOfFloats[i++] *= 2; 
}
```



Because the postfix increment operator (++) is used, arrayOfFloats\[i\] is multiplied by 2 before i is incremented. This could be slightly rearranged to use the prefix increment operator. This one is harder to read, although both examples are equivalent.


```
float4 arrayOfFloats[4] = { 1.0f, 2.0f, 3.0f, 4.4f };

for (int i = 0; i<4; )
{
    arrayOfFloats[++i - 1] *= 2; 
}
```



Because the prefix operator (++) is used, arrayOfFloats\[i+1 - 1\] is multiplied by 2 after i is incremented.

The prefix decrement and postfix decrement operator (--) are applied in the same sequence as the increment operator. The difference is that decrement subtracts 1 instead of adding 1.

## Structure Operator

The structure member selection operator (.) is a period. Given this structure:


```
struct position
{
float4 x;
float4 y;
float4 z;
};
```



It can be read like this:


```
struct position pos = { 1,2,3 };

float 1D_Float = pos.x
1D_Float = pos.y
```



Each member can be read or written with the structure operator:


```
struct position pos = { 1,2,3 };
pos.x = 2.0f;
pos.z = 1.0f;       // z = 1.0f
pos.z = pos.x      // z = 2.0f
```



## Unary Operators

The unary operators are: !, -, +

Unary operators operate on a single operand.


```
bool b = false;
bool b2 = !b;      // b2 = true
int i = 2;
int i2 = -i;       // i2 = -2
int j = +i2;       // j = +2
```



## Operator Precedence

When an expression contains more than one operator, operator precedence determines the order of evaluation. Operator precedence for HLSL follows the same precedence as C.

## Remarks

Curly braces ({,}) start and end a statement block. When a statement block uses a single statement, the curly braces are optional.

## Related topics

<dl> <dt>

[Statements (DirectX HLSL)](dx-graphics-hlsl-statements.md)
</dt> </dl>

 

 




