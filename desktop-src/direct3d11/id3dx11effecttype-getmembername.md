---
title: ID3DX11EffectType GetMemberName method
description: Get the name of a member.
ms.assetid: cd231741-09e1-4e69-9384-5cdfbf83fc8b
keywords:
- GetMemberName method Direct3D 11
- GetMemberName method Direct3D 11 , ID3DX11EffectType interface
- ID3DX11EffectType interface Direct3D 11 , GetMemberName method
topic_type:
- apiref
api_name:
- ID3DX11EffectType.GetMemberName
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

# ID3DX11EffectType::GetMemberName method

Get the name of a member.

## Syntax


```C++
LPCSTR GetMemberName(
   UINT Index
);
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A zero-based index.

</dd> </dl>

## Return value

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The name of the member.

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

[ID3DX11EffectType](id3dx11effecttype.md)
</dt> </dl>

 

 





