---
title: ID3DX11Effect GetTechniqueByName method (D3dx11effect.h)
description: Get a technique by name. | ID3DX11Effect GetTechniqueByName method (D3dx11effect.h)
ms.assetid: 0f7fa02c-dfbf-4971-86ad-3429f99f84e0
keywords:
- GetTechniqueByName method Direct3D 11
- GetTechniqueByName method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , GetTechniqueByName method
topic_type:
- apiref
api_name:
- ID3DX11Effect.GetTechniqueByName
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11Effect::GetTechniqueByName method

Get a technique by name.

## Syntax


```C++
ID3DX11EffectTechnique* GetTechniqueByName(
   LPCSTR Name
);
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)**

The name of the technique.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectTechnique**](id3dx11effecttechnique.md)\***

A pointer to an [**ID3DX11EffectTechnique**](id3dx11effecttechnique.md). If a technique with the appropriate name is not found an invalid technique is returned. [**ID3DX11EffectTechnique::IsValid**](id3dx11effecttechnique-isvalid.md) should be called on the returned technique to determine whether it is valid.

## Remarks

An effect contains one or more techniques; each technique contains one or more passes. You can access a technique using its name or with an index.

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

 

