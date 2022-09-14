---
title: ID3DX11EffectSamplerVariable interface (D3dx11effect.h)
description: A sampler interface accesses sampler state.
ms.assetid: 8d21f829-2145-45f2-a9b4-2fdc06e0a879
keywords:
- ID3DX11EffectSamplerVariable interface Direct3D 11
- ID3DX11EffectSamplerVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectSamplerVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectSamplerVariable interface

A sampler interface accesses sampler state.

## Members

The **ID3DX11EffectSamplerVariable** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectSamplerVariable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectSamplerVariable** interface has these methods.



| Method                                                                  | Description                                                         |
|:------------------------------------------------------------------------|:--------------------------------------------------------------------|
| [**GetBackingStore**](id3dx11effectsamplervariable-getbackingstore.md) | Get a pointer to a variable that contains sampler state.<br/> |
| [**GetSampler**](id3dx11effectsamplervariable-getsampler.md)           | Get a pointer to a sampler interface.<br/>                    |
| [**SetSampler**](id3dx11effectsamplervariable-setsampler.md)           | Set sampler state.<br/>                                       |
| [**UndoSetSampler**](id3dx11effectsamplervariable-undosetsampler.md)   | Revert a previously set sampler state.<br/>                   |



 

## Remarks

An [**ID3DX11EffectVariable**](id3dx11effectvariable.md) interface is created when an effect is read into memory.

Effect variables are saved in memory in the backing store; when a technique is applied, the values in the backing store are copied to the device. You can use either of these methods to return state.

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

 

 





