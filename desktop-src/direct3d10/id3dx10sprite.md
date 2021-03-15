---
description: The ID3DX10Sprite interface provides a set of methods that simplify the process of drawing sprites using Microsoft Direct3D. This interface can operate on a set of many sprites.
ms.assetid: 3703f272-f631-41c0-a0d5-e7cf2d4ae145
title: ID3DX10Sprite interface (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Sprite
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Sprite interface

The ID3DX10Sprite interface provides a set of methods that simplify the process of drawing sprites using Microsoft Direct3D. This interface can operate on a set of many sprites.

## Members

The **ID3DX10Sprite** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX10Sprite** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX10Sprite** interface has these methods.



| Method                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:-----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Begin**](id3dx10sprite-begin.md)                                   | Prepare a device for drawing sprites.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**DrawSpritesBuffered**](id3dx10sprite-drawspritesbuffered.md)       | Add an array of sprites to the batch of sprites to be rendered. This must be called in between calls to [**ID3DX10Sprite::Begin**](id3dx10sprite-begin.md) and [**ID3DX10Sprite::End**](id3dx10sprite-end.md), and [**ID3DX10Sprite::Flush**](id3dx10sprite-flush.md) must be called before End to send all of the batched sprites to the device for rendering. This draw method is most useful when drawing a small number of sprites that you want buffered into a large batch, such as fonts.<br/>                                                                                                                                                                              |
| [**DrawSpritesImmediate**](id3dx10sprite-drawspritesimmediate.md)     | Draw an array of sprites. This will immediately send the sprites to the device for rendering, which is different from [**ID3DX10Sprite::DrawSpritesBuffered**](id3dx10sprite-drawspritesbuffered.md) which only adds an array of sprites to a batch of sprites to be rendered when [**ID3DX10Sprite::Flush**](id3dx10sprite-flush.md) is called. This draw method is most useful when drawing a large number of sprites that have already been sorted on the CPU (or do not need to be sorted), such as in a particle system. This must be called in between calls to [**ID3DX10Sprite::Begin**](id3dx10sprite-begin.md) and [**ID3DX10Sprite::End**](id3dx10sprite-end.md).<br/> |
| [**End**](id3dx10sprite-end.md)                                       | Call this after ID3DX10Sprite::Flush. If D3DX10\_SPRITE\_SAVE\_STATE was specified when ID3DX10Sprite::Begin was called, this API will restore the device state to how it was before ID3DX10Sprite::Begin was called.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**Flush**](id3dx10sprite-flush.md)                                   | Force all batched sprites to be submitted to the device. Device states remain as they were after the last call to ID3DX10Sprite::Begin. The list of batched sprites is then cleared.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**GetDevice**](id3dx10sprite-getdevice.md)                           | Retrieve the device associated with the sprite object.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**GetProjectionTransform**](id3dx10sprite-getprojectiontransform.md) | Get the sprite projection matrix that is applied to all sprites.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**GetViewTransform**](id3dx10sprite-getviewtransform.md)             | Get the view transform that applies to all sprites.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**SetProjectionTransform**](id3dx10sprite-setprojectiontransform.md) | Set the projection matrix for all sprites.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**SetViewTransform**](id3dx10sprite-setviewtransform.md)             | Set the view transform that applies to all sprites.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

## Remarks

The ID3DX10Sprite interface is obtained by calling the [**D3DX10CreateSprite**](d3dx10createsprite.md) function.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
