---
description: A conditional selection function that chooses between two values based on a condition.
nms.assetid:
title: select
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- select
api_type:
- NA
---


# select

A conditional selection function that chooses between two values based on a condition.

## Syntax


```syntax
any_sampler select(bool cond, any_sampler t, any_sampler f);
```

## Parameters

| Item | Description |
|------|-------------|
| *cond* | [in] The condition for the selection. If component of 'cond' is zero, then the corresponding component of 'f' is selected. Else, the corresponding component of 't' is selected.  || *t* | [in] The value to return if the condition is true (non-zero).  || *f* | [in] The value to return if the condition is false (zero).  |
## Return value

 Returns a template type which can be scalar, vector, or matrix and component type of float, int, or uint. The returned value corresponds to either 't' or 'f' depending on the 'cond' value.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types), [**int**](../WinProg/windows-data-types), or [**uint**](../WinProg/windows-data-types) | 1 |
| *cond*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | **bool** | 1 |
| *t*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types), [**int**](../WinProg/windows-data-types), or [**uint**](../WinProg/windows-data-types) | 1 |
| *f*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types), [**int**](../WinProg/windows-data-types), or [**uint**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|

## Shader Stages


## Remarks

In HLSL 2021 `int3 Z = select(X, 1, 0);` is a replacement for
```hlsl
int3 X = {1, 1, 1};
int3 Z = X ? 1 : 0;
```
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- ** See [HLSL 2021 Logical operation short-circuiting for scalars](https://github.com/microsoft/DirectXShaderCompiler/wiki/HLSL-2021#logical-operation-short-circuiting-for-scalars)**