---
title: frac
description: Returns the fractional (or decimal) part of x; which is greater than or equal to 0 and less than 1.
ms.assetid: 4e85390f-2b1a-402b-b932-09b80097f7e6
keywords:
- frac HLSL
topic_type:
- apiref
api_name:
- frac
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# frac

Returns the fractional (or decimal) part of x; which is greater than or equal to 0 and less than 1.

Also see [trunc](./dx-graphics-hlsl-trunc.md).

| *ret* frac(*x*) |
|-----------------|



 

## Parameters



| Item                                                   | Description                            |
|--------------------------------------------------------|----------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The specified value.<br/> |



 

## Return Value

The fractional part of the *x* parameter.

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



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

