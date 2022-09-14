---
title: refract
description: Returns a refraction vector using an entering ray, a surface normal, and a refraction index.
ms.assetid: 9f9467d7-dd9b-472a-bbdc-752394d382c6
keywords:
- refract HLSL
topic_type:
- apiref
api_name:
- refract
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# refract

Returns a refraction vector using an entering ray, a surface normal, and a refraction index.



| *ret* refract(*i*, *n*, ?) |
|----------------------------|



 

## Parameters



| Item                                                   | Description                                                  |
|--------------------------------------------------------|--------------------------------------------------------------|
| <span id="i"></span><span id="I"></span>*i*<br/> | \[in\] A floating-point, ray direction vector.<br/>    |
| <span id="n"></span><span id="N"></span>*n*<br/> | \[in\] A floating-point, surface normal vector.<br/>   |
| *?*<br/>                                         | \[in\] A floating-point, refraction index scalar.<br/> |



 

## Return Value

A floating-point, refraction vector. If the angle between the entering ray i and the surface normal n is too great for a given refraction index ?, the return value is (0,0,0).

## Type Description



| Name              | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *i*               | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *n*               | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *i* |
| ?                 | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 1                              |
| refraction vector | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *i* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported           |
|------------------------------------------------------------------------------------|---------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes                 |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | yes (vs\_1\_1 only) |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

