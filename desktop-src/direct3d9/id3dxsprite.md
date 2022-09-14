---
description: The ID3DXSprite interface provides a set of methods that simplify the process of drawing sprites using Microsoft Direct3D.
ms.assetid: ccf34fac-91a7-4734-bc62-aedaf4d66522
title: ID3DXSprite interface (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSprite
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSprite interface

The ID3DXSprite interface provides a set of methods that simplify the process of drawing sprites using Microsoft Direct3D.

## Members

The **ID3DXSprite** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXSprite** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXSprite** interface has these methods.



| Method                                                | Description                                                                                                                                                                                                                  |
|:------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Begin**](id3dxsprite--begin.md)                   | Prepares a device for drawing sprites.<br/>                                                                                                                                                                            |
| [**Draw**](id3dxsprite--draw.md)                     | Adds a sprite to the list of batched sprites.<br/>                                                                                                                                                                     |
| [**End**](id3dxsprite--end.md)                       | Calls [**ID3DXSprite::Flush**](id3dxsprite--flush.md) and restores the device state to how it was before [**ID3DXSprite::Begin**](id3dxsprite--begin.md) was called.<br/>                                            |
| [**Flush**](id3dxsprite--flush.md)                   | Forces all batched sprites to be submitted to the device. Device states remain as they were after the last call to [**ID3DXSprite::Begin**](id3dxsprite--begin.md). The list of batched sprites is then cleared.<br/> |
| [**GetDevice**](id3dxsprite--getdevice.md)           | Retrieves the device associated with the sprite object.<br/>                                                                                                                                                           |
| [**GetTransform**](id3dxsprite--gettransform.md)     | Gets the sprite transform.<br/>                                                                                                                                                                                        |
| [**OnLostDevice**](id3dxsprite--onlostdevice.md)     | Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost or before resetting a device.<br/>                              |
| [**OnResetDevice**](id3dxsprite--onresetdevice.md)   | Use this method to re-acquire resources and save initial state.<br/>                                                                                                                                                   |
| [**SetTransform**](id3dxsprite--settransform.md)     | Sets the sprite transform.<br/>                                                                                                                                                                                        |
| [**SetWorldViewLH**](id3dxsprite--setworldviewlh.md) | Sets the left-handed world-view transform for a sprite. A call to this method is required before billboarding or sorting sprites.<br/>                                                                                 |
| [**SetWorldViewRH**](id3dxsprite--setworldviewrh.md) | Sets the right-handed world-view transform for a sprite. A call to this method is required before billboarding or sorting sprites.<br/>                                                                                |



 

## Remarks

The **ID3DXSprite** interface is obtained by calling the [**D3DXCreateSprite**](d3dxcreatesprite.md) function.

The application typically first calls [**ID3DXSprite::Begin**](id3dxsprite--begin.md), which allows control over the device render state, alpha blending, and sprite transformation and sorting. Then for each sprite to be displayed, call [**ID3DXSprite::Draw**](id3dxsprite--draw.md). **ID3DXSprite::Draw** can be called repeatedly to store any number of sprites. To display the batched sprites to the device, call [**ID3DXSprite::End**](id3dxsprite--end.md) or [**ID3DXSprite::Flush**](id3dxsprite--flush.md).

The LPD3DXSPRITE type is defined as a pointer to the **ID3DXSprite** interface.


```
typedef interface ID3DXSprite ID3DXSprite;
typedef interface ID3DXSprite *LPD3DXSPRITE;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
