---
title: ID3DX11EffectConstantBuffer interface (D3dx11effect.h)
description: A constant-buffer interface accesses constant buffers or texture buffers.
ms.assetid: 2106cb51-dc0a-4ab6-adb6-2deb06922af1
keywords:
- ID3DX11EffectConstantBuffer interface Direct3D 11
- ID3DX11EffectConstantBuffer interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectConstantBuffer
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectConstantBuffer interface

A constant-buffer interface accesses constant buffers or texture buffers.

## Members

The **ID3DX11EffectConstantBuffer** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectConstantBuffer** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectConstantBuffer** interface has these methods.



| Method                                                                             | Description                                          |
|:-----------------------------------------------------------------------------------|:-----------------------------------------------------|
| [**GetConstantBuffer**](id3dx11effectconstantbuffer-getconstantbuffer.md)         | Get a constant-buffer.<br/>                    |
| [**GetTextureBuffer**](id3dx11effectconstantbuffer-gettexturebuffer.md)           | Get a texture-buffer.<br/>                     |
| [**SetConstantBuffer**](id3dx11effectconstantbuffer-setconstantbuffer.md)         | Set a constant-buffer.<br/>                    |
| [**SetTextureBuffer**](id3dx11effectconstantbuffer-settexturebuffer.md)           | Set a texture-buffer.<br/>                     |
| [**UndoSetConstantBuffer**](id3dx11effectconstantbuffer-undosetconstantbuffer.md) | Reverts a previously set constant buffer.<br/> |
| [**UndoSetTextureBuffer**](id3dx11effectconstantbuffer-undosettexturebuffer.md)   | Reverts a previously set texture buffer.<br/>  |



 

## Remarks

Use constant buffers to store many effect constants; grouping constants into buffers based on their frequency of update. This allows you to minimize the number of state changes as well as make the fewest API calls to change state. Both of these factors lead to better performance.

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

 

 





