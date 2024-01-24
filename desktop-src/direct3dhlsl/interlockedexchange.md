---
title: InterlockedExchange function (HLSL reference)
description: Assigns value to dest and returns the original value.
ms.assetid: 1e7ce7ff-9e23-47fa-8e76-713f6bf57abf
keywords:
- InterlockedExchange function HLSL
topic_type:
- apiref
api_name:
- InterlockedExchange
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InterlockedExchange function (HLSL reference)

Assigns value to dest and returns the original value.

## Syntax

``` syntax
void InterlockedExchange(
  in  R dest,
  in  T value,
  out T original_value
);
```

## Parameters

<dl> <dt>

*dest* \[in\]
</dt> <dd>

Type: **R**

The destination address.

</dd> <dt>

*value* \[in\]
</dt> <dd>

Type: **T**

The input value.

</dd> <dt>

*original\_value* \[out\]
</dt> <dd>

Type: **T**

The original value.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This operation can only be performed on scalar-typed resources and shared memory variables. There are two possible uses for this function. The first is when R is a shared memory variable type. In this case, the function performs the operation on the shared memory register referenced by dest. The second scenario is when R is a resource variable type. In this scenario, the function performs the operation on the resource location referenced by dest. This operation is only available when R is readable and writable.

Interlocked operations do not imply any memory fence/barrier.

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      |  x   | x      |  x       | x     | x       |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




