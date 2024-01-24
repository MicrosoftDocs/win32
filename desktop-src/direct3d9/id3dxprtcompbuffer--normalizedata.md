---
description: Normalizes all principal component analysis (PCA) weights so that they are between -1 and 1. Basis vectors are modified to reflect this normalization.
ms.assetid: f1c87049-a1ec-452e-b556-a2dc95324d5d
title: ID3DXPRTCompBuffer::NormalizeData method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTCompBuffer.NormalizeData
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTCompBuffer::NormalizeData method

Normalizes all principal component analysis (PCA) weights so that they are between -1 and 1. Basis vectors are modified to reflect this normalization.

## Syntax


```C++
HRESULT NormalizeData();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTCompBuffer](id3dxprtcompbuffer.md)
</dt> </dl>

 

 




