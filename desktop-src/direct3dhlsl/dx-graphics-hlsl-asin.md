---
title: asin
description: Returns the arcsine of the specified value.
ms.assetid: 49559cb2-3305-4c97-8071-1589bcca3a75
keywords:
- asin HLSL
topic_type:
- apiref
api_name:
- asin
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# asin

Returns the arcsine of the specified value.



| *ret* asin(*x*) |
|-----------------|



 

## Parameters



| Item                                                   | Description                            |
|--------------------------------------------------------|----------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The specified value.<br/> |



 

## Return Value

The arcsine of the *x* parameter.

## Remarks

Each component of the *x* parameter should be within the range of -?/2 to ?/2.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types), **vector**, or **matrix** | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | any                            |
| *ret* | same as input *x*                                                                                              | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | same dimension(s) as input *x* |



 

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

 

 





