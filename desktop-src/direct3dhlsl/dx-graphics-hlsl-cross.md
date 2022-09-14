---
title: cross
description: Returns the cross product of two floating-point, 3D vectors.
ms.assetid: 5f1832af-6bc5-49a7-956a-fd762f674f5f
keywords:
- cross HLSL
topic_type:
- apiref
api_name:
- cross
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# cross

Returns the cross product of two floating-point, 3D vectors.



| *ret* cross(*x*, *y*) |
|-----------------------|



 

## Parameters



| Item                                                   | Description                                             |
|--------------------------------------------------------|---------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The first floating-point, 3D vector.<br/>  |
| <span id="y"></span><span id="Y"></span>*y*<br/> | \[in\] The second floating-point, 3D vector.<br/> |



 

## Return Value

The cross product of the *x* parameter and the *y* parameter.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size |
|-------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|------|
| *x*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 3    |
| *y*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 3    |
| *ret* | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 3    |



 

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

 

