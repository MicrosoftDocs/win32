---
title: tex1D (HLSL reference)
description: Samples a 1D texture.
ms.assetid: 587be0fd-af12-4bf0-862b-84988435e90e
keywords:
- tex1D HLSL
topic_type:
- apiref
api_name:
- tex1D
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# tex1D (HLSL reference)

Samples a 1D texture.



| ret tex1D(s, t) |
|-----------------|



 

## Parameters



| Item                                                   | Description                               |
|--------------------------------------------------------|-------------------------------------------|
| <span id="s"></span><span id="S"></span>*s*<br/> | \[in\] The sampler state.<br/>      |
| <span id="t"></span><span id="T"></span>*t*<br/> | \[in\] The texture coordinate.<br/> |



 

## Return Value

The value of the texture data.

## Type Description



| Name | In/Out | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size |
|------|--------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|------|
| s    | in     | [**object**](dx-graphics-hlsl-intrinsic-functions.md) | [sampler1D](dx-graphics-hlsl-sampler.md)                      | 1    |
| t    | in     | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 1    |
| ret  | out    | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 4    |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported                                                                                                                         |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes (pixel shader only), but you must use the [legacy compile option](/windows/desktop/direct3dtools/dx-graphics-tools-fxc-syntax) when compiling. |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | yes (pixel shader only)                                                                                                           |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | yes (pixel shader only)                                                                                                           |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | yes (pixel shader only)                                                                                                           |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

