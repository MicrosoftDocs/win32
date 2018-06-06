---
Description: Get the sprite projection matrix that is applied to all sprites.
ms.assetid: aee65a9f-27f9-42d9-98eb-ae90fc18c7f5
title: ID3DX10Sprite::GetProjectionTransform method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX10Sprite::GetProjectionTransform method

Get the sprite projection matrix that is applied to all sprites.

## Syntax


```C++
HRESULT GetProjectionTransform(
  [out] D3DXMATRIX *pProjectionTransform
);
```



## Parameters

<dl> <dt>

*pProjectionTransform* \[out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxmatrix.htm)\***

Pointer to a [**D3DX10MATRIX**](d3d10-d3dxmatrix.md) that will be set to the sprite's projection matrix.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Sprite](id3dx10sprite.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




