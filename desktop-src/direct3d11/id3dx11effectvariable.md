---
title: ID3DX11EffectVariable interface (D3dx11effect.h)
description: The ID3DX11EffectVariable interface is the base class for all effect variables.The lifetime of an ID3DX11EffectVariable object is equal to the lifetime of its parent ID3DX11Effect object.
ms.assetid: 07f1b7d7-c266-49ae-b79a-7a645521df89
keywords:
- ID3DX11EffectVariable interface Direct3D 11
- ID3DX11EffectVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable interface

The **ID3DX11EffectVariable** interface is the base class for all effect variables.

The lifetime of an **ID3DX11EffectVariable** object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.

-   [Methods](#methods)

### Methods

The **ID3DX11EffectVariable** interface has these methods.



| Method                                                                           | Description                                            |
|:---------------------------------------------------------------------------------|:-------------------------------------------------------|
| [**AsBlend**](id3dx11effectvariable-asblend.md)                                 | Get a effect-blend variable.<br/>                |
| [**AsClassInstance**](id3dx11effectvariable-asclassinstance.md)                 | Get a class-instance variable.<br/>              |
| [**AsConstantBuffer**](id3dx11effectvariable-asconstantbuffer.md)               | Get a constant buffer.<br/>                      |
| [**AsDepthStencil**](id3dx11effectvariable-asdepthstencil.md)                   | Get a depth-stencil variable.<br/>               |
| [**AsDepthStencilView**](id3dx11effectvariable-asdepthstencilview.md)           | Get a depth-stencil-view variable.<br/>          |
| [**AsInterface**](id3dx11effectvariable-asinterface.md)                         | Get an interface variable.<br/>                  |
| [**AsMatrix**](id3dx11effectvariable-asmatrix.md)                               | Get a matrix variable.<br/>                      |
| [**AsRasterizer**](id3dx11effectvariable-asrasterizer.md)                       | Get a rasterizer variable.<br/>                  |
| [**AsRenderTargetView**](id3dx11effectvariable-asrendertargetview.md)           | Get a render-target-view variable.<br/>          |
| [**AsSampler**](id3dx11effectvariable-assampler.md)                             | Get a sampler variable.<br/>                     |
| [**AsScalar**](id3dx11effectvariable-asscalar.md)                               | Get a scalar variable.<br/>                      |
| [**AsShader**](id3dx11effectvariable-asshader.md)                               | Get a shader variable.<br/>                      |
| [**AsShaderResource**](id3dx11effectvariable-asshaderresource.md)               | Get a shader-resource variable.<br/>             |
| [**AsString**](id3dx11effectvariable-asstring.md)                               | Get a string variable.<br/>                      |
| [**AsUnorderedAccessView**](id3dx11effectvariable-asunorderedaccessview.md)     | Get an unordered-access-view variable.<br/>      |
| [**AsVector**](id3dx11effectvariable-asvector.md)                               | Get a vector variable.<br/>                      |
| [**GetAnnotationByIndex**](id3dx11effectvariable-getannotationbyindex.md)       | Get an annotation by index.<br/>                 |
| [**GetAnnotationByName**](id3dx11effectvariable-getannotationbyname.md)         | Get an annotation by name.<br/>                  |
| [**GetDesc**](id3dx11effectvariable-getdesc.md)                                 | Get a description.<br/>                          |
| [**GetElement**](id3dx11effectvariable-getelement.md)                           | Get an array element.<br/>                       |
| [**GetMemberByIndex**](id3dx11effectvariable-getmemberbyindex.md)               | Get a structure member by index.<br/>            |
| [**GetMemberByName**](id3dx11effectvariable-getmemberbyname.md)                 | Get a structure member by name.<br/>             |
| [**GetMemberBySemantic**](id3dx11effectvariable-getmemberbysemantic.md)         | Get a structure member by semantic.<br/>         |
| [**GetParentConstantBuffer**](id3dx11effectvariable-getparentconstantbuffer.md) | Get a constant buffer.<br/>                      |
| [**GetRawValue**](id3dx11effectvariable-getrawvalue.md)                         | Get data.<br/>                                   |
| [**GetType**](id3dx11effectvariable-gettype.md)                                 | Get type information.<br/>                       |
| [**IsValid**](id3dx11effectvariable-isvalid.md)                                 | Compare the data type with the data stored.<br/> |
| [**SetRawValue**](id3dx11effectvariable-setrawvalue.md)                         | Set data.<br/>                                   |



 

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

[Effects 11 Interfaces](d3d11-graphics-reference-effects11-interfaces.md)
</dt> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

 





