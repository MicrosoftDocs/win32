---
title: ID3DX11EffectShaderVariable interface (D3dx11effect.h)
description: A shader-variable interface accesses a shader variable.
ms.assetid: e547a5e9-7b60-4a85-806d-272be55d12e7
keywords:
- ID3DX11EffectShaderVariable interface Direct3D 11
- ID3DX11EffectShaderVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectShaderVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectShaderVariable interface

A shader-variable interface accesses a shader variable.

## Members

The **ID3DX11EffectShaderVariable** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectShaderVariable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectShaderVariable** interface has these methods.



| Method                                                                                                           | Description                                            |
|:-----------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------|
| [**GetComputeShader**](id3dx11effectshadervariable-getcomputeshader.md)                                         | Get a compute shader.<br/>                       |
| [**GetDomainShader**](id3dx11effectshadervariable-getdomainshader.md)                                           | Get a domain shader.<br/>                        |
| [**GetGeometryShader**](id3dx11effectshadervariable-getgeometryshader.md)                                       | Get a geometry shader.<br/>                      |
| [**GetHullShader**](id3dx11effectshadervariable-gethullshader.md)                                               | Get a hull shader.<br/>                          |
| [**GetInputSignatureElementDesc**](id3dx11effectshadervariable-getinputsignatureelementdesc.md)                 | Get an input-signature description.<br/>         |
| [**GetOutputSignatureElementDesc**](id3dx11effectshadervariable-getoutputsignatureelementdesc.md)               | Get an output-signature description.<br/>        |
| [**GetPatchConstantSignatureElementDesc**](id3dx11effectshadervariable-getpatchconstantsignatureelementdesc.md) | Get a patch constant signature description.<br/> |
| [**GetPixelShader**](id3dx11effectshadervariable-getpixelshader.md)                                             | Get a pixel shader.<br/>                         |
| [**GetShaderDesc**](id3dx11effectshadervariable-getshaderdesc.md)                                               | Get a shader description.<br/>                   |
| [**GetVertexShader**](id3dx11effectshadervariable-getvertexshader.md)                                           | Get a vertex shader.<br/>                        |



 

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

 

 





