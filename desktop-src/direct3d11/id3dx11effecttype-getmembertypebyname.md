---
title: ID3DX11EffectType GetMemberTypeByName method (D3dx11effect.h)
description: Get an member type by name.
ms.assetid: 0c5a732b-7c3a-41da-b7de-dc464eed814a
keywords:
- GetMemberTypeByName method Direct3D 11
- GetMemberTypeByName method Direct3D 11 , ID3DX11EffectType interface
- ID3DX11EffectType interface Direct3D 11 , GetMemberTypeByName method
topic_type:
- apiref
api_name:
- ID3DX11EffectType.GetMemberTypeByName
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectType::GetMemberTypeByName method

Get an member type by name.

## Syntax


```C++
ID3DX11EffectType* GetMemberTypeByName(
   LPCSTR Name
);
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)**

A member's name.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectType**](id3dx11effecttype.md)\***

A pointer to an [**ID3DX11EffectType**](id3dx11effecttype.md).

## Remarks

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectType](id3dx11effecttype.md)
</dt> </dl>

 

