---
title: reversebits function
description: Reverses the order of the bits, per component.
ms.assetid: dad46e25-9980-4645-98eb-d834db704fc8
keywords:
- reversebits function HLSL
topic_type:
- apiref
api_name:
- reversebits
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# reversebits function

Reverses the order of the bits, per component.

## Syntax

``` syntax
uint reversebits(
  in uint value
);
```

## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **uint**

The input value.

</dd> </dl>

## Return value

Type: **uint**

The input value, with the bit order reversed.

## Remarks

The following overloaded versions are also available:

``` syntax
uint2 reversebits(uint2 value);
uint3 reversebits(uint3 value);
uint4 reversebits(uint4 value);
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

 

 




