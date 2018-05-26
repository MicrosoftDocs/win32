---
title: ID3DX11EffectPass GetAnnotationByName method
description: Get an annotation by name.
ms.assetid: b54a4fb0-62c7-4d96-af30-f9ae04ff7dab
keywords:
- GetAnnotationByName method Direct3D 11
- GetAnnotationByName method Direct3D 11 , ID3DX11EffectPass interface
- ID3DX11EffectPass interface Direct3D 11 , GetAnnotationByName method
topic_type:
- apiref
api_name:
- ID3DX11EffectPass.GetAnnotationByName
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX11EffectPass::GetAnnotationByName method

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

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The name of the annotation.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectVariable**](id3dx11effectvariable.md)\***

A pointer to an [**ID3DX11EffectVariable**](id3dx11effectvariable.md).

## Remarks

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



|                    |                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectPass](id3dx11effectpass.md)
</dt> </dl>

 

 





