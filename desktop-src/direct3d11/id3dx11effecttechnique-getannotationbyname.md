---
title: ID3DX11EffectTechnique GetAnnotationByName method (D3dx11effect.h)
description: Get an annotation by name. | ID3DX11EffectTechnique GetAnnotationByName method (D3dx11effect.h)
ms.assetid: 3a9e1fa7-4586-42d6-a723-3140f29a01b4
keywords:
- GetAnnotationByName method Direct3D 11
- GetAnnotationByName method Direct3D 11 , ID3DX11EffectTechnique interface
- ID3DX11EffectTechnique interface Direct3D 11 , GetAnnotationByName method
topic_type:
- apiref
api_name:
- ID3DX11EffectTechnique.GetAnnotationByName
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectTechnique::GetAnnotationByName method

Get an annotation by name.

## Syntax


```C++
ID3DX11EffectVariable* GetAnnotationByName(
   LPCSTR Name
);
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)**

Name of the annotation.

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

 

