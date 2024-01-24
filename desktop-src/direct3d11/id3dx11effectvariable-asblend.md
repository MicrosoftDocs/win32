---
title: ID3DX11EffectVariable AsBlend method (D3dx11effect.h)
description: Get a effect-blend variable.
ms.assetid: e9670d13-e006-408b-9cdf-352bcfa66a52
keywords:
- AsBlend method Direct3D 11
- AsBlend method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , AsBlend method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.AsBlend
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::AsBlend method

Get a effect-blend variable.

## Syntax


```C++
ID3DX11EffectBlendVariable* AsBlend();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**ID3DX11EffectBlendVariable**](id3dx11effectblendvariable.md)\***

A pointer to an effect blend variable. See [**ID3DX11EffectBlendVariable**](id3dx11effectblendvariable.md).

## Remarks

AsBlend returns a version of the effect variable that has been specialized to an effect-blend variable. Similar to a cast, this specialization will return an invalid object if the effect variable does not contain effect-blend data.

Applications can test the returned object for validity by calling [**IsValid**](id3dx11effectvariable-isvalid.md).

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectVariable](id3dx11effectvariable.md)
</dt> </dl>

 

 





