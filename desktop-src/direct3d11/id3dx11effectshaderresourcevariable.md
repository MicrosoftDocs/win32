---
title: ID3DX11EffectShaderResourceVariable interface (D3dx11effect.h)
description: A shader-resource interface accesses a shader resource.
ms.assetid: 936a3439-1f7d-4fea-b124-1d6ead528250
keywords:
- ID3DX11EffectShaderResourceVariable interface Direct3D 11
- ID3DX11EffectShaderResourceVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectShaderResourceVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectShaderResourceVariable interface

A shader-resource interface accesses a shader resource.

## Members

The **ID3DX11EffectShaderResourceVariable** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectShaderResourceVariable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectShaderResourceVariable** interface has these methods.



| Method                                                                           | Description                                  |
|:---------------------------------------------------------------------------------|:---------------------------------------------|
| [**GetResource**](id3dx11effectshaderresourcevariable-getresource.md)           | Get a shader resource.<br/>            |
| [**GetResourceArray**](id3dx11effectshaderresourcevariable-getresourcearray.md) | Get an array of shader resources.<br/> |
| [**SetResource**](id3dx11effectshaderresourcevariable-setresource.md)           | Set a shader resource.<br/>            |
| [**SetResourceArray**](id3dx11effectshaderresourcevariable-setresourcearray.md) | Set an array of shader resources.<br/> |



 

## Remarks

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[**ID3DX11EffectVariable**](id3dx11effectvariable.md)
</dt> <dt>

[Effects 11 Interfaces](d3d11-graphics-reference-effects11-interfaces.md)
</dt> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

 





