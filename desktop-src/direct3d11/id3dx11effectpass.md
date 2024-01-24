---
title: ID3DX11EffectPass interface (D3dx11effect.h)
description: An ID3DX11EffectPass interface encapsulates state assignments within a technique.The lifetime of an ID3DX11EffectPass object is equal to the lifetime of its parent ID3DX11Effect object.
ms.assetid: 4d86c362-b0f8-4396-86de-c7c89710f46d
keywords:
- ID3DX11EffectPass interface Direct3D 11
- ID3DX11EffectPass interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectPass
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectPass interface

An **ID3DX11EffectPass** interface encapsulates state assignments within a technique.

The lifetime of an **ID3DX11EffectPass** object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.

-   [Methods](#methods)

### Methods

The **ID3DX11EffectPass** interface has these methods.



| Method                                                                   | Description                                                       |
|:-------------------------------------------------------------------------|:------------------------------------------------------------------|
| [**Apply**](id3dx11effectpass-apply.md)                                 | Set the state contained in a pass to the device.<br/>       |
| [**ComputeStateBlockMask**](id3dx11effectpass-computestateblockmask.md) | Generate a mask for allowing/preventing state changes.<br/> |
| [**GetAnnotationByIndex**](id3dx11effectpass-getannotationbyindex.md)   | Get an annotation by index.<br/>                            |
| [**GetAnnotationByName**](id3dx11effectpass-getannotationbyname.md)     | Get an annotation by name.<br/>                             |
| [**GetComputeShaderDesc**](id3dx11effectpass-getcomputeshaderdesc.md)   | Get a compute-shader description.<br/>                      |
| [**GetDesc**](id3dx11effectpass-getdesc.md)                             | Get a pass description.<br/>                                |
| [**GetDomainShaderDesc**](id3dx11effectpass-getdomainshaderdesc.md)     | Get a domain-shader description.<br/>                       |
| [**GetGeometryShaderDesc**](id3dx11effectpass-getgeometryshaderdesc.md) | Get a geometry-shader description.<br/>                     |
| [**GetHullShaderDesc**](id3dx11effectpass-gethullshaderdesc.md)         | Get hull-shader description.<br/>                           |
| [**GetPixelShaderDesc**](id3dx11effectpass-getpixelshaderdesc.md)       | Get a pixel-shader description.<br/>                        |
| [**GetVertexShaderDesc**](id3dx11effectpass-getvertexshaderdesc.md)     | Get a vertex-shader description.<br/>                       |
| [**IsValid**](id3dx11effectpass-isvalid.md)                             | Test a pass to see if it contains valid syntax.<br/>        |



 

## Remarks

A pass is a block of code that sets render-state objects and shaders. A pass is declared within a technique.

To get an effect-pass interface, call a method like [**ID3DX11EffectTechnique::GetPassByName**](id3dx11effecttechnique-getpassbyname.md).

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

 

 





