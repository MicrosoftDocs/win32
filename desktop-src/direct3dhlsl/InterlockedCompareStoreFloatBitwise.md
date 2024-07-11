---
description: Atomic compare and store for floats.
nms.assetid:
title: InterlockedCompareStoreFloatBitwise
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- InterlockedCompareStoreFloatBitwise
api_type:
- NA
---


# InterlockedCompareStoreFloatBitwise

Atomic compare and store for floats.


## Syntax


```syntax
void InterlockedCompareStoreFloatBitwise(uint byteOffest, float compare, float value);
```


## Parameters

| Item | Description |
|------|-------------|
| *byteOffset* | [in] A parameter representing the byte offset at which the comparison and replacement should start.  |
| *compare* | [in] The value to compare with the current memory location's value. If the values are equal, the operation will proceed.  |
| *value* | [in] The value to place in the memory location if the comparison passes.  |

## Return value

 This function does not return a value.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | **void** | **void** | 0 |
| *byteOffest* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *compare* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types) | 1 |
| *value* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.3](https://github.com/microsoft/DirectXShaderCompiler/wiki/Shader-Model-6.3) and higher shader models | yes |

## Shader Stages


## Remarks

The floating-point overrides of these functions  use the same operations by the existing integer functions. Therefore, these overrides are supported on SM 6.0 even without capability bits.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- ** See [InterlockedCompareStoreFloatBitwise](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_6_Int64_and_Float_Atomics.html#interlockedcomparestorefloatbitwise)**