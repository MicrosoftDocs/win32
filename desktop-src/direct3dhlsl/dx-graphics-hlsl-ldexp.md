---
title: ldexp (Corecrt\_math.h)
description: Returns the result of multiplying the specified value by two, raised to the power of the specified exponent.
ms.assetid: 6d6fee96-f952-4058-a1ac-3abb98dbd540
keywords:
- ldexp HLSL
topic_type:
- apiref
api_name:
- ldexp
api_location:
- corecrt_math.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ldexp

Returns the result of multiplying the specified value by two, raised to the power of the specified exponent.



| *ret* ldexp(*x*, *exp*) |
|-------------------------|



 

This function uses the following formula: *x* \* 2<sup>exp</sup>

## Parameters



| Item                                                         | Description                               |
|--------------------------------------------------------------|-------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/>       | \[in\] The specified value.<br/>    |
| <span id="exp"></span><span id="EXP"></span>*exp*<br/> | \[in\] The specified exponent.<br/> |



 

## Return Value

The result of multiplying the *x* parameter by two, raised to the power of the *exp* parameter.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *exp* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |
| *ret* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported           |
|------------------------------------------------------------------------------------|---------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes                 |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | yes (vs\_1\_1 only) |



 

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Corecrt\_math.h</dt> </dl> |



## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

