---
Description: Defines position, texture, and color information about a sprite.
ms.assetid: 4b8d1ed1-75d5-418c-b809-410c6a44d425
title: D3DX10_SPRITE structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10_SPRITE
api_type: 
- HeaderDef
api_location: 
- D3DX10.h
---

# D3DX10\_SPRITE structure

Defines position, texture, and color information about a sprite.

## Syntax


```C++
typedef struct D3DX10_SPRITE {
  D3DXMATRIX               matWorld;
  D3DXVECTOR2              TexCoord;
  D3DXVECTOR2              TexSize;
  D3DXCOLOR                ColorModulate;
  ID3D10ShaderResourceView *pTexture;
  UINT                     TextureIndex;
} D3DX10_SPRITE;
```



## Members

<dl> <dt>

**matWorld**
</dt> <dd>

Type: **[**D3DXMATRIX**](https://msdn.microsoft.com/en-us/library/Bb172912(v=VS.85).aspx)**

</dd> <dd>

The sprite's model-world transformation. This defines the position and orientation of the sprite in world space.

</dd> <dt>

**TexCoord**
</dt> <dd>

Type: **[**D3DXVECTOR2**](https://msdn.microsoft.com/en-us/library/Bb205544(v=VS.85).aspx)**

</dd> <dd>

Offset from the upper-left corner of the texture indicating where the sprite image should start in the texture. **TexCoord** is in texture coordinates.

</dd> <dt>

**TexSize**
</dt> <dd>

Type: **[**D3DXVECTOR2**](https://msdn.microsoft.com/en-us/library/Bb205544(v=VS.85).aspx)**

</dd> <dd>

A vector containing the width and height of the sprite in texture coordinates.

</dd> <dt>

**ColorModulate**
</dt> <dd>

Type: **[**D3DXCOLOR**](https://msdn.microsoft.com/en-us/library/Bb172721(v=VS.85).aspx)**

</dd> <dd>

A color that will be multiplied with the pixel color before rendering.

</dd> <dt>

**pTexture**
</dt> <dd>

Type: **[**ID3D10ShaderResourceView**](/windows/desktop/api/d3d10/nn-d3d10-id3d10shaderresourceview)\***

</dd> <dd>

Pointer to a shader-resource view representing the sprite's texture. See [**ID3D10ShaderResourceView Interface**](/windows/desktop/api/d3d10/nn-d3d10-id3d10shaderresourceview).

</dd> <dt>

**TextureIndex**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

The index of the texture. If pTexture does not represent a texture array, then this should be 0.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](d3d10-graphics-reference-d3dx10-structures.md)
</dt> </dl>

 

 




