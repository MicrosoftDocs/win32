---
title: ID3DX11EffectTechnique GetAnnotationByIndex method (D3dx11effect.h)
description: Get an annotation by index. | ID3DX11EffectTechnique GetAnnotationByIndex method (D3dx11effect.h)
ms.assetid: 703663b0-ee00-4686-a038-6c99ce61266b
keywords:
- GetAnnotationByIndex method Direct3D 11
- GetAnnotationByIndex method Direct3D 11 , ID3DX11EffectTechnique interface
- ID3DX11EffectTechnique interface Direct3D 11 , GetAnnotationByIndex method
topic_type:
- apiref
api_name:
- ID3DX11EffectTechnique.GetAnnotationByIndex
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectTechnique::GetAnnotationByIndex method

Get an annotation by index.

## Syntax


```C++
ID3DX11EffectVariable* GetAnnotationByIndex(
   UINT Index
);
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The zero-based index of the interface pointer.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectVariable**](id3dx11effectvariable.md)\***

A pointer to an [**ID3DX11EffectVariable**](id3dx11effectvariable.md).

## Remarks

Use an annotation to attach a piece of metadata to a technique.

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

 

