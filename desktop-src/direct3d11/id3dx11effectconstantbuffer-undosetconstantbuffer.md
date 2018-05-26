---
title: ID3DX11EffectConstantBuffer UndoSetConstantBuffer method
description: Reverts a previously set constant buffer.
ms.assetid: 6c5e1256-3a92-4bfe-8614-f09d627bc3db
keywords:
- UndoSetConstantBuffer method Direct3D 11
- UndoSetConstantBuffer method Direct3D 11 , ID3DX11EffectConstantBuffer interface
- ID3DX11EffectConstantBuffer interface Direct3D 11 , UndoSetConstantBuffer method
topic_type:
- apiref
api_name:
- ID3DX11EffectConstantBuffer.UndoSetConstantBuffer
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX11EffectConstantBuffer::UndoSetConstantBuffer method

Reverts a previously set constant buffer.

## Syntax


```C++
HRESULT UndoSetConstantBuffer();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



|                    |                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectConstantBuffer](id3dx11effectconstantbuffer.md)
</dt> </dl>

 

 





