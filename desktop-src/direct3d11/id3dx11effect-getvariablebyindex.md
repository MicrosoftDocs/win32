---
title: ID3DX11Effect GetVariableByIndex method (D3dx11effect.h)
description: Get a variable by index.
ms.assetid: af25b945-9526-45c2-8746-8b62f8166de7
keywords:
- GetVariableByIndex method Direct3D 11
- GetVariableByIndex method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , GetVariableByIndex method
topic_type:
- apiref
api_name:
- ID3DX11Effect.GetVariableByIndex
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11Effect::GetVariableByIndex method

Get a variable by index.

## Syntax


```C++
ID3DX11EffectVariable* GetVariableByIndex(
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

Type: **[**ID3DX11EffectVariable**](id3dx11effectvariable.md)\***

A pointer to a [**ID3DX11EffectVariable**](id3dx11effectvariable.md).

## Remarks

An effect may contain one or more variables. Variables outside of a technique are considered global to all effects, those located inside of a technique are local to that technique. You can access any local non-static effect variable using its name or with an index.

The method returns a pointer to an [**effect-variable interface**](id3dx11effectvariable.md) if a variable is not found; you can call [**ID3DX11Effect::IsValid**](id3dx11effect-isvalid.md) to verify whether or not the index exists.

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

 

