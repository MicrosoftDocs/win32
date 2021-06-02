---
title: DDS_PIXELFORMAT structure (Dds.h)
description: Surface pixel format.
ms.assetid: 39c5e48d-cf20-4d77-80d5-a67f04de4883
keywords:
- DDS_PIXELFORMAT structure DDS
topic_type:
- apiref
api_name:
- DDS_PIXELFORMAT
api_location:
- Dds.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DDS\_PIXELFORMAT structure

Surface pixel format.

## Syntax


```C++
struct DDS_PIXELFORMAT {
  DWORD dwSize;
  DWORD dwFlags;
  DWORD dwFourCC;
  DWORD dwRGBBitCount;
  DWORD dwRBitMask;
  DWORD dwGBitMask;
  DWORD dwBBitMask;
  DWORD dwABitMask;
};
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Structure size; set to 32 (bytes).

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Values which indicate what type of data is in the surface.



| Flag              | Description                                                                                                                                                                                                                                | Value   |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| DDPF\_ALPHAPIXELS | Texture contains alpha data; **dwRGBAlphaBitMask** contains valid data.                                                                                                                                                                    | 0x1     |
| DDPF\_ALPHA       | Used in some older DDS files for alpha channel only uncompressed data (dwRGBBitCount contains the alpha channel bitcount; dwABitMask contains valid data)                                                                                  | 0x2     |
| DDPF\_FOURCC      | Texture contains compressed RGB data; **dwFourCC** contains valid data.                                                                                                                                                                    | 0x4     |
| DDPF\_RGB         | Texture contains uncompressed RGB data; **dwRGBBitCount** and the RGB masks (**dwRBitMask**, **dwGBitMask**, **dwBBitMask**) contain valid data.                                                                                           | 0x40    |
| DDPF\_YUV         | Used in some older DDS files for YUV uncompressed data (dwRGBBitCount contains the YUV bit count; dwRBitMask contains the Y mask, dwGBitMask contains the U mask, dwBBitMask contains the V mask)                                          | 0x200   |
| DDPF\_LUMINANCE   | Used in some older DDS files for single channel color uncompressed data (dwRGBBitCount contains the luminance channel bit count; dwRBitMask contains the channel mask). Can be combined with DDPF\_ALPHAPIXELS for a two channel DDS file. | 0x20000 |



 

</dd> <dt>

**dwFourCC**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Four-character codes for specifying compressed or custom formats. Possible values include: *DXT1*, *DXT2*, *DXT3*, *DXT4*, or *DXT5*. A FourCC of DX10 indicates the prescense of the [**DDS\_HEADER\_DXT10**](dds-header-dxt10.md) extended header, and the dxgiFormat member of that structure indicates the true format. When using a four-character code, dwFlags must include *DDPF\_FOURCC*.

</dd> <dt>

**dwRGBBitCount**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Number of bits in an RGB (possibly including alpha) format. Valid when **dwFlags** includes *DDPF\_RGB*, *DDPF\_LUMINANCE*, or *DDPF\_YUV*.

</dd> <dt>

**dwRBitMask**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Red (or lumiannce or Y) mask for reading color data. For instance, given the A8R8G8B8 format, the red mask would be 0x00ff0000.

</dd> <dt>

**dwGBitMask**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Green (or U) mask for reading color data. For instance, given the A8R8G8B8 format, the green mask would be 0x0000ff00.

</dd> <dt>

**dwBBitMask**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Blue (or V) mask for reading color data. For instance, given the A8R8G8B8 format, the blue mask would be 0x000000ff.

</dd> <dt>

**dwABitMask**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Alpha mask for reading alpha data. dwFlags must include *DDPF\_ALPHAPIXELS* or *DDPF\_ALPHA*. For instance, given the A8R8G8B8 format, the alpha mask would be 0xff000000.

</dd> </dl>

## Remarks

To store DXGI formats such as floating-point data, use a **dwFlags** of DDPF\_FOURCC and set **dwFourCC** to 'D','X','1','0'. Use the [**DDS\_HEADER\_DXT10**](dds-header-dxt10.md) extension header to store the DXGI format in the **dxgiFormat** member.

Note that there are non-standard variants of DDS files where **dwFlags** has DDPF\_FOURCC and the **dwFourCC** value is set directly to a D3DFORMAT or DXGI\_FORMAT enumeration value. It is not possible to disambiguate the D3DFORMAT versus DXGI\_FORMAT values using this non-standard scheme, so the DX10 extension header is recommended instead.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dds.h</dt> </dl> |



## See also

<dl> <dt>

[Reference for DDS](dx-graphics-dds-reference.md)
</dt> </dl>

 

