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

A matrix is a data type that contains between one and sixteen [scalar](dx-graphics-hlsl-scalar.md) components in a two dimensional grid. Every component of a matrix must be of the same type.

## Type Declaration

You can declare matrix variables by using the [scalar type](dx-graphics-hlsl-scalar.md) name of the matrix's contents with the number of rows and columns it contains:

```syntax
TypeRowsCols Name
```

Where `Type` is the [scalar type](dx-graphics-hlsl-scalar.md) of each of the components, `Rows` is a constant integer expression between 1 and 4 inclusive indicating the number of rows, `Cols` is a constant integer expression between 1 and 4 inclusive indicating the number of columns and `Name` is an ASCII string that uniquely identifies the variable name.

Examples:

```hlsl
int1x1    iMatrix;   // integer matrix with 1 row,  1 column, 1 single component
int4x1    iMatrix;   // integer matrix with 4 rows, 1 column, 4 total components
int1x4    iMatrix;   // integer matrix with 1 row, 4 columns, 4 total components
double3x3 dMatrix;   // double matrix with 3 rows, 3 columns, 9 total components

float3x2 fMatrix = { 0.0f, 0.1f, // row 1
                     2.1f, 2.2f, // row 2
                     4.1f, 4.2f  // row 3
                   };   
```

## Template-style Declaration

An alternate declaration syntax uses the `matrix` keyword and template arguments to indicate scalar type, number of rows and number of columns:

```syntax
matrix <Type=float, Rows=4, Cols=4> Name
```

Where `Type` is the [scalar type](dx-graphics-hlsl-scalar.md) of each of the components, `Rows` is an integer between 1 and 4 inclusive indicating the number of rows, `Cols` is an integer between 1 and 4 inclusive indicating the number of columns, but they are specified within template-style angle brackets. `Name` is an ASCII string that uniquely identifies the variable name.

Note that the template parameter defaults allow specifying 4-column matrtices of a given type and row count by leaving off the last parameter, a 4x4 matrix of a given type by leaving off the last two template parameters or 4x4 float matrices by leaving off all three.

Examples:

```hlsl
matrix <int, 1, 1>   iMatrix = { 1 }; 
matrix <float, 2, 3> fMatrix = { 0.0f, 0.1f, 0.2f, // row 1
                                 2.1f, 2.2f, 2.3f  // row 2
                               };
matrix<int16_t, 1>   sMatrix = { 1, 2, 3, 4 }; // Defaults to 1x4 int16 matrix
matrix<float16_t>    hMatrix = { 0.0f, 0.1f, 0.2f, 0.3f, // Defaults to 4x4 float16 matrix
                                 1.0f, 1.1f, 1.2f, 1.3f,
                                 2.0f, 2.1f, 2.2f, 2.3f,
                                 3.0f, 3.1f, 3.2f, 3.3f }; 
matrix               fMatrix = { 0.0f, 0.1f, 0.2f, 0.3f, // Defaults to 4x4 float matrix
                                 1.0f, 1.1f, 1.2f, 1.3f,
                                 2.0f, 2.1f, 2.2f, 2.3f,
                                 3.0f, 3.1f, 3.2f, 3.3f }; 
```

## See also

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
