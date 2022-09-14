---
title: normalize
description: Normalizes the specified floating-point vector according to x / length(x).
ms.assetid: 7fd6f8ff-f3ff-4d14-b3fc-b44fdddf6c75
keywords:
- normalize HLSL
topic_type:
- apiref
api_name:
- normalize
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# normalize

Normalizes the specified floating-point vector according to x / length(x).



| *ret* normalize(*x*) |
|----------------------|



 

## Parameters



| Item                                                   | Description                                            |
|--------------------------------------------------------|--------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The specified floating-point vector.<br/> |



 

## Return Value

The normalized *x* parameter. If the length of the *x* parameter is 0, the result is indefinite.

## Remarks

The **normalize** HLSL intrinsic function uses the following formula: *x* / [**length**](dx-graphics-hlsl-length.md)(*x*).

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *ret* | same as input *x*                                                                   | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported           |
|------------------------------------------------------------------------------------|---------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes                 |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | yes (vs\_1\_1 only) |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

