---
description: Returns a description of the original contents of an image file.
ms.assetid: d6cbd5b7-642e-43ce-a2ed-11a400c5bdc1
title: D3DXIMAGE_INFO structure (D3dx9tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXIMAGE_INFO
api_type: 
- HeaderDef
api_location: 
- d3dx9tex.h
---

# D3DXIMAGE\_INFO structure

Returns a description of the original contents of an image file.

## Syntax


```C++
typedef struct D3DXIMAGE_INFO {
  UINT                 Width;
  UINT                 Height;
  UINT                 Depth;
  UINT                 MipLevels;
  D3DFORMAT            Format;
  D3DRESOURCETYPE      ResourceType;
  D3DXIMAGE_FILEFORMAT ImageFileFormat;
} D3DXIMAGE_INFO, *LPD3DXIMAGE_INFO;
```



## Members

<dl> <dt>

**Width**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Width of original image in pixels.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Height of original image in pixels.

</dd> <dt>

**Depth**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Depth of original image in pixels.

</dd> <dt>

**MipLevels**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of mip levels in original image.

</dd> <dt>

**Format**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

A value from the [D3DFORMAT](d3dformat.md) enumerated type that most closely describes the data in the original image.

</dd> <dt>

**ResourceType**
</dt> <dd>

Type: **[**D3DRESOURCETYPE**](./d3dresourcetype.md)**

</dd> <dd>

Represents the type of the texture stored in the file. It is either D3DRTYPE\_TEXTURE, D3DRTYPE\_VOLUMETEXTURE, or D3DRTYPE\_CubeTexture.

</dd> <dt>

**ImageFileFormat**
</dt> <dd>

Type: **[**D3DXIMAGE\_FILEFORMAT**](./d3dximage-fileformat.md)**

</dd> <dd>

Represents the format of the image file.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9tex.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 
