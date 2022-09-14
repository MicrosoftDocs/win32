---
title: ID3DX11Effect GetConstantBufferByName method (D3dx11effect.h)
description: Get a constant buffer by name.
ms.assetid: 11757615-4068-430d-9ab0-f83f02af8e55
keywords:
- GetConstantBufferByName method Direct3D 11
- GetConstantBufferByName method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , GetConstantBufferByName method
topic_type:
- apiref
api_name:
- ID3DX11Effect.GetConstantBufferByName
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11Effect::GetConstantBufferByName method

Get a constant buffer by name.

## Syntax


```C++
ID3DX11EffectConstantBuffer* GetConstantBufferByName(
   LPCSTR Name
);
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)**

The constant-buffer name.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectConstantBuffer**](id3dx11effectconstantbuffer.md)\***

A pointer to the constant buffer indicated by the Name. See [**ID3DX11EffectConstantBuffer**](id3dx11effectconstantbuffer.md).

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

 

