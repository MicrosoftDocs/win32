---
title: reflect
description: Returns a reflection vector using an incident ray and a surface normal.
ms.assetid: e321b399-f382-4585-83a6-a7da1f7b2327
keywords:
- reflect HLSL
topic_type:
- apiref
api_name:
- reflect
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# reflect

Returns a reflection vector using an incident ray and a surface normal.



| *ret* reflect(*i*, *n*) |
|-------------------------|



 

## Parameters



| Item                                                   | Description                                          |
|--------------------------------------------------------|------------------------------------------------------|
| <span id="i"></span><span id="I"></span>*i*<br/> | \[in\] A floating-point, incident vector.<br/> |
| <span id="n"></span><span id="N"></span>*n*<br/> | \[in\] A floating-point, normal vector.<br/>   |



 

## Return Value

A floating-point, reflection vector.

## Remarks

This function calculates the reflection vector using the following formula: v = i - 2 \* n \* dot(i n) .

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *i*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *n*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *i* |
| *ret* | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *i* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported |
|------------------------------------------------------------------------------------|-----------|
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) and higher shader models | yes       |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

