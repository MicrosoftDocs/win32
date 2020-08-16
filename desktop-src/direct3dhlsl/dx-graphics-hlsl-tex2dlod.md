---
title: tex2Dlod
description: Samples a 2D texture with mipmaps. The mipmap LOD is specified in t.w.
ms.assetid: 689eff39-f6ac-4c25-8b92-ca68707ae8ad
keywords:
- tex2Dlod HLSL
topic_type:
- apiref
api_name:
- tex2Dlod
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# tex2Dlod

Samples a 2D texture with mipmaps. The mipmap LOD is specified in t.w.



| ret tex2Dlod(s, t) |
|--------------------|



 

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
| s    | in     | [**object**](dx-graphics-hlsl-intrinsic-functions.md) | [sampler2D](dx-graphics-hlsl-sampler.md)                      | 1    |
| t    | in     | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 4    |
| ret  | out    | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 4    |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported |
|------------------------------------------------------------------------------------|-----------|
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) and higher shader models | yes       |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md)                          | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | no        |



 

## Remarks

Starting with Direct3D 10, you can use new HLSL syntax to access textures and other resources. You can replace intrinsic-style texture lookup functions, such as **tex2Dlod**, with a more object-oriented style. In this object-oriented style, textures are decoupled from samplers and have methods for loading and sampling.

To sample a 2D texture, instead of using **tex2Dlod** as in this code:


```
sampler S;
...
color = tex2Dlod(S, Location);
```



Use the [SampleLevel](dx-graphics-hlsl-to-samplelevel.md) method of a [**Texture Object**](dx-graphics-hlsl-to-type.md) as in this code:


```
Texture2D MyTexture;
SamplerState MySampler;
...
color = MyTexture.SampleLevel(MySampler, Location, LOD);
```



To use the intrinsic-style texture lookup functions, such as **tex2Dlod**, with [shader model 4](dx-graphics-hlsl-sm4.md) and higher, use [**D3DCOMPILE\_ENABLE\_BACKWARDS\_COMPATIBILITY**](d3dcompile-constants.md) to compile. However, if you want to target shader model 4 and higher (even [\*\_4\_0\_level\_9\_\*](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro)) with newer object-oriented style code, migrate to the newer HLSL syntax.

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

