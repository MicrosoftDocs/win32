---
title: firstbithigh function
description: Gets the location of the first set bit starting from the highest order bit and working downward, per component.
ms.assetid: 0fa89a9e-1706-44f7-8dd3-c37af5c11ddc
keywords:
- firstbithigh function HLSL
topic_type:
- apiref
api_name:
- firstbithigh
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# firstbithigh function

Gets the location of the first set bit starting from the highest order bit and working downward, per component.

## Syntax

``` syntax
int firstbithigh(
  in int value
);
```

## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **[**int**](/windows/desktop/WinProg/windows-data-types)**

The input value.

</dd> </dl>

## Return value

Type: **[**int**](/windows/desktop/WinProg/windows-data-types)**

The location of the first set bit.

## Remarks

For a signed integer, the first significant bit is zero for a negative number.

The following overloaded versions are also available:

``` syntax
int2 firstbithigh(int2 value);
int3 firstbithigh(int3 value);
int4 firstbithigh(int4 value);
uint firstbithigh(uint value);
uint2 firstbithigh(uint2 value);
uint3 firstbithigh(uint3 value);
uint4 firstbithigh(uint4 value);
```

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 