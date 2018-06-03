---
title: frexp
description: Returns the mantissa and exponent of the specified floating-point value.
ms.assetid: 9252feff-da85-4b3e-97db-1fcddd786695
keywords:
- frexp HLSL
topic_type:
- apiref
api_name:
- frexp
api_location:
- corecrt_math.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# frexp

Returns the mantissa and exponent of the specified floating-point value.



| *ret* frexp(*x*, *exp*) |
|-------------------------|



 

The return value is the mantissa, and the value returned by *exp* parameter is the exponent.

## Parameters



| Item                                                         | Description                                                                                                                                      |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/>       | \[in\] The specified floating-point value. If the *x* parameter is 0, this function returns 0 for both the mantissa and the exponent.<br/> |
| <span id="exp"></span><span id="EXP"></span>*exp*<br/> | \[out\] The returned exponent of the *x* parameter.<br/>                                                                                   |



 

## Return Value

The mantissa of the *x* parameter.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](https://www.bing.com/search?q=**scalar**), **vector**, or **matrix** | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | any                            |
| *exp* | same as input *x*                                                                                              | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | same dimension(s) as input *x* |
| *ret* | same as input *x*                                                                                              | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | same dimension(s) as input *x* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported           |
|------------------------------------------------------------------------------------|---------------------|
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) and higher shader models | yes                 |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md)                          | yes (ps\_2\_x only) |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | no                  |



 

## Remarks

## Requirements



|                   |                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Corecrt\_math.h</dt> </dl> |



## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





