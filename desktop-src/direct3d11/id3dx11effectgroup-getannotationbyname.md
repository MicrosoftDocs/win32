---
title: ID3DX11EffectGroup GetAnnotationByName method (D3dx11effect.h)
description: Get an annotation by name. | ID3DX11EffectGroup GetAnnotationByName method (D3dx11effect.h)
ms.assetid: c526a249-fb56-47bb-a0c2-b829a1da88e8
keywords:
- GetAnnotationByName method Direct3D 11
- GetAnnotationByName method Direct3D 11 , ID3DX11EffectGroup interface
- ID3DX11EffectGroup interface Direct3D 11 , GetAnnotationByName method
topic_type:
- apiref
api_name:
- ID3DX11EffectGroup.GetAnnotationByName
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectGroup::GetAnnotationByName method

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

The name of the annotation.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectVariable**](id3dx11effectvariable.md)\***

A pointer to an [**ID3DX11EffectVariable**](id3dx11effectvariable.md). Note that if the annotation is not found the **ID3DX11EffectVariable** returned will be empty. The [**ID3DX11EffectVariable::IsValid**](id3dx11effectvariable-isvalid.md) method should be called to determine whether the annotation was found.

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

[ID3DX11EffectGroup](id3dx11effectgroup.md)
</dt> </dl>

 

