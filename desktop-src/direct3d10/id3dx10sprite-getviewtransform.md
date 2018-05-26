---
Description: Get the view transform that applies to all sprites.
ms.assetid: eba45c08-64cc-4119-83d4-50351fe21bea
title: ID3DX10SpriteGetViewTransform method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX10Sprite::GetViewTransform method

Get the view transform that applies to all sprites.

## Syntax


```C++
HRESULT GetViewTransform(
  [out] D3DXMATRIX *pViewTransform
);
```



## Parameters

<dl> <dt>

*pViewTransform* \[out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to a [**D3DX10MATRIX**](d3d10-d3dxmatrix.md) that will be set to the transform of the sprite from the original world space.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

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

 

 




