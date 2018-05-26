---
title: min
description: Selects the lesser of x and y.
ms.assetid: 4e10cfc2-d680-4d7f-81b2-fa52024f902d
keywords:
- min HLSL
topic_type:
- apiref
api_name:
- min
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# min

Selects the lesser of x and y.



| ret min(x, y) |
|---------------|



 

## Parameters



| Item                                                   | Description                          |
|--------------------------------------------------------|--------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The x input value.<br/> |
| <span id="y"></span><span id="Y"></span>*y*<br/> | \[in\] The y input value.<br/> |



 

## Return Value

The *x* or *y* parameter, whichever is the smallest value.

## Remarks

For values of -INF or INF, min will behave as expected. However for values of NaN, the results are undefined.

## Type Description



| Name | In/Out      | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md)                 | Size                         |
|------|-------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------|
| x    | in          | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types), **vector**, or **matrix** | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751), [**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751) | any                          |
| y    | in          | same as input x                                                                                                | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751), [**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751) | same dimension(s) as input x |
| ret  | return type | same as input x                                                                                                | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751), [**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751) | same dimension(s) as input x |



 

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

 

 





