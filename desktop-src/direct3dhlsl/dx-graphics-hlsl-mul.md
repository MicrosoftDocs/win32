---
title: mul
description: Multiplies x and y using matrix math. The inner dimension x-columns and y-rows must be equal.
ms.assetid: 9945388a-d802-4dbe-bdb7-4eadb8751c39
keywords:
- mul HLSL
topic_type:
- apiref
api_name:
- mul
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# mul

Multiplies x and y using matrix math. The inner dimension x-columns and y-rows must be equal.



| ret mul(x, y) |
|---------------|



 

## Parameters



| Item                                                   | Description                                                                           |
|--------------------------------------------------------|---------------------------------------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The x input value. If x is a vector, it treated as a row vector.<br/>    |
| <span id="y"></span><span id="Y"></span>*y*<br/> | \[in\] The y input value. If y is a vector, it treated as a column vector.<br/> |



 

## Return Value

The result of x times y. The result has the dimension x-rows x y-columns.

## Type Description

There are 9 overloaded versions of this function; the overloaded versions handle the different cases for the types and sizes of the input arguments.



| Version | Name | Purpose | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md) | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                                                                     |
|---------|------|---------|---------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------|
| 1       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | scalar                                                        | float, int                                                     | 1                                                                        |
|         | y    | in      | scalar                                                        | same as input x                                                | 1                                                                        |
|         | ret  | out     | scalar                                                        | same as input x                                                | 1                                                                        |
| 2       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | scalar                                                        | float, int                                                     | 1                                                                        |
|         | y    | in      | vector                                                        | float, int                                                     | any                                                                      |
|         | ret  | out     | vector                                                        | float, int                                                     | same dimension(s) as input y                                             |
| 3       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | scalar                                                        | float, int                                                     | 1                                                                        |
|         | y    | in      | matrix                                                        | float, int                                                     | any                                                                      |
|         | ret  | out     | matrix                                                        | same as input y                                                | same dimension(s) as input y                                             |
| 4       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | vector                                                        | float, int                                                     | any                                                                      |
|         | y    | in      | scalar                                                        | float, int                                                     | 1                                                                        |
|         | ret  | out     | vector                                                        | float, int                                                     | same dimension(s) as input x                                             |
| 5       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | vector                                                        | float, int                                                     | any                                                                      |
|         | y    | in      | vector                                                        | float, int                                                     | same dimension(s) as input x                                             |
|         | ret  | out     | scalar                                                        | float, int                                                     | 1                                                                        |
| 6       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | vector                                                        | float, int                                                     | any                                                                      |
|         | y    | in      | matrix                                                        | float, int                                                     | rows = same dimension(s) as input x, columns = any                       |
|         | ret  | out     | vector                                                        | float, int                                                     | same dimension(s) as input y columns                                     |
| 7       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | matrix                                                        | float, int                                                     | any                                                                      |
|         | y    | in      | scalar                                                        | float, int                                                     | 1                                                                        |
|         | ret  | out     | matrix                                                        | float, int                                                     | same dimension(s) as input x                                             |
| 8       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | matrix                                                        | float, int                                                     | any                                                                      |
|         | y    | in      | vector                                                        | float, int                                                     | number of columns in input x                                             |
|         | ret  | out     | vector                                                        | float, int                                                     | number of rows in input x                                                |
| 9       |      |         |                                                               |                                                                |                                                                          |
|         | x    | in      | matrix                                                        | float, int                                                     | any                                                                      |
|         | y    | in      | matrix                                                        | float, int                                                     | rows = number of columns in input x                                      |
|         | ret  | out     | matrix                                                        | float, int                                                     | rows = number of rows in input x, columns = number of columns in input y |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported |
|------------------------------------------------------------------------------------|-----------|
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) and higher shader models | yes       |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





