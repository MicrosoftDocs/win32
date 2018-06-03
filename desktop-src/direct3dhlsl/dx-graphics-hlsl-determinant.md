---
title: determinant
description: Returns the determinant of the specified floating-point, square matrix.
ms.assetid: 9062b6f1-8518-4ee4-8d57-5aa9e2176d05
keywords:
- determinant HLSL
topic_type:
- apiref
api_name:
- determinant
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# determinant

Returns the determinant of the specified floating-point, square matrix.



| *ret* determinant(*m*) |
|------------------------|



 

## Parameters



| Item                                                   | Description                            |
|--------------------------------------------------------|----------------------------------------|
| <span id="m"></span><span id="M"></span>*m*<br/> | \[in\] The specified value.<br/> |



 

## Return Value

The floating-point, scalar value that represents the determinant of the *m* parameter.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                                     |
|-------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|------------------------------------------|
| *m*   | [**matrix**](https://www.bing.com/search?q=**matrix**) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | any (number of rows = number of columns) |
| *ret* | [**scalar**](https://www.bing.com/search?q=**scalar**) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 1                                        |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported             |
|------------------------------------------------------------------------------------|-----------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes                   |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | vs\_1\_1 and ps\_1\_4 |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





