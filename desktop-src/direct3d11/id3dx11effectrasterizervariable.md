---
title: ID3DX11EffectRasterizerVariable interface (D3dx11effect.h)
description: A rasterizer-variable interface accesses rasterizer state.
ms.assetid: d039e3c5-c066-4658-bead-92a5d705ed89
keywords:
- ID3DX11EffectRasterizerVariable interface Direct3D 11
- ID3DX11EffectRasterizerVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectRasterizerVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectRasterizerVariable interface

A rasterizer-variable interface accesses rasterizer state.

## Members

The **ID3DX11EffectRasterizerVariable** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectRasterizerVariable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectRasterizerVariable** interface has these methods.



| Method                                                                                   | Description                                                            |
|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**GetBackingStore**](id3dx11effectrasterizervariable-getbackingstore.md)               | Get a pointer to a variable that contains rasteriser state.<br/> |
| [**GetRasterizerState**](id3dx11effectrasterizervariable-getrasterizerstate.md)         | Get a pointer to a rasterizer interface.<br/>                    |
| [**SetRasterizerState**](id3dx11effectrasterizervariable-setrasterizerstate.md)         | Sets the rasterizer state.<br/>                                  |
| [**UndoSetRasterizerState**](id3dx11effectrasterizervariable-undosetrasterizerstate.md) | Reverts a previously set rasterizer state.<br/>                  |



 

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

 

 





