---
title: ID3DX11EffectDepthStencilViewVariable interface (D3dx11effect.h)
description: A depth-stencil-view-variable interface accesses a depth-stencil view.
ms.assetid: 316bf0cc-a7cd-4a40-932a-d566e3c2001e
keywords:
- ID3DX11EffectDepthStencilViewVariable interface Direct3D 11
- ID3DX11EffectDepthStencilViewVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectDepthStencilViewVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectDepthStencilViewVariable interface

A depth-stencil-view-variable interface accesses a depth-stencil view.

## Members

The **ID3DX11EffectDepthStencilViewVariable** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectDepthStencilViewVariable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectDepthStencilViewVariable** interface has these methods.



| Method                                                                                     | Description                                              |
|:-------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| [**GetDepthStencil**](id3dx11effectdepthstencilviewvariable-getdepthstencil.md)           | Get a depth-stencil-view resource.<br/>            |
| [**GetDepthStencilArray**](id3dx11effectdepthstencilviewvariable-getdepthstencilarray.md) | Get an array of depth-stencil-view resources.<br/> |
| [**SetDepthStencil**](id3dx11effectdepthstencilviewvariable-setdepthstencil.md)           | Set a depth-stencil-view resource.<br/>            |
| [**SetDepthStencilArray**](id3dx11effectdepthstencilviewvariable-setdepthstencilarray.md) | Set an array of depth-stencil-view resources.<br/> |



 

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

 

 





