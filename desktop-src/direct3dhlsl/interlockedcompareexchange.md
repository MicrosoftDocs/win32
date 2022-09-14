---
title: InterlockedCompareExchange function (HLSL reference)
description: Atomically compares the destination with the comparison value. If they are identical, the destination is overwritten with the input value. The original value is set to the destination's original value.
ms.assetid: 85d1ba58-8e79-41cd-abd6-7ffff59839c7
keywords:
- InterlockedCompareExchange function HLSL
topic_type:
- apiref
api_name:
- InterlockedCompareExchange
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InterlockedCompareExchange function (HLSL reference)

Atomically compares the destination with the comparison value. If they are identical, the destination is overwritten with the input value. The original value is set to the destination's original value.

## Syntax

``` syntax
void InterlockedCompareExchange(
  in  R dest,
  in  T compare_value,
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

*compare\_value* \[in\]
</dt> <dd>

Type: **T**

The comparison value.

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

Atomically compares the value referenced by *dest* with *compare\_value*, stores *value* in the location referenced by *dest* if the values match, returns the original value of *dest* in *original\_value*. This operation can only be performed on **int** or **uint** typed resources and shared memory variables. There are two possible uses for this function. The first is when R is a shared memory variable type. In this case, the function performs the operation on the shared memory register referenced by *dest*. The second scenario is when R is a resource variable type. In this scenario, the function performs the operation on the resource location referenced by *dest*. This operation is only available when R is readable and writable.

Interlocked operations do not imply any memory fence/barrier.

> [!Note]  
> If you call **InterlockedCompareExchange** in a [**for**](dx-graphics-hlsl-for.md) or [**while**](dx-graphics-hlsl-while.md) compute shader loop, to properly compile, you must use the **\[allow\_uav\_condition\]** attribute on that loop.

 

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

 

 




