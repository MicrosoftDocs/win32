---
Description: Information about the properties of a display mode.
ms.assetid: df9d12b9-7acb-435b-9d54-0b095c871f0e
title: D3DDISPLAYMODEEX structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DDISPLAYMODEEX structure

Information about the properties of a display mode.

## Syntax


```C++
typedef struct {
  UINT                Size;
  UINT                Width;
  UINT                Height;
  UINT                RefreshRate;
  D3DFORMAT           Format;
  D3DSCANLINEORDERING ScanLineOrdering;
} D3DDISPLAYMODEEX;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

The size of this structure. This should always be set to sizeof(D3DDISPLAYMODEEX).

</dd> <dt>

**Width**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Width of the display mode.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Height of the display mode.

</dd> <dt>

**RefreshRate**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Refresh rate of the display mode.

</dd> <dt>

**Format**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

Format of the display mode. See [D3DFORMAT](d3dformat.md).

</dd> <dt>

**ScanLineOrdering**
</dt> <dd>

Type: **[**D3DSCANLINEORDERING**](direct3d9.d3dscanlineordering)**

</dd> <dd>

Indicates whether the scanline order is progressive or interlaced. See [**D3DSCANLINEORDERING**](direct3d9.d3dscanlineordering).

</dd> </dl>

## Remarks

This structure is used in various methods to create and manage Direct3D 9Ex devices ([**IDirect3DDevice9Ex**](/windows/win32/d3d9/nn-d3d9-idirect3ddevice9ex?branch=master)) and swapchains ([**IDirect3DSwapChain9Ex**](/windows/win32/d3d9/nn-d3d9-idirect3dswapchain9ex?branch=master)).

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 




