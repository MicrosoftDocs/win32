---
title: asuint function
description: Reinterprets the bit pattern of a 64-bit value as two unsigned 32-bit integers.
ms.assetid: 29671661-4fec-46e5-9b6f-56fba8e1d756
keywords:
- asuint function HLSL
topic_type:
- apiref
api_name:
- asuint
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# asuint function

Reinterprets the bit pattern of a 64-bit value as two unsigned 32-bit integers.

## Syntax

``` syntax
void asuint(
  in  double value,
  out uint lowbits,
  out uint highbits
);
```

## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **double**

The input value.

</dd> <dt>

*lowbits* \[out\]
</dt> <dd>

Type: **uint**

The low 32-bit pattern of *value*.

</dd> <dt>

*highbits* \[out\]
</dt> <dd>

Type: **uint**

The high 32-bit pattern of *value*.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function is an alternate version of the [**asuint**](dx-graphics-hlsl-asuint.md) intrinsic that has been available in earlier shader models, and was introduced for Shader Model 5. The original function (recognized in the HLSL compiler by its different signature) remains available to Shader Model 5.

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

[**asuint (DirectX HLSL)**](dx-graphics-hlsl-asuint.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




