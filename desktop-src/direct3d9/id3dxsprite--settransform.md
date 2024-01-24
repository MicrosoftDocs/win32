---
description: Sets the sprite transform.
ms.assetid: 87dfc169-b647-4a96-897d-abbe765ea9e2
title: ID3DXSprite::SetTransform method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSprite.SetTransform
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSprite::SetTransform method

Sets the sprite transform.

## Syntax


```C++
HRESULT SetTransform(
  [in] const D3DXMATRIX *pTransform
);
```



## Parameters

<dl> <dt>

*pTransform* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) that contains a transform of the sprite from the original world space. Use this transform to scale, rotate, or transform the sprite.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> <dt>

[Transforms (Direct3D 9)](transforms.md)
</dt> </dl>

 

 




