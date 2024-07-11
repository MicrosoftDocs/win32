---
description: Atomic compare and exchange for floats.
nms.assetid:
title: InterlockedCompareExchangeFloatBitwise
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- InterlockedCompareExchangeFloatBitwise
api_type:
- NA
---


# InterlockedCompareExchangeFloatBitwise

Atomic compare and exchange for floats.


## Syntax


```syntax
void InterlockedCompareExchangeFloatBitwise(uint byteOffest, float compare, float value, float original);
```


## Parameters

| Item | Description |
|------|-------------|
| *byteOffset* | [in] An integer representing the byte offset value.  |
| *compare* | [in] The comparison value for the function.  |
| *value* | [in] The replacement value if the compare and original values match.  |
| *original* | [in] The original value being compared with the compare value. If the original and compare values match, the original value is replaced by the value parameter.  |

## Return value

 This function does not return a value.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | **void** | **void** | 0 |
| *byteOffest* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *compare* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types) | 1 |
| *value* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types) | 1 |
| *original* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types) | 1 |

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
- ** See [InterlockedCompareStoreFloatBitwise](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_6_Int64_and_Float_Atomics.html#interlockedcompareexchange)**