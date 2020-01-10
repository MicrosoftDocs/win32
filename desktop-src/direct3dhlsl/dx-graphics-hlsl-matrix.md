---
title: Matrix Type
description: A matrix is a special data type that contains between one and sixteen components. Every component of a matrix must be of the same type.
ms.assetid: 728eb472-103d-4c7f-b6f6-e515fc024801
keywords:
- Matrix Type HLSL
topic_type:
- apiref
api_name:
- Matrix Type
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Matrix Type

A matrix is a special data type that contains between one and sixteen components. Every component of a matrix must be of the same type.



|                         |
|-------------------------|
| **TypeComponents Name** |



 

## Components



| Item                                                                                                                             | Description                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TypeComponents"></span><span id="typecomponents"></span><span id="TYPECOMPONENTS"></span>**TypeComponents**<br/> | A single name that contains three parts. The first part is one of the [scalar](dx-graphics-hlsl-data-types.md) types. The second part is the number of rows. The third part is the number of columns. The number of rows and columns is a positive integer between 1 and 4 inclusive.<br/> |
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>                                         | An ASCII string that uniquely identifies the variable name.<br/>                                                                                                                                                                                                                            |



 

## Examples

Here are some examples:


```
int1x1    iMatrix;   // integer matrix with 1 row,  1 column
int4x1    iMatrix;   // integer matrix with 4 rows, 1 column
int1x4    iMatrix;   // integer matrix with 1 row, 4 columns
double3x3 dMatrix;   // double matrix with 3 rows, 3 columns

float2x2 fMatrix = { 0.0f, 0.1, // row 1
                     2.1f, 2.2f // row 2
                   };   
```



A matrix can be declared using this syntax also:


```
matrix <Type, Number> VariableName
```



The matrix type uses the angle brackets to specify the type, the number of rows, and the number of columns. This example creates a floating-point matrix, with two rows and two columns. Any of the scalar data types can be used.

Here is an example:


```
matrix <float, 2, 2> fMatrix = { 0.0f, 0.1, // row 1
                                 2.1f, 2.2f // row 2
                               };
```



## See also

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 





