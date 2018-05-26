---
Description: Gets the sprite transform.
ms.assetid: d91f2776-ee87-42b3-998b-fccea178cee2
title: ID3DXSpriteGetTransform method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSprite::GetTransform method

Gets the sprite transform.

## Syntax


```C++
HRESULT GetTransform(
  [in] D3DXMATRIX *pTransform
);
```



## Parameters

<dl> <dt>

*pTransform* \[in\]
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) that contains a transform of the sprite from the original world space.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> </dl>

 

 




