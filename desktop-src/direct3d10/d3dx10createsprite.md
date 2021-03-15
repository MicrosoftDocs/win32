---
description: Create a sprite for drawing a 2D texture.Note  Instead of using this function, we recommend that you use Direct2D and the DirectXTK library, SpriteBatch class.
ms.assetid: 64efb8e4-da0b-4e67-874a-e0bb0083961c
title: D3DX10CreateSprite function (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10CreateSprite
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DX10CreateSprite function

Create a sprite for drawing a 2D texture.

> [!Note]  
> Instead of using this function, we recommend that you use [Direct2D](../direct2d/direct2d-portal.md) and the [DirectXTK](https://github.com/Microsoft/DirectXTK) library, **SpriteBatch** class.

 

## Syntax


```C++
HRESULT D3DX10CreateSprite(
  _In_  ID3D10Device   *pDevice,
  _In_  UINT           cDeviceBufferSize,
  _Out_ LPD3DX10SPRITE *ppSprite
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)\***

A pointer to the device (see [**ID3D10Device Interface**](/windows/desktop/api/D3D10/nn-d3d10-id3d10device)) that will draw the sprite.

</dd> <dt>

*cDeviceBufferSize* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The size of the vertex buffer, in number of sprites, that will be sent to the device when [**ID3DX10Sprite::Flush**](id3dx10sprite-flush.md) or [**ID3DX10Sprite::DrawSpritesImmediate**](id3dx10sprite-drawspritesimmediate.md) is called. This should be a small number if you know you will be rendering a small number of sprites at a time (to save memory) and a large number if you know you will be rendering a large number of sprites at a time. The maximum value is 4096. If 0 is specified, the vertex buffer size will automatically be set to 4096.

</dd> <dt>

*ppSprite* \[out\]
</dt> <dd>

Type: **[**LPD3DX10SPRITE**](id3dx10sprite.md)\***

The address of a pointer to a sprite interface (see [**ID3DX10Sprite Interface**](id3dx10sprite.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 
