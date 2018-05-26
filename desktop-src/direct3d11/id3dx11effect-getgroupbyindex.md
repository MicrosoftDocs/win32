---
title: ID3DX11Effect GetGroupByIndex method
description: Gets an effect group by index.
ms.assetid: b38ecdbf-0920-48ff-a599-9629a3581d75
keywords:
- GetGroupByIndex method Direct3D 11
- GetGroupByIndex method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , GetGroupByIndex method
topic_type:
- apiref
api_name:
- ID3DX11Effect.GetGroupByIndex
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

# ID3DX11Effect::GetGroupByIndex method

Gets an effect group by index.

## Syntax


```C++
ID3DX11EffectGroup* GetGroupByIndex(
   UINT Index
);
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Index of the effect group.

</dd> </dl>

## Return value

Type: **[**ID3DX11EffectGroup**](id3dx11effectgroup.md)\***

A pointer to an [**ID3DX11EffectGroup**](id3dx11effectgroup.md) interface.

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

[ID3DX11Effect](id3dx11effect.md)
</dt> </dl>

 

 





