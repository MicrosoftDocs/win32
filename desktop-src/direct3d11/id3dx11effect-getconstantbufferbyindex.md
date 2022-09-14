---
title: ID3DX11Effect GetConstantBufferByIndex method (D3dx11effect.h)
description: Get a constant buffer by index.
ms.assetid: 146b146b-89ff-4d56-9ac7-e67a92a30e26
keywords:
- GetConstantBufferByIndex method Direct3D 11
- GetConstantBufferByIndex method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , GetConstantBufferByIndex method
topic_type:
- apiref
api_name:
- ID3DX11Effect.GetConstantBufferByIndex
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11Effect::GetConstantBufferByIndex method

Get a constant buffer by index.

## Syntax


```C++
ID3DX11EffectConstantBuffer* GetConstantBufferByIndex(
   UINT Index
);
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

A zero-based index.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectConstantBuffer**](id3dx11effectconstantbuffer.md)\***

A pointer to a [**ID3DX11EffectConstantBuffer**](id3dx11effectconstantbuffer.md).

## Remarks

An effect that contains a variable that will be read/written by an application requires at least one constant buffer. For best performance, an effect should organize variables into one or more constant buffers based on their frequency of update.

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11Effect](id3dx11effect.md)
</dt> </dl>

 

