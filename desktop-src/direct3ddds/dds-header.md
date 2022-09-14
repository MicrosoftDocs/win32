---
title: DDS_HEADER structure (Dds.h)
description: Describes a DDS file header.
ms.assetid: 7f8bde30-0ff9-4bb9-b444-5c875e6a0865
keywords:
- DDS_HEADER structure DDS
topic_type:
- apiref
api_name:
- DDS_HEADER
api_location:
- Dds.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DDS\_HEADER structure

Describes a DDS file header.

## Syntax


```C++
typedef struct {
  DWORD           dwSize;
  DWORD           dwFlags;
  DWORD           dwHeight;
  DWORD           dwWidth;
  DWORD           dwPitchOrLinearSize;
  DWORD           dwDepth;
  DWORD           dwMipMapCount;
  DWORD           dwReserved1[11];
  DDS_PIXELFORMAT ddspf;
  DWORD           dwCaps;
  DWORD           dwCaps2;
  DWORD           dwCaps3;
  DWORD           dwCaps4;
  DWORD           dwReserved2;
} DDS_HEADER;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Size of structure. This member must be set to 124.

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Flags to indicate which members contain valid data.



| Flag              | Description                                                  | Value    |
|-------------------|--------------------------------------------------------------|----------|
| DDSD\_CAPS        | Required in every .dds file.                                 | 0x1      |
| DDSD\_HEIGHT      | Required in every .dds file.                                 | 0x2      |
| DDSD\_WIDTH       | Required in every .dds file.                                 | 0x4      |
| DDSD\_PITCH       | Required when pitch is provided for an uncompressed texture. | 0x8      |
| DDSD\_PIXELFORMAT | Required in every .dds file.                                 | 0x1000   |
| DDSD\_MIPMAPCOUNT | Required in a mipmapped texture.                             | 0x20000  |
| DDSD\_LINEARSIZE  | Required when pitch is provided for a compressed texture.    | 0x80000  |
| DDSD\_DEPTH       | Required in a depth texture.                                 | 0x800000 |



 

> [!Note]  
> When you write .dds files, you should set the DDSD\_CAPS and DDSD\_PIXELFORMAT flags, and for mipmapped textures you should also set the DDSD\_MIPMAPCOUNT flag. However, when you read a .dds file, you should not rely on the DDSD\_CAPS, DDSD\_PIXELFORMAT, and DDSD\_MIPMAPCOUNT flags being set because some writers of such a file might not set these flags.

 

The DDS\_HEADER\_FLAGS\_TEXTURE flag, which is defined in Dds.h, is a bitwise-OR combination of the DDSD\_CAPS, DDSD\_HEIGHT, DDSD\_WIDTH, and DDSD\_PIXELFORMAT flags.

The DDS\_HEADER\_FLAGS\_MIPMAP flag, which is defined in Dds.h, is equal to the DDSD\_MIPMAPCOUNT flag.

The DDS\_HEADER\_FLAGS\_VOLUME flag, which is defined in Dds.h, is equal to the DDSD\_DEPTH flag.

The DDS\_HEADER\_FLAGS\_PITCH flag, which is defined in Dds.h, is equal to the DDSD\_PITCH flag.

The DDS\_HEADER\_FLAGS\_LINEARSIZE flag, which is defined in Dds.h, is equal to the DDSD\_LINEARSIZE flag.

</dd> <dt>

**dwHeight**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Surface height (in pixels).

</dd> <dt>

**dwWidth**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Surface width (in pixels).

</dd> <dt>

**dwPitchOrLinearSize**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

The pitch or number of bytes per scan line in an uncompressed texture; the total number of bytes in the top level texture for a compressed texture. For information about how to compute the pitch, see the DDS File Layout section of the [Programming Guide for DDS](dx-graphics-dds-pguide.md).

</dd> <dt>

**dwDepth**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Depth of a volume texture (in pixels), otherwise unused.

</dd> <dt>

**dwMipMapCount**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Number of mipmap levels, otherwise unused.

</dd> <dt>

**dwReserved1\[11\]**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Unused.

</dd> <dt>

**ddspf**
</dt> <dd>

Type: **[**DDS\_PIXELFORMAT**](dds-pixelformat.md)**

</dd> <dd>

The pixel format (see [**DDS\_PIXELFORMAT**](dds-pixelformat.md)).

</dd> <dt>

**dwCaps**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Specifies the complexity of the surfaces stored.



| Flag             | Description                                                                                                                              | Value    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------|
| DDSCAPS\_COMPLEX | Optional; must be used on any file that contains more than one surface (a mipmap, a cubic environment map, or mipmapped volume texture). | 0x8      |
| DDSCAPS\_MIPMAP  | Optional; should be used for a mipmap.                                                                                                   | 0x400000 |
| DDSCAPS\_TEXTURE | Required                                                                                                                                 | 0x1000   |



 

> [!Note]  
> When you write .dds files, you should set the DDSCAPS\_TEXTURE flag, and for multiple surfaces you should also set the DDSCAPS\_COMPLEX flag. However, when you read a .dds file, you should not rely on the DDSCAPS\_TEXTURE and DDSCAPS\_COMPLEX flags being set because some writers of such a file might not set these flags.

 

The DDS\_SURFACE\_FLAGS\_MIPMAP flag, which is defined in Dds.h, is a bitwise-OR combination of the DDSCAPS\_COMPLEX and DDSCAPS\_MIPMAP flags.

The DDS\_SURFACE\_FLAGS\_TEXTURE flag, which is defined in Dds.h, is equal to the DDSCAPS\_TEXTURE flag.

The DDS\_SURFACE\_FLAGS\_CUBEMAP flag, which is defined in Dds.h, is equal to the DDSCAPS\_COMPLEX flag.

</dd> <dt>

**dwCaps2**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Additional detail about the surfaces stored.



| Flag                         | Description                                            | Value    |
|------------------------------|--------------------------------------------------------|----------|
| DDSCAPS2\_CUBEMAP            | Required for a cube map.                               | 0x200    |
| DDSCAPS2\_CUBEMAP\_POSITIVEX | Required when these surfaces are stored in a cube map. | 0x400    |
| DDSCAPS2\_CUBEMAP\_NEGATIVEX | Required when these surfaces are stored in a cube map. | 0x800    |
| DDSCAPS2\_CUBEMAP\_POSITIVEY | Required when these surfaces are stored in a cube map. | 0x1000   |
| DDSCAPS2\_CUBEMAP\_NEGATIVEY | Required when these surfaces are stored in a cube map. | 0x2000   |
| DDSCAPS2\_CUBEMAP\_POSITIVEZ | Required when these surfaces are stored in a cube map. | 0x4000   |
| DDSCAPS2\_CUBEMAP\_NEGATIVEZ | Required when these surfaces are stored in a cube map. | 0x8000   |
| DDSCAPS2\_VOLUME             | Required for a volume texture.                         | 0x200000 |



 

The DDS\_CUBEMAP\_POSITIVEX flag, which is defined in Dds.h, is a bitwise-OR combination of the DDSCAPS2\_CUBEMAP and DDSCAPS2\_CUBEMAP\_POSITIVEX flags.

The DDS\_CUBEMAP\_NEGATIVEX flag, which is defined in Dds.h, is a bitwise-OR combination of the DDSCAPS2\_CUBEMAP and DDSCAPS2\_CUBEMAP\_NEGATIVEX flags.

The DDS\_CUBEMAP\_POSITIVEY flag, which is defined in Dds.h, is a bitwise-OR combination of the DDSCAPS2\_CUBEMAP and DDSCAPS2\_CUBEMAP\_POSITIVEY flags.

The DDS\_CUBEMAP\_NEGATIVEY flag, which is defined in Dds.h, is a bitwise-OR combination of the DDSCAPS2\_CUBEMAP and DDSCAPS2\_CUBEMAP\_NEGATIVEY flags.

The DDS\_CUBEMAP\_POSITIVEZ flag, which is defined in Dds.h, is a bitwise-OR combination of the DDSCAPS2\_CUBEMAP and DDSCAPS2\_CUBEMAP\_POSITIVEZ flags.

The DDS\_CUBEMAP\_NEGATIVEZ flag, which is defined in Dds.h, is a bitwise-OR combination of the DDSCAPS2\_CUBEMAP and DDSCAPS2\_CUBEMAP\_NEGATIVEZ flags.

The DDS\_CUBEMAP\_ALLFACES flag, which is defined in Dds.h, is a bitwise-OR combination of the DDS\_CUBEMAP\_POSITIVEX, DDS\_CUBEMAP\_NEGATIVEX, DDS\_CUBEMAP\_POSITIVEY, DDS\_CUBEMAP\_NEGATIVEY, DDS\_CUBEMAP\_POSITIVEZ, and DDSCAPS2\_CUBEMAP\_NEGATIVEZ flags.

The DDS\_FLAGS\_VOLUME flag, which is defined in Dds.h, is equal to the DDSCAPS2\_VOLUME flag.

> [!Note]  
> Although Direct3D 9 supports partial cube-maps, Direct3D 10, 10.1, and 11 require that you define all six cube-map faces (that is, you must set DDS\_CUBEMAP\_ALLFACES).

 

</dd> <dt>

**dwCaps3**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Unused.

</dd> <dt>

**dwCaps4**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Unused.

</dd> <dt>

**dwReserved2**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Unused.

</dd> </dl>

## Remarks

Include flags in **dwFlags** for the members of the structure that contain valid data.

Use this structure in combination with a [**DDS\_HEADER\_DXT10**](dds-header-dxt10.md) to store a resource array in a DDS file. For more information, see [texture arrays](dx-graphics-dds-pguide.md).

**DDS\_HEADER** is identical to the DirectDraw DDSURFACEDESC2 structure without DirectDraw dependencies.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dds.h</dt> </dl> |



## See also

<dl> <dt>

[Reference for DDS](dx-graphics-dds-reference.md)
</dt> </dl>

 

