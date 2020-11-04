---
title: noise
description: Generates a random value using the Perlin-noise algorithm.
ms.assetid: 0188a7f3-9955-4e1c-9370-ef1d8aff3765
keywords:
- noise HLSL
topic_type:
- apiref
api_name:
- noise
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# noise

Generates a random value using the Perlin-noise algorithm.




| *ret* noise(*x*) |
|------------------|



 

## Parameters



| Item                                                   | Description                                                                    |
|--------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] A floating-point vector from which to generate Perlin noise.<br/> |



 

## Return Value

The Perlin noise value within a range between -1 and 1.

## Remarks

Perlin noise values change smoothly from one point to another over a space, creating natural looking, randomly generated values. You can use Perlin noise to generate procedural textures for effects like smoke and fire.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size |
|-------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|------|
| *x*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any  |
| *ret* | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 1    |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported           |
|------------------------------------------------------------------------------------|---------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | no                  |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | yes (tx\_1\_0 only) |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

