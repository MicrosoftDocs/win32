---
title: clamp
description: Clamps the specified value to the specified minimum and maximum range.
ms.assetid: bcfafcec-3f9c-4b65-950c-da34184d5cdb
keywords:
- clamp HLSL
topic_type:
- apiref
api_name:
- clamp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# clamp

Clamps the specified value to the specified minimum and maximum range.



| *ret* clamp(*x*, *min*, *max*) |
|--------------------------------|



 

## Parameters



| Item                                                         | Description                                    |
|--------------------------------------------------------------|------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/>       | \[in\] A value to clamp.<br/>            |
| <span id="min"></span><span id="MIN"></span>*min*<br/> | \[in\] The specified minimum range.<br/> |
| <span id="max"></span><span id="MAX"></span>*max*<br/> | \[in\] The specified maximum range.<br/> |



 

## Return Value

The clamped value for the *x* parameter.

## Remarks

For values of -INF or INF, clamp will behave as expected. However for values of NaN, the results are undefined.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md)                 | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types) | any                            |
| *min* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types) | same dimension(s) as input *x* |
| *max* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types) | same dimension(s) as input *x* |
| *ret* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types) | same dimension(s) as input *x* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported             |
|------------------------------------------------------------------------------------|-----------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes                   |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | vs\_1\_1 and ps\_1\_4 |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

