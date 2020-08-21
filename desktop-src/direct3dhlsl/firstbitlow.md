---
title: firstbitlow function
description: Returns the location of the first set bit starting from the lowest order bit and working upward, per component.
ms.assetid: 204250f3-1a9b-445d-bd16-4cc9a5d9d60a
keywords:
- firstbitlow function HLSL
topic_type:
- apiref
api_name:
- firstbitlow
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# firstbitlow function

Returns the location of the first set bit starting from the lowest order bit and working upward, per component.

## Syntax

``` syntax
int firstbitlow(
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

The following overloaded versions are also available:

``` syntax
uint2 firstbitlow(uint2 value);
uint3 firstbitlow(uint3 value);
uint4 firstbitlow(uint4 value);
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

 

 