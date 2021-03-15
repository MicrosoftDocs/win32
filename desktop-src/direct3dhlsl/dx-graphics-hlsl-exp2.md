---
title: exp2 (Corecrt\_math.h)
description: Returns the base 2 exponential, or 2x, of the specified value.
ms.assetid: 68b0057c-864d-440b-84f6-781d5fa3b019
keywords:
- exp2 HLSL
topic_type:
- apiref
api_name:
- exp2
api_location:
- corecrt_math.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# exp2

Returns the base 2 exponential, or 2<sup>x</sup>, of the specified value.



| *ret* exp2(*x*) |
|-----------------|



 

## Parameters



| Item                                                   | Description                                           |
|--------------------------------------------------------|-------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The specified floating-point value.<br/> |



 

## Return Value

The base 2 exponential of the *x* parameter.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
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

 

