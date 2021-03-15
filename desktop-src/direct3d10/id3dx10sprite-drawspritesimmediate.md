---
description: Draw an array of sprites.
ms.assetid: 3fcc7705-0d59-450e-b137-c9cb7ec6b1ea
title: ID3DX10Sprite::DrawSpritesImmediate method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Sprite.DrawSpritesImmediate
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Sprite::DrawSpritesImmediate method

Draw an array of sprites. This will immediately send the sprites to the device for rendering, which is different from [**ID3DX10Sprite::DrawSpritesBuffered**](id3dx10sprite-drawspritesbuffered.md) which only adds an array of sprites to a batch of sprites to be rendered when [**ID3DX10Sprite::Flush**](id3dx10sprite-flush.md) is called. This draw method is most useful when drawing a large number of sprites that have already been sorted on the CPU (or do not need to be sorted), such as in a particle system. This must be called in between calls to [**ID3DX10Sprite::Begin**](id3dx10sprite-begin.md) and [**ID3DX10Sprite::End**](id3dx10sprite-end.md).

## Syntax


```C++
HRESULT DrawSpritesImmediate(
  [in] D3DX10_SPRITE *pSprites,
  [in] UINT          cSprites,
  [in] UINT          cbSprite,
  [in] UINT          flags
);
```



## Parameters

<dl> <dt>

*pSprites* \[in\]
</dt> <dd>

Type: **[**D3DX10\_SPRITE**](d3dx10-sprite.md)\***

The array of sprites to draw. See [**D3DX10\_SPRITE**](d3dx10-sprite.md).

</dd> <dt>

*cSprites* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of sprites in pSprites.

</dd> <dt>

*cbSprite* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The size of the sprite structure you are passing into pSprites. Passing in 0 is the equivalent of passing in sizeof(D3DX10\_SPRITE).

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Reserved.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Sprite](id3dx10sprite.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
