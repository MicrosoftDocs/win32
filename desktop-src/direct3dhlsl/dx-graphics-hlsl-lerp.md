---
title: lerp
description: Performs a linear interpolation.
ms.assetid: e369f182-b5bd-4b7f-aa77-9cfe11033bc4
keywords:
- lerp HLSL
topic_type:
- apiref
api_name:
- lerp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# lerp

Performs a linear interpolation.



| *ret* lerp(*x*, *y*, *s*) |
|---------------------------|



 

## Parameters



| Item                                                   | Description                                                                                           |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The first-floating point value.<br/>                                                     |
| <span id="y"></span><span id="Y"></span>*y*<br/> | \[in\] The second-floating point value.<br/>                                                    |
| <span id="s"></span><span id="S"></span>*s*<br/> | \[in\] A value that linearly interpolates between the *x* parameter and the *y* parameter.<br/> |



 

## Return Value

The result of the linear interpolation.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *y*   | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |
| *s*   | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |
| *ret* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |



 

## Remarks

Linear interpolation is based on the following formula: x\*(1-s) + y\*s which can equivalently be written as x + s(y-x).

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported                   |
|------------------------------------------------------------------------------------|-----------------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes                         |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | yes (vs\_1\_1 and ps\_1\_1) |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

