---
description: Sets the right-handed world-view transform for a sprite. A call to this method is required before billboarding or sorting sprites.
ms.assetid: 83654e9a-8991-49ec-ab28-cf9063126dbe
title: ID3DXSprite::SetWorldViewRH method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSprite.SetWorldViewRH
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSprite::SetWorldViewRH method

Sets the right-handed world-view transform for a sprite. A call to this method is required before billboarding or sorting sprites.

## Syntax


```C++
HRESULT SetWorldViewRH(
  [in] const D3DXMATRIX *pWorld,
  [in] const D3DXMATRIX *pView
);
```



## Parameters

<dl> <dt>

*pWorld* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) that contains a world transform. If **NULL**, the identity matrix is used for the world transform.

</dd> <dt>

*pView* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) that contains a view transform. If **NULL**, the identity matrix is used for the view transform.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

A call to this method (or to [**ID3DXSprite::SetWorldViewLH**](id3dxsprite--setworldviewlh.md)) is required if the sprite will be rendered with the [D3DXSprite\_\_BILLBOARD](d3dxsprite.md), D3DXSprite\_\_SORT\_DEPTH\_FRONTTOBACK, or D3DXSprite\_\_SORT\_DEPTH\_BACKTOFRONT flag value in [**ID3DXSprite::Begin**](id3dxsprite--begin.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSprite](id3dxsprite.md)
</dt> </dl>

 

 




