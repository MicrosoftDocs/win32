---
title: Vector Type (HLSL)
description: A vector contains between one and four scalar components; every component of a vector must be of the same type.
ms.assetid: 16e66f3c-c513-4d03-8adf-463dc8d83e12
keywords:
- Vector Type HLSL
topic_type:
- apiref
api_name:
- Vector Type
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Vector Type

A vector is a data type that contains between one and four [scalar](dx-graphics-hlsl-scalar.md) components. Every component of a vector must be of the same type.

## Type Declaration

You can declare vector variables by using the [scalar type](dx-graphics-hlsl-scalar.md) name of the vector's contents with the number of components it contains:

```syntax
TypeComponents Name
```

Where `Type` is the [scalar type](dx-graphics-hlsl-scalar.md) of each of the components, `Components` is an constant integer expression between 1 and 4 inclusive indicating the number of components and `Name` is an ASCII string that uniquely identifies the variable name.

Examples:

```hlsl
int     iScalar;     // integer scalar
int1    iVector = 1; // vector containing one integer
float3  fVector = { 0.2f, 0.3f, 0.4f }; // vector containing three floats
```

## Template-style Declaration

An alternate declaration syntax uses the `vector` keyword and template arguments to indicate scalar type and number of components:

```syntax
vector <Type=float, Components=4> Name
```

Where again `Type` is the scalar type of each of the components, `Components` is an integer between 1 and 4 inclusive indicating the number of components, but they are specified within template-style angle brackets. `Name` is an ASCII string that uniquely identifies the variable name,

Note that the template parameter defaults allow specifying 4-component vectors of a given type by leaving off the last parameter or 4-component float vectors by leaving off both.

Here are some examples:

```hlsl
vector <int,    1> iVector = 1;
vector <double, 4> dVector = { 0.2f, 0.3f, 0.4f, 0.5f };
vector <float16_t> hVector = { 0.1f, 0.2f, 0.3f, 0.4f };     // Defaults to 4-component float16 vector
vector             fVector = { -0.4f, -0.3f, -0.2f, -0.1f }; // Defaults to 4-component float vector
```

## See also

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
