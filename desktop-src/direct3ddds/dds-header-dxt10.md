---
title: DDS\_HEADER\_DXT10 structure
description: DDS header extension to handle resource arrays, DXGI pixel formats that don't map to the legacy Microsoft DirectDraw pixel format structures, and additional metadata.
ms.assetid: '502d6943-8f25-446c-b990-8276f862c195'
keywords: ["DDS_HEADER_DXT10 structure DDS"]
topic_type:
- apiref
api_name:
- DDS_HEADER_DXT10
api_location:
- Dds.h
api_type:
- HeaderDef
---

# DDS\_HEADER\_DXT10 structure

DDS header extension to handle resource arrays, DXGI pixel formats that don't map to the legacy Microsoft DirectDraw pixel format structures, and additional metadata.

## Syntax


```C++
typedef struct {
  DXGI_FORMAT              dxgiFormat;
  D3D10_RESOURCE_DIMENSION resourceDimension;
  UINT                     miscFlag;
  UINT                     arraySize;
  UINT                     miscFlags2;
} DDS_HEADER_DXT10;
```



## Members

<dl> <dt>

**dxgiFormat**
</dt> <dd>

Type: **[**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059)**

</dd> <dd>

The surface pixel format (see [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059)).

</dd> <dt>

**resourceDimension**
</dt> <dd>

Type: **[**D3D10\_RESOURCE\_DIMENSION**](https://msdn.microsoft.com/library/windows/desktop/bb172411)**

</dd> <dd>

Identifies the type of resource. The following values for this member are a subset of the values in the [**D3D10\_RESOURCE\_DIMENSION**](https://msdn.microsoft.com/library/windows/desktop/bb172411) or [**D3D11\_RESOURCE\_DIMENSION**](https://msdn.microsoft.com/library/windows/desktop/ff476202) enumeration:



| Type                                                              | Description                                                                                                                                                                                                                                                                                                                                                            | Value |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| DDS\_DIMENSION\_TEXTURE1D (D3D10\_RESOURCE\_DIMENSION\_TEXTURE1D) | Resource is a [1D texture](https://msdn.microsoft.com/library/windows/desktop/bb205133). The **dwWidth** member of [**DDS\_HEADER**](dds-header.md) specifies the size of the texture. Typically, you set the **dwHeight** member of **DDS\_HEADER** to 1; you also must set the DDSD\_HEIGHT flag in the **dwFlags** member of **DDS\_HEADER**.                      | 2     |
| DDS\_DIMENSION\_TEXTURE2D (D3D10\_RESOURCE\_DIMENSION\_TEXTURE2D) | Resource is a [2D texture](https://msdn.microsoft.com/library/windows/desktop/bb205133) with an area specified by the **dwWidth** and **dwHeight** members of [**DDS\_HEADER**](dds-header.md). You can also use this type to identify a cube-map texture. For more information about how to identify a cube-map texture, see **miscFlag** and **arraySize** members. | 3     |
| DDS\_DIMENSION\_TEXTURE3D (D3D10\_RESOURCE\_DIMENSION\_TEXTURE3D) | Resource is a [3D texture](https://msdn.microsoft.com/library/windows/desktop/bb205133) with a volume specified by the **dwWidth**, **dwHeight**, and **dwDepth** members of [**DDS\_HEADER**](dds-header.md). You also must set the DDSD\_DEPTH flag in the **dwFlags** member of **DDS\_HEADER**.                                                                   | 4     |



 

</dd> <dt>

**miscFlag**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Identifies other, less common options for resources. The following value for this member is a subset of the values in the [**D3D10\_RESOURCE\_MISC\_FLAG**](https://msdn.microsoft.com/library/windows/desktop/bb172412) or [**D3D11\_RESOURCE\_MISC\_FLAG**](https://msdn.microsoft.com/library/windows/desktop/ff476203) enumeration:



| Type                             | Description                                                                                                  | Value |
|----------------------------------|--------------------------------------------------------------------------------------------------------------|-------|
| DDS\_RESOURCE\_MISC\_TEXTURECUBE | Indicates a [2D texture](https://msdn.microsoft.com/library/windows/desktop/bb205133) is a cube-map texture. | 0x4   |



 

</dd> <dt>

**arraySize**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

The number of elements in the array.

For a [2D texture](https://msdn.microsoft.com/library/windows/desktop/bb205133) that is also a cube-map texture, this number represents the number of cubes. This number is the same as the number in the **NumCubes** member of [**D3D10\_TEXCUBE\_ARRAY\_SRV1**](https://msdn.microsoft.com/library/windows/desktop/bb694536) or [**D3D11\_TEXCUBE\_ARRAY\_SRV**](https://msdn.microsoft.com/library/windows/desktop/ff476250)). In this case, the DDS file contains **arraySize**\*6 2D textures. For more information about this case, see the **miscFlag** description.

For a [3D texture](https://msdn.microsoft.com/library/windows/desktop/bb205133), you must set this number to 1.

</dd> <dt>

**miscFlags2**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Contains additional metadata (formerly was reserved). The lower 3 bits indicate the alpha mode of the associated resource. The upper 29 bits are reserved and are typically 0.



| Type                            | Description                                                                                                                              | Value |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------|
| DDS\_ALPHA\_MODE\_UNKNOWN       | Alpha channel content is unknown. This is the value for legacy files, which typically is assumed to be 'straight' alpha.                 | 0x0   |
| DDS\_ALPHA\_MODE\_STRAIGHT      | Any alpha channel content is presumed to use straight alpha.                                                                             | 0x1   |
| DDS\_ALPHA\_MODE\_PREMULTIPLIED | Any alpha channel content is using premultiplied alpha. The only legacy file formats that indicate this information are 'DX2' and 'DX4'. | 0x2   |
| DDS\_ALPHA\_MODE\_OPAQUE        | Any alpha channel content is all set to fully opaque.                                                                                    | 0x3   |
| DDS\_ALPHA\_MODE\_CUSTOM        | Any alpha channel content is being used as a 4th channel and is not intended to represent transparency (straight or premultiplied).      | 0x4   |



 

> [!Note]  
> The legacy D3DX 10 and [D3DX 11](https://msdn.microsoft.com/library/windows/desktop/ff476162) utility libraries will fail to load any .DDS file with **miscFlags2** not equal to zero.

 

</dd> </dl>

## Remarks

Use this structure together with a [**DDS\_HEADER**](dds-header.md) to store a resource array in a DDS file. For more info, see [texture arrays](dx-graphics-dds-pguide.md#using-texture-arrays-in-direct3d-1011).

This header is present if the **dwFourCC** member of the [**DDS\_PIXELFORMAT**](dds-pixelformat.md) structure is set to 'DX10'.

## Requirements



|                   |                                                                                  |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dds.h</dt> </dl> |



## See also

<dl> <dt>

[Reference for DDS](dx-graphics-dds-reference.md)
</dt> </dl>

 

 





