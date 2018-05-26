---
Description: Set the projection matrix for all sprites.
ms.assetid: cb4c5546-1a31-40d9-a943-af4fbddcee01
title: ID3DX10SpriteSetProjectionTransform method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX10Sprite::SetProjectionTransform method

Set the projection matrix for all sprites.

## Syntax


```C++
HRESULT SetProjectionTransform(
  [in] D3DXMATRIX *pProjectionTransform
);
```



## Parameters

<dl> <dt>

*pProjectionTransform* \[in\]
</dt> <dd>

Type: **[**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

The projection matrix to be used on all sprites.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




