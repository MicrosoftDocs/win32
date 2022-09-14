---
title: ID3DX11EffectVariable AsDepthStencil method (D3dx11effect.h)
description: Get a depth-stencil variable.
ms.assetid: 3526812b-6c43-492e-b529-12f61ecd20e3
keywords:
- AsDepthStencil method Direct3D 11
- AsDepthStencil method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , AsDepthStencil method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.AsDepthStencil
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::AsDepthStencil method

Get a depth-stencil variable.

## Syntax


```C++
ID3DX11EffectDepthStencilVariable* AsDepthStencil();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**ID3DX11EffectDepthStencilVariable**](id3dx11effectdepthstencilvariable.md)\***

A pointer to a depth-stencil variable. See [**ID3DX11EffectDepthStencilVariable**](id3dx11effectdepthstencilvariable.md).

## Remarks

AsDepthStencil returns a version of the effect variable that has been specialized to a depth-stencil variable. Similar to a cast, this specialization will return an invalid object if the effect variable does not contain depth-stencil data.

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

 

 





