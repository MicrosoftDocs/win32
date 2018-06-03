---
title: ID3DX11Effect GetGroupByName method
description: Gets an effect group by name.
ms.assetid: 14b4b484-848a-409c-9a99-207ab25b7566
keywords:
- GetGroupByName method Direct3D 11
- GetGroupByName method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , GetGroupByName method
topic_type:
- apiref
api_name:
- ID3DX11Effect.GetGroupByName
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX11Effect::GetGroupByName method

Gets an effect group by name.

## Syntax


```C++
ID3DX11EffectGroup* GetGroupByName(
   LPCSTR Name
);
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Name of the effect group.

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

 

 





