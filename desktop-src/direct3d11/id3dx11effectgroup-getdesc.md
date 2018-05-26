---
title: ID3DX11EffectGroup GetDesc method
description: Gets a group description.
ms.assetid: 04bb707a-be21-43d1-8d9d-5a84d29fda74
keywords:
- GetDesc method Direct3D 11
- GetDesc method Direct3D 11 , ID3DX11EffectGroup interface
- ID3DX11EffectGroup interface Direct3D 11 , GetDesc method
topic_type:
- apiref
api_name:
- ID3DX11EffectGroup.GetDesc
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

# ID3DX11EffectGroup::GetDesc method

Gets a group description.

## Syntax


```C++
HRESULT GetDesc(
   D3DX11_GROUP_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*pDesc* 
</dt> <dd>

Type: **[**D3DX11\_GROUP\_DESC**](d3dx11-group-desc.md)\***

A pointer to a [**D3DX11\_GROUP\_DESC**](d3dx11-group-desc.md) structure.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

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

[ID3DX11EffectGroup](id3dx11effectgroup.md)
</dt> </dl>

 

 





