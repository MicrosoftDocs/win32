---
title: sign
description: Returns the sign of x.
ms.assetid: 3e2e04e8-0ffc-4721-a5d8-1ccfa6ca2a1a
keywords:
- sign HLSL
topic_type:
- apiref
api_name:
- sign
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# sign

Returns the sign of *x*.



| *ret* sign(*x*) |
|-----------------|



 

## Parameters



| Item                                                   | Description                        |
|--------------------------------------------------------|------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The input value.<br/> |



 

## Return Value

Returns -1 if *x* is less than zero; 0 if *x* equals zero; and 1 if *x* is greater than zero.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md)                 | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751), [**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751) | any                            |
| *ret* | same as input *x*                                                                                              | [**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                                          | same dimension(s) as input *x* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported                   |
|------------------------------------------------------------------------------------|-----------------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes                         |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | yes (vs\_1\_1 and ps\_1\_4) |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





