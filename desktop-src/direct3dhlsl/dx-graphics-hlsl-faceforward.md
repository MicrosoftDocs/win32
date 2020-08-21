---
title: faceforward
description: Flips the surface-normal (if needed) to face in a direction opposite to i; returns the result in n.
ms.assetid: 6530a928-d221-49e4-ab68-6285c3db370f
keywords:
- faceforward HLSL
topic_type:
- apiref
api_name:
- faceforward
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# faceforward

Flips the surface-normal (if needed) to face in a direction opposite to i; returns the result in n.



| *ret* faceforward(*n*, *i*, *ng*) |
|-----------------------------------|



 

This function uses the following formula: -*n*  sign(dot(*i*, *ng*)).

## Parameters



| Item                                                      | Description                                                                                                     |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <span id="n"></span><span id="N"></span>*n*<br/>    | \[in\] The resulting floating-point surface-normal vector.<br/>                                           |
| <span id="i"></span><span id="I"></span>*i*<br/>    | \[in\] A floating-point, incident vector that points from the view position to the shading position.<br/> |
| <span id="ng"></span><span id="NG"></span>*ng*<br/> | \[in\] A floating-point surface-normal vector.<br/>                                                       |



 

## Return Value

A floating-point, surface normal vector that is facing the view direction.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *n*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *i*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *n* |
| *ng*  | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimensions as input *n*   |
| *ret* | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimensions as input *n*   |



 

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

 

