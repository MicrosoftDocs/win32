---
title: ID3DX11EffectBlendVariable interface (D3dx11effect.h)
description: The blend-variable interface accesses blend state.
ms.assetid: 8a6e6e7e-2f1e-4e16-8d28-ffc7f3f018d6
keywords:
- ID3DX11EffectBlendVariable interface Direct3D 11
- ID3DX11EffectBlendVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectBlendVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectBlendVariable interface

The blend-variable interface accesses blend state.

## Members

The **ID3DX11EffectBlendVariable** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectBlendVariable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectBlendVariable** interface has these methods.



| Method                                                                    | Description                                          |
|:--------------------------------------------------------------------------|:-----------------------------------------------------|
| [**GetBackingStore**](id3dx11effectblendvariable-getbackingstore.md)     | Get a pointer to a blend-state variable.<br/>  |
| [**GetBlendState**](id3dx11effectblendvariable-getblendstate.md)         | Get a pointer to a blend-state interface.<br/> |
| [**SetBlendState**](id3dx11effectblendvariable-setblendstate.md)         | Sets an effect's blend-state.<br/>             |
| [**UndoSetBlendState**](id3dx11effectblendvariable-undosetblendstate.md) | Reverts a previously set blend-state.<br/>     |



 

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

 

 





