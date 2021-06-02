---
title: ID3DX11EffectTechnique interface (D3dx11effect.h)
description: An ID3DX11EffectTechnique interface is a collection of passes.The lifetime of an ID3DX11EffectTechnique object is equal to the lifetime of its parent ID3DX11Effect object.
ms.assetid: 63d52cac-287d-4432-bf2b-7b4e67e525e6
keywords:
- ID3DX11EffectTechnique interface Direct3D 11
- ID3DX11EffectTechnique interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectTechnique
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectTechnique interface

An **ID3DX11EffectTechnique** interface is a collection of passes.

The lifetime of an **ID3DX11EffectTechnique** object is equal to the lifetime of its parent [**ID3DX11Effect**](id3dx11effect.md) object.

-   [Methods](#methods)

### Methods

The **ID3DX11EffectTechnique** interface has these methods.



| Method                                                                        | Description                                                           |
|:------------------------------------------------------------------------------|:----------------------------------------------------------------------|
| [**ComputeStateBlockMask**](id3dx11effecttechnique-computestateblockmask.md) | Compute a state-block mask to allow/prevent state changes.<br/> |
| [**GetAnnotationByIndex**](id3dx11effecttechnique-getannotationbyindex.md)   | Get an annotation by index.<br/>                                |
| [**GetAnnotationByName**](id3dx11effecttechnique-getannotationbyname.md)     | Get an annotation by name.<br/>                                 |
| [**GetDesc**](id3dx11effecttechnique-getdesc.md)                             | Get a technique description.<br/>                               |
| [**GetPassByIndex**](id3dx11effecttechnique-getpassbyindex.md)               | Get a pass by index.<br/>                                       |
| [**GetPassByName**](id3dx11effecttechnique-getpassbyname.md)                 | Get a pass by name.<br/>                                        |
| [**IsValid**](id3dx11effecttechnique-isvalid.md)                             | Test a technique to see if it contains valid syntax.<br/>       |



 

## Remarks

An effect contains one or more techniques; each technique contains one or more passes; each pass contains state assignments.

To get an effect-technique interface, call a method such as [**ID3DX11Effect::GetTechniqueByName**](id3dx11effect-gettechniquebyname.md).

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

 

 





