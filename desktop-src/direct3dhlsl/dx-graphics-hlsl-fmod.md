---
title: fmod (Corecrt\_math.h)
description: Returns the floating-point remainder of x/y.
ms.assetid: bb940548-c4c5-4109-a488-4ea7295c7213
keywords:
- fmod HLSL
topic_type:
- apiref
api_name:
- fmod
api_location:
- corecrt_math.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# fmod

Returns the floating-point remainder of x/y.



| *ret* fmod(*x*, *y*) |
|----------------------|



 

## Parameters



| Item                                                   | Description                                    |
|--------------------------------------------------------|------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The floating-point dividend.<br/> |
| <span id="y"></span><span id="Y"></span>*y*<br/> | \[in\] The floating-point divisor.<br/>  |



 

## Return Value

The floating-point remainder of the *x* parameter divided by the *y* parameter.

## Remarks

The floating-point remainder is calculated such that x = i \* y + f, where i is an integer, f has the same sign as x, and the absolute value of f is less than the absolute value of y.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *y*   | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |
| *ret* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported |
|------------------------------------------------------------------------------------|-----------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes       |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | vs\_1\_1  |



 

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Corecrt\_math.h</dt> </dl> |



## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

