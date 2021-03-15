---
title: modf (Corecrt\_math.h)
description: Splits the value x into fractional and integer parts, each of which has the same sign as x.
ms.assetid: 0cac1cf3-f0da-4b0a-ba30-4af5d65b04b2
keywords:
- modf HLSL
topic_type:
- apiref
api_name:
- modf
api_location:
- corecrt_math.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# modf

Splits the value x into fractional and integer parts, each of which has the same sign as x.



| ret modf(x, out ip) |
|---------------------|



 

## Parameters



| Item                                                      | Description                                    |
|-----------------------------------------------------------|------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/>    | \[in\] The x input value.<br/>           |
| <span id="ip"></span><span id="IP"></span>*ip*<br/> | \[out\] The integer portion of *x*.<br/> |



 

## Return Value

The signed-fractional portion of x.

## Type Description



| Name | In/Out | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md)                 | Size                         |
|------|--------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------|
| x    | in     | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types) | any                          |
| ip   | out    | same as input x                                                                                                | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types) | same dimension(s) as input x |
| ret  | out    | same as input x                                                                                                | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types) | same dimension(s) as input x |



 

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

 

