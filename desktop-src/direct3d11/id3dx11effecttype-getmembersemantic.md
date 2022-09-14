---
title: ID3DX11EffectType GetMemberSemantic method (D3dx11effect.h)
description: Get the semantic attached to a member.
ms.assetid: e0666d4e-7510-4496-849e-a0531238b5f8
keywords:
- GetMemberSemantic method Direct3D 11
- GetMemberSemantic method Direct3D 11 , ID3DX11EffectType interface
- ID3DX11EffectType interface Direct3D 11 , GetMemberSemantic method
topic_type:
- apiref
api_name:
- ID3DX11EffectType.GetMemberSemantic
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectType::GetMemberSemantic method

Get the semantic attached to a member.

## Syntax


```C++
LPCSTR GetMemberSemantic(
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

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)**

A string that contains the semantic.

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

 

