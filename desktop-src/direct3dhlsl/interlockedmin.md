---
title: InterlockedMin function (HLSL reference)
description: Performs a guaranteed atomic min.
ms.assetid: a6d3d81c-45d7-4e15-b8ec-fa2e30f854ce
keywords:
- InterlockedMin function HLSL
topic_type:
- apiref
api_name:
- InterlockedMin
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InterlockedMin function (HLSL reference)

Performs a guaranteed atomic min.

## Syntax

``` syntax
void InterlockedMin(
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

Optional. The original input value.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This operation can only be performed on int and uint typed resources and shared memory variables. There are two possible uses for this function. The first is when R is a shared memory variable type. In this case, the function performs an atomic min of value to the shared memory register referenced by dest. The second scenario is when R is a resource variable type. In this scenario, the function performs an atomic min of value to the resource location referenced by dest. The overloaded function has an additional output variable which will be set to the original value of dest. This overloaded operation is only available when R is readable and writable.

Interlocked operations do not imply any memory fence/barrier.

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      |  x   |  x     |  x       | x     | x       |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




