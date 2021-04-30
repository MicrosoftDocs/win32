---
description: Describes an off-screen render target used by an instance of ID3DXRenderToEnvMap.
ms.assetid: 805df4da-e882-4d54-bf2c-49cfcbc59ac6
title: D3DXRTE_DESC structure (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXRTE_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9core.h
---

# D3DXRTE\_DESC structure

Describes an off-screen render target used by an instance of [**ID3DXRenderToEnvMap**](id3dxrendertoenvmap.md).

## Syntax


```C++
typedef struct D3DXRTE_DESC {
  UINT      Size;
  UINT      MipLevels;
  D3DFORMAT Format;
  BOOL      DepthStencil;
  D3DFORMAT DepthStencilFormat;
} D3DXRTE_DESC, *LPD3DXRTE_DESC;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Width and height in pixels.

</dd> <dt>

**MipLevels**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Maximum level of detail (LOD) number.

</dd> <dt>

**Format**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

Color buffer format.

</dd> <dt>

**DepthStencil**
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

</dd> <dd>

Indicates if the z-buffer is needed.

</dd> <dt>

**DepthStencilFormat**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

Format of the depth buffer.

</dd> </dl>

## Remarks

This method is used to return the creation parameters used when creating an [**ID3DXRenderToEnvMap**](id3dxrendertoenvmap.md) object.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9core.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 
