---
title: ID3DX11EffectVariable AsShaderResource method (D3dx11effect.h)
description: Get a shader-resource variable.
ms.assetid: 02db94eb-980a-4677-af89-3006aef6faca
keywords:
- AsShaderResource method Direct3D 11
- AsShaderResource method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , AsShaderResource method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.AsShaderResource
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::AsShaderResource method

Get a shader-resource variable.

## Syntax


```C++
ID3DX11EffectShaderResourceVariable* AsShaderResource();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**ID3DX11EffectShaderResourceVariable**](id3dx11effectshaderresourcevariable.md)\***

A pointer to a shader-resource variable. See [**ID3DX11EffectShaderResourceVariable**](id3dx11effectshaderresourcevariable.md).

## Remarks

AsShaderResource returns a version of the effect variable that has been specialized to a shader-resource variable. Similar to a cast, this specialization will return an invalid object if the effect variable does not contain shader-resource data.

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

 

 





