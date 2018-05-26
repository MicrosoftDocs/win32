---
Description: Returns a description of the original contents of an image file.
ms.assetid: 40d89166-cc11-490d-867c-ae5db23a0784
title: D3DX10\_IMAGE\_INFO structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10\_IMAGE\_INFO structure

Returns a description of the original contents of an image file.

## Syntax


```C++
typedef struct D3DX10_IMAGE_INFO {
  UINT                     Width;
  UINT                     Height;
  UINT                     Depth;
  UINT                     ArraySize;
  UINT                     MipLevels;
  UINT                     MiscFlags;
  DXGI_FORMAT              Format;
  D3D10_RESOURCE_DIMENSION ResourceDimension;
  D3DX10_IMAGE_FILE_FORMAT ImageFileFormat;
} D3DX10_IMAGE_INFO, *LPD3DX10_IMAGE_INFO;
```



## Members

<dl> <dt>

**Width**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Width of original image in pixels.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Height of original image in pixels.

</dd> <dt>

**Depth**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Depth of original image in pixels.

</dd> <dt>

**ArraySize**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Size of the texture array. *ArraySize* will be 1 for a single image.

</dd> <dt>

**MipLevels**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of mipmap levels in original image.

</dd> <dt>

**MiscFlags**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Miscellaneous resource properties (see [**D3D10\_RESOURCE\_MISC\_FLAG**](/windows/win32/D3D10/ne-d3d10-d3d10_resource_misc_flag?branch=master)).

</dd> <dt>

**Format**
</dt> <dd>

Type: **[**DXGI\_FORMAT**](direct3ddxgi.dxgi_format)**

</dd> <dd>

A value from the [**DXGI\_FORMAT**](direct3ddxgi.dxgi_format) enumerated type that most closely describes the data in the original image.

</dd> <dt>

**ResourceDimension**
</dt> <dd>

Type: **[**D3D10\_RESOURCE\_DIMENSION**](/windows/win32/D3D10/ne-d3d10-d3d10_resource_dimension?branch=master)**

</dd> <dd>

Represents the type of the texture stored in the file. See [**D3D10\_RESOURCE\_DIMENSION**](/windows/win32/D3D10/ne-d3d10-d3d10_resource_dimension?branch=master).

</dd> <dt>

**ImageFileFormat**
</dt> <dd>

Type: **[**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md)**

</dd> <dd>

Represents the format of the image file. See [**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md).

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](d3d10-graphics-reference-d3dx10-structures.md)
</dt> </dl>

 

 




