---
description: Unsigned add of 32-bit operand with the carry.
nms.assetid:
title: AddUint64
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- AddUint64
api_type:
- NA
---


# AddUint64

Unsigned add of 32-bit operand with the carry.

## Syntax


```syntax
uint<c> AddUint64(uint<c> a, uint<c> b);
```

## Parameters

| Item | Description |
|------|-------------|
| *a* | [in] A vector of type uint64_t (64-bit unsigned integer) as the first operand.  || *b* | [in] A second vector of type uint64_t (64-bit unsigned integer) as the second operand.  |
## Return value

 Returns a vector resulting from the addition of the two input vectors. Each component in the resulting vector is the sum of the corresponding components of the input vectors. All operations are performed on uint64_t types.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**uint**](../WinProg/windows-data-types) | any |
| *a*   | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**uint**](../WinProg/windows-data-types) | any |
| *b*   | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**uint**](../WinProg/windows-data-types) | any |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6](../direct3dhlsl/shader-model-6-0.md) and higher shader models | yes |

## Shader Stages


## Remarks

AddUint64 allows performing addition operations on 64-bit unsigned integers in shaders for complex arithmetic tasks.
`AddUint64` is useful for high-precision computations where 64-bit integers are required.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)