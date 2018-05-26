---
Description: Specifies the source glyph and location in a monochrome surface to copy glyphs into.
ms.assetid: eda6fc82-6a06-4a59-a3ab-9f7e5c5bb5a1
title: D3DCOMPOSERECTDESTINATION structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DCOMPOSERECTDESTINATION structure

Specifies the source glyph and location in a monochrome surface to copy glyphs into.

## Syntax


```C++
typedef struct _D3DCOMPOSERECTDESTINATION {
  USHORT SrcRectIndex;
  USHORT Reserved;
  USHORT X;
  USHORT Y;
} D3DCOMPOSERECTDESTINATION;
```



## Members

<dl> <dt>

**SrcRectIndex**
</dt> <dd>

Type: **[**USHORT**](winprog.windows_data_types)**

</dd> <dd>

Index particular glyph from vertex buffer containing [**D3DCOMPOSERECTDESC**](d3dcomposerectdesc.md) structures.

</dd> <dt>

**Reserved**
</dt> <dd>

Type: **[**USHORT**](winprog.windows_data_types)**

</dd> <dd>

Reserved for alignment purposes.

</dd> <dt>

**X**
</dt> <dd>

Type: **[**USHORT**](winprog.windows_data_types)**

</dd> <dd>

Left coordinate to begin copy at.

</dd> <dt>

**Y**
</dt> <dd>

Type: **[**USHORT**](winprog.windows_data_types)**

</dd> <dd>

Top coordinate to begin copy at.

</dd> </dl>

## Remarks

This structure is used in calls to [**ComposeRects**](/windows/win32/d3d9/nf-d3d9-idirect3ddevice9ex-composerects?branch=master) to indicate the locaiton glyphs should be copied to and which particular glyph should be copied. A vertex buffer (see [**IDirect3DVertexBuffer9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvertexbuffer9?branch=master)) filled with these structures are created to contain the glyph locations. USHORT members are used to reduce the memory footprint as much as possible.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 




