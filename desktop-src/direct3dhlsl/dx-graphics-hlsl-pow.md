---
title: pow
description: Returns the specified value raised to the specified power.
ms.assetid: 1d64452c-81c7-4ef5-a332-13e0263c2cd1
keywords:
- pow HLSL
topic_type:
- apiref
api_name:
- pow
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# pow

Returns the specified value raised to the specified power.



| *ret* pow(*x*, *y*) |
|---------------------|



 

## Parameters



| Item                                                   | Description                            |
|--------------------------------------------------------|----------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The specified value.<br/> |
| <span id="y"></span><span id="Y"></span>*y*<br/> | \[in\] The specified power.<br/> |



 

## Return Value

The *x* parameter raised to the power of the *y* parameter.

## Remarks

The **pow** HLSL intrinsic function calculates *x*<sup>y</sup>.



| X      | Y      | Result                                                                      |
|--------|--------|-----------------------------------------------------------------------------|
| < 0 | any    | NAN                                                                         |
| > 0 | == 0   | 1                                                                           |
| == 0   | > 0 | 0                                                                           |
| == 0   | < 0 | inf                                                                         |
| > 0 | < 0 | 1/X<sup>-Y</sup>                                                            |
| == 0   | == 0   | Depends on the particular graphics processor<br/> 0, or 1, or NAN<br/> |



 

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *y*   | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |
| *ret* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |



 

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

 

