---
title: ID3DX11EffectTechnique GetPassByName method (D3dx11effect.h)
description: Get a pass by name.
ms.assetid: 07c7502e-2af9-4898-8cd4-106d6814fb85
keywords:
- GetPassByName method Direct3D 11
- GetPassByName method Direct3D 11 , ID3DX11EffectTechnique interface
- ID3DX11EffectTechnique interface Direct3D 11 , GetPassByName method
topic_type:
- apiref
api_name:
- ID3DX11EffectTechnique.GetPassByName
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectTechnique::GetPassByName method

Get a pass by name.

## Syntax


```C++
ID3DX11EffectPass* GetPassByName(
   LPCSTR Name
);
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)**

The name of the pass.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectPass**](id3dx11effectpass.md)\***

A pointer to an [**ID3DX11EffectPass**](id3dx11effectpass.md).

## Remarks

A technique contains one or more passes; get a pass using a name or an index.

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectTechnique](id3dx11effecttechnique.md)
</dt> </dl>

 

