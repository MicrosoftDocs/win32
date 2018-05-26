---
title: ID3DX11Effect GetDevice method
description: Get the device that created the effect.
ms.assetid: efcc0358-9842-46eb-a521-ea220ec18735
keywords:
- GetDevice method Direct3D 11
- GetDevice method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , GetDevice method
topic_type:
- apiref
api_name:
- ID3DX11Effect.GetDevice
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

# ID3DX11Effect::GetDevice method

Get the device that created the effect.

## Syntax


```C++
HRESULT GetDevice(
   ID3D11Device **ppDevice
);
```



## Parameters

<dl> <dt>

*ppDevice* 
</dt> <dd>

Type: **[**ID3D11Device**](/windows/win32/D3D11/nn-d3d11-id3d11device?branch=master)\*\***

A pointer to an [**ID3D11Device**](/windows/win32/D3D11/nn-d3d11-id3d11device?branch=master).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

An effect is created for a specific device, by calling a function such as [**D3DX11CreateEffectFromMemory**](d3dx11createeffectfrommemory.md).

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



|                    |                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11Effect](id3dx11effect.md)
</dt> </dl>

 

 





