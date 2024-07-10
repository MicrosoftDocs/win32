---
description: Signed dot product of 4 x i8 vectors packed into i32, with accumulate to i32.
nms.assetid:
title: dot4add_i8packed
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- dot4add_i8packed
api_type:
- NA
---


# dot4add_i8packed

Signed dot product of 4 x i8 vectors packed into i32, with accumulate to i32.

## Syntax


```syntax
int dot4add_i8packed(uint a, uint b, int c);
```

## Parameters

| Item | Description |
|------|-------------|
| *a* | [in] First input parameter of type 'i8packed'. It is the first vector in the dot product operation.  || *b* | [in] Second input parameter of type 'i8packed'. It is the second vector in the dot product operation.  || *c* | [in] Third parameter of type int. This value gets added to the result of the dot product operation.  |
## Return value

 This function returns a template of type 'scalar' with component type 'int'. It represents the result of the dot product operation between the two input parameters with the third parameter added to it.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**int**](../WinProg/windows-data-types) | 1 |
| *a*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *b*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *c*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**int**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.4](../direct3dhlsl/hlsl-shader-model-6-4-features-for-direct3d-12.md) and higher shader models | yes |

## Shader Stages


## Remarks

dot4add_i8packed computes a dot product with four 8-bit packed signed integer vectors, useful for SIMD optimizations.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [Signed Integer Dot-Product of 4 Elements and Accumulate](../direct3dhlsl/hlsl-shader-model-6-4-features-for-direct3d-12.md#signed-integer-dot-product-of-4-elements-and-accumulate)**