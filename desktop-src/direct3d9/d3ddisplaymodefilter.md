---
description: Specifies types of display modes to filter out.
ms.assetid: 4a03d0f0-dec5-4209-8c99-b58cc13064f5
title: D3DDISPLAYMODEFILTER structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DDISPLAYMODEFILTER
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DDISPLAYMODEFILTER structure

Specifies types of display modes to filter out.

## Syntax


```C++
typedef struct {
  UINT                Size;
  D3DFORMAT           Format;
  D3DSCANLINEORDERING ScanLineOrdering;
} D3DDISPLAYMODEFILTER;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

The size of this structure. This should always be set to sizeof(D3DDISPLAYMODEFILTER).

</dd> <dt>

**Format**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

The display mode format to filter out. See [D3DFORMAT](d3dformat.md).

</dd> <dt>

**ScanLineOrdering**
</dt> <dd>

Type: **[**D3DSCANLINEORDERING**](./d3dscanlineordering.md)**

</dd> <dd>

Whether the scanline ordering is interlaced or progressive. See [**D3DSCANLINEORDERING**](./d3dscanlineordering.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 
