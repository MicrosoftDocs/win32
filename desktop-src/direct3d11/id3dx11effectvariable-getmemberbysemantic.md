---
title: ID3DX11EffectVariable GetMemberBySemantic method (D3dx11effect.h)
description: Get a structure member by semantic.
ms.assetid: e4ae1f6a-43d2-45df-9dba-833d4f767818
keywords:
- GetMemberBySemantic method Direct3D 11
- GetMemberBySemantic method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , GetMemberBySemantic method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.GetMemberBySemantic
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::GetMemberBySemantic method

Get a structure member by semantic.

## Syntax


```C++
ID3DX11EffectVariable* GetMemberBySemantic(
   LPCSTR Semantic
);
```



## Parameters

<dl> <dt>

*Semantic* 
</dt> <dd>

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)**

The semantic.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectVariable**](id3dx11effectvariable.md)\***

A pointer to an [**ID3DX11EffectVariable**](id3dx11effectvariable.md).

## Remarks

If the effect variable is an structure, use this method to look up a member by attached semantic.

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectVariable](id3dx11effectvariable.md)
</dt> </dl>

 

