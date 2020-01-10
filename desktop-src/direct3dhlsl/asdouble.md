---
title: asdouble function
description: Reinterprets a cast value (two 32-bit values) into a double.
ms.assetid: 55e5276d-81e1-4e7e-8cb4-0beb57d2fb7f
keywords:
- asdouble function HLSL
topic_type:
- apiref
api_name:
- asdouble
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# asdouble function

Reinterprets a cast value (two 32-bit values) into a double.

## Syntax

``` syntax
double asdouble(
  in uint lowbits,
  in uint highbits
);
```

## Parameters

<dl> <dt>

*lowbits* \[in\]
</dt> <dd>

Type: **uint**

The low 32-bit pattern of the input value.

</dd> <dt>

*highbits* \[in\]
</dt> <dd>

Type: **uint**

The high 32-bit pattern of the input value.

</dd> </dl>

## Return value

Type: **double**

The input (two 32-bit values) recast as a double.

## Remarks

The following overloaded version is also available:

``` syntax
double2 asdouble(uint2 lowbits, uint2 highbits);
```

If the input value is two 32-bit components, the return type will contain one double. If the input value is four 32-bit components, the return type will contain two doubles. If the input value is a 64-bit type, the returned value will have the same number of components as the input value.

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

 

 




