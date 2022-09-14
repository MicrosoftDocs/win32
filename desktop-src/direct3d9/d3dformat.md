---
description: Defines the various types of surface formats.
ms.assetid: a222e3bb-310c-4019-93ee-6a2da2a46ded
title: D3DFORMAT (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DFORMAT
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DFORMAT

Defines the various types of surface formats.

``` syntax
typedef enum _D3DFORMAT {
    D3DFMT_UNKNOWN              =  0,

    D3DFMT_R8G8B8               = 20,
    D3DFMT_A8R8G8B8             = 21,
    D3DFMT_X8R8G8B8             = 22,
    D3DFMT_R5G6B5               = 23,
    D3DFMT_X1R5G5B5             = 24,
    D3DFMT_A1R5G5B5             = 25,
    D3DFMT_A4R4G4B4             = 26,
    D3DFMT_R3G3B2               = 27,
    D3DFMT_A8                   = 28,
    D3DFMT_A8R3G3B2             = 29,
    D3DFMT_X4R4G4B4             = 30,
    D3DFMT_A2B10G10R10          = 31,
    D3DFMT_A8B8G8R8             = 32,
    D3DFMT_X8B8G8R8             = 33,
    D3DFMT_G16R16               = 34,
    D3DFMT_A2R10G10B10          = 35,
    D3DFMT_A16B16G16R16         = 36,

    D3DFMT_A8P8                 = 40,
    D3DFMT_P8                   = 41,

    D3DFMT_L8                   = 50,
    D3DFMT_A8L8                 = 51,
    D3DFMT_A4L4                 = 52,

    D3DFMT_V8U8                 = 60,
    D3DFMT_L6V5U5               = 61,
    D3DFMT_X8L8V8U8             = 62,
    D3DFMT_Q8W8V8U8             = 63,
    D3DFMT_V16U16               = 64,
    D3DFMT_A2W10V10U10          = 67,

    D3DFMT_UYVY                 = MAKEFOURCC('U', 'Y', 'V', 'Y'),
    D3DFMT_R8G8_B8G8            = MAKEFOURCC('R', 'G', 'B', 'G'),
    D3DFMT_YUY2                 = MAKEFOURCC('Y', 'U', 'Y', '2'),
    D3DFMT_G8R8_G8B8            = MAKEFOURCC('G', 'R', 'G', 'B'),
    D3DFMT_DXT1                 = MAKEFOURCC('D', 'X', 'T', '1'),
    D3DFMT_DXT2                 = MAKEFOURCC('D', 'X', 'T', '2'),
    D3DFMT_DXT3                 = MAKEFOURCC('D', 'X', 'T', '3'),
    D3DFMT_DXT4                 = MAKEFOURCC('D', 'X', 'T', '4'),
    D3DFMT_DXT5                 = MAKEFOURCC('D', 'X', 'T', '5'),

    D3DFMT_D16_LOCKABLE         = 70,
    D3DFMT_D32                  = 71,
    D3DFMT_D15S1                = 73,
    D3DFMT_D24S8                = 75,
    D3DFMT_D24X8                = 77,
    D3DFMT_D24X4S4              = 79,
    D3DFMT_D16                  = 80,

    D3DFMT_D32F_LOCKABLE        = 82,
    D3DFMT_D24FS8               = 83,

#if !defined(D3D_DISABLE_9EX)
    D3DFMT_D32_LOCKABLE         = 84,
    D3DFMT_S8_LOCKABLE          = 85,
#endif // !D3D_DISABLE_9EX

    D3DFMT_L16                  = 81,

    D3DFMT_VERTEXDATA           =100,
    D3DFMT_INDEX16              =101,
    D3DFMT_INDEX32              =102,

    D3DFMT_Q16W16V16U16         =110,

    D3DFMT_MULTI2_ARGB8         = MAKEFOURCC('M','E','T','1'),

    D3DFMT_R16F                 = 111,
    D3DFMT_G16R16F              = 112,
    D3DFMT_A16B16G16R16F        = 113,

    D3DFMT_R32F                 = 114,
    D3DFMT_G32R32F              = 115,
    D3DFMT_A32B32G32R32F        = 116,

    D3DFMT_CxV8U8               = 117,

#if !defined(D3D_DISABLE_9EX)
    D3DFMT_A1                   = 118,
    D3DFMT_A2B10G10R10_XR_BIAS  = 119,
    D3DFMT_BINARYBUFFER         = 199,
#endif // !D3D_DISABLE_9EX

    D3DFMT_FORCE_DWORD          =0x7fffffff
} D3DFORMAT;
```

## Remarks

There are several types of formats:

-   [BackBuffer or Display Formats](#backbuffer-or-display-formats)
-   [Buffer Formats](#buffer-formats)
-   [DXTn Compressed Texture Formats](#dxtn-compressed-texture-formats)
-   [Floating-Point Formats](#floating-point-formats)
-   [FOURCC Formats](#fourcc-formats)
-   [IEEE Formats](#ieee-formats)
-   [Mixed Formats](#mixed-formats)
-   [Signed Formats](#signed-formats)
-   [Unsigned Formats](#unsigned-formats)
-   [Other](#other)

All formats are listed from left to right, most-significant bit to least-significant bit. For example, **D3DFORMAT\_ARGB** is ordered from the most-significant bit channel A (alpha), to the least-significant bit channel B (blue). When traversing surface data, the data is stored in memory from least-significant bit to most-significant bit, which means that the channel order in memory is from least-significant bit (blue) to most-significant bit (alpha).

The default value for formats that contain undefined channels (G16R16, A8, and so on) is 1. The only exception is the A8 format, which is initialized to 000 for the three color channels.

The order of the bits is from the most significant byte first, so D3DFMT\_A8L8 indicates that the high byte of this 2-byte format is alpha. **D3DFMT\_D16** indicates a 16-bit integer value and an application-lockable surface.

Pixel formats have been chosen to enable the expression of hardware-vendor-defined extension formats, as well as to include the well-established FOURCC method. The set of formats understood by the Direct3D runtime is defined by D3DFORMAT.

Note that formats are supplied by independent hardware vendors (IHVs) and many FOURCC codes are not listed. The formats in this enumeration are unique in that they are sanctioned by the runtime, meaning that the reference rasterizer will operate on all these types. IHV-supplied formats will be supported by the individual IHVs on a card-by-card basis.

### BackBuffer or Display Formats

These formats are the only valid formats for a back buffer or a display.



| Format      | Back buffer | Display                   |
|-------------|-------------|---------------------------|
| A2R10G10B10 | x           | x (full-screen mode only) |
| A8R8G8B8    | x           |                           |
| X8R8G8B8    | x           | x                         |
| A1R5G5B5    | x           |                           |
| X1R5G5B5    | x           | x                         |
| R5G6B5      | x           | x                         |



 

### Buffer Formats

Depth, stencil, vertex, and index buffers each have unique formats.



| Buffer flags               | Value | Format                                                                                                                                        |
|----------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **D3DFMT\_D16\_LOCKABLE**  | 70    | 16-bit z-buffer bit depth.                                                                                                                    |
| **D3DFMT\_D32**            | 71    | 32-bit z-buffer bit depth.                                                                                                                    |
| **D3DFMT\_D15S1**          | 73    | 16-bit z-buffer bit depth where 15 bits are reserved for the depth channel and 1 bit is reserved for the stencil channel.                     |
| **D3DFMT\_D24S8**          | 75    | 32-bit z-buffer bit depth using 24 bits for the depth channel and 8 bits for the stencil channel.                                             |
| **D3DFMT\_D24X8**          | 77    | 32-bit z-buffer bit depth using 24 bits for the depth channel.                                                                                |
| **D3DFMT\_D24X4S4**        | 79    | 32-bit z-buffer bit depth using 24 bits for the depth channel and 4 bits for the stencil channel.                                             |
| **D3DFMT\_D32F\_LOCKABLE** | 82    | A lockable format where the depth value is represented as a standard IEEE floating-point number.                                              |
| **D3DFMT\_D24FS8**         | 83    | A non-lockable format that contains 24 bits of depth (in a 24-bit floating point format - 20e4) and 8 bits of stencil.                        |
| **D3DFMT\_D32\_LOCKABLE**  | 84    | A lockable 32-bit depth buffer. **Differences between Direct3D 9 and Direct3D 9Ex:** This flag is available in Direct3D 9Ex only.<br/>  |
| **D3DFMT\_S8\_LOCKABLE**   | 85    | A lockable 8-bit stencil buffer. **Differences between Direct3D 9 and Direct3D 9Ex:** This flag is available in Direct3D 9Ex only.<br/> |
| **D3DFMT\_D16**            | 80    | 16-bit z-buffer bit depth.                                                                                                                    |
| **D3DFMT\_VERTEXDATA**     | 100   | Describes a vertex buffer surface.                                                                                                            |
| **D3DFMT\_INDEX16**        | 101   | 16-bit index buffer bit depth.                                                                                                                |
| **D3DFMT\_INDEX32**        | 102   | 32-bit index buffer bit depth.                                                                                                                |



 

All depth-stencil formats except D3DFMT\_D16\_LOCKABLE indicate no particular bit ordering per pixel, and the driver is allowed to consume more than the indicated number of bits-per-depth channel (but not stencil channel).

### DXTn Compressed Texture Formats

These flags are used for compressed textures:



| DXTn Compressed Texture flags | Value                          | Format                          |
|-------------------------------|--------------------------------|---------------------------------|
| **D3DFMT\_DXT1**              | MAKEFOURCC('D', 'X', 'T', '1') | DXT1 compression texture format |
| **D3DFMT\_DXT2**              | MAKEFOURCC('D', 'X', 'T', '2') | DXT2 compression texture format |
| **D3DFMT\_DXT3**              | MAKEFOURCC('D', 'X', 'T', '3') | DXT3 compression texture format |
| **D3DFMT\_DXT4**              | MAKEFOURCC('D', 'X', 'T', '4') | DXT4 compression texture format |
| **D3DFMT\_DXT5**              | MAKEFOURCC('D', 'X', 'T', '5') | DXT5 compression texture format |



 

The runtime will not allow an application to create a surface using a DXTn format unless the surface dimensions are multiples of 4. This applies to offscreen-plain surfaces, render targets, 2D textures, cube textures, and volume textures.

### Floating-Point Formats

These flags are used for floating-point surface formats. These 16-bits-per-channel formats are also known as s10e5 formats.



| Floating-point flags      | Value | Format                                                                                   |
|---------------------------|-------|------------------------------------------------------------------------------------------|
| **D3DFMT\_R16F**          | 111   | 16-bit float format using 16 bits for the red channel.                                   |
| **D3DFMT\_G16R16F**       | 112   | 32-bit float format using 16 bits for the red channel and 16 bits for the green channel. |
| **D3DFMT\_A16B16G16R16F** | 113   | 64-bit float format using 16 bits for the each channel (alpha, blue, green, red).        |



 

### FOURCC Formats

Data in a FOURCC format is compressed data.

### MAKEFOURCC

A macro for generating four-character codes follows:

``` syntax
#define MAKEFOURCC(ch0, ch1, ch2, ch3)                              \
                ((DWORD)(BYTE)(ch0) | ((DWORD)(BYTE)(ch1) << 8) |   \
                ((DWORD)(BYTE)(ch2) << 16) | ((DWORD)(BYTE)(ch3) << 24 ))
```

Here are the defined FOURCC formats:



| FOURCC flags              | Value                          | Format                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **D3DFMT\_MULTI2\_ARGB8** | MAKEFOURCC('M','E','T','1')    | MultiElement texture (not compressed)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **D3DFMT\_G8R8\_G8B8**    | MAKEFOURCC('G', 'R', 'G', 'B') | A 16-bit packed RGB format analogous to YUY2 (Y0U0, Y1V0, Y2U2, and so on). It requires a pixel pair in order to properly represent the color value. The first pixel in the pair contains 8 bits of green (in the high 8 bits) and 8 bits of red (in the low 8 bits). The second pixel contains 8 bits of green (in the high 8 bits) and 8 bits of blue (in the low 8 bits). Together, the two pixels share the red and blue components, while each has a unique green component (G0R0, G1B0, G2R2, and so on). The texture sampler does not normalize the colors when looking up into a pixel shader; they remain in the range of 0.0f to 255.0f. This is true for all programmable pixel shader models. For the fixed function pixel shader, the hardware should normalize to the 0.f to 1.f range and essentially treat it as the YUY2 texture. Hardware that exposes this format must have the PixelShader1xMaxValue member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) set to a value capable of handling that range. |
| **D3DFMT\_R8G8\_B8G8**    | MAKEFOURCC('R', 'G', 'B', 'G') | A 16-bit packed RGB format analogous to UYVY (U0Y0, V0Y1, U2Y2, and so on). It requires a pixel pair in order to properly represent the color value. The first pixel in the pair contains 8 bits of green (in the low 8 bits) and 8 bits of red (in the high 8 bits). The second pixel contains 8 bits of green (in the low 8 bits) and 8 bits of blue (in the high 8 bits). Together, the two pixels share the red and blue components, while each has a unique green component (R0G0, B0G1, R2G2, and so on). The texture sampler does not normalize the colors when looking up into a pixel shader; they remain in the range of 0.0f to 255.0f. This is true for all programmable pixel shader models. For the fixed function pixel shader, the hardware should normalize to the 0.f to 1.f range and essentially treat it as the YUY2 texture. Hardware that exposes this format must have PixelShader1xMaxValue member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) set to a value capable of handling that range.     |
| **D3DFMT\_UYVY**          | MAKEFOURCC('U', 'Y', 'V', 'Y') | UYVY format (PC98 compliance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **D3DFMT\_YUY2**          | MAKEFOURCC('Y', 'U', 'Y', '2') | YUY2 format (PC98 compliance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |



 

### IEEE Formats

These flags are used for floating-point surface formats. These 32-bits-per-channel formats are also known as s23e8 formats.



| Floating-point flags      | Value | Format                                                                                   |
|---------------------------|-------|------------------------------------------------------------------------------------------|
| **D3DFMT\_R32F**          | 114   | 32-bit float format using 32 bits for the red channel.                                   |
| **D3DFMT\_G32R32F**       | 115   | 64-bit float format using 32 bits for the red channel and 32 bits for the green channel. |
| **D3DFMT\_A32B32G32R32F** | 116   | 128-bit float format using 32 bits for the each channel (alpha, blue, green, red).       |



 

### Mixed Formats

Data in mixed formats can contain a combination of unsigned data and signed data.



| Mixed format flags      | Value | Format                                                                                         |
|-------------------------|-------|------------------------------------------------------------------------------------------------|
| **D3DFMT\_L6V5U5**      | 61    | 16-bit bump-map format with luminance using 6 bits for luminance, and 5 bits each for v and u. |
| **D3DFMT\_X8L8V8U8**    | 62    | 32-bit bump-map format with luminance using 8 bits for each channel.                           |
| **D3DFMT\_A2W10V10U10** | 67    | 32-bit bump-map format using 2 bits for alpha and 10 bits each for w, v, and u.                |



 

### Signed Formats

Data in a signed format can be both positive and negative. Signed formats use combinations of (U), (V), (W), and (Q) data.



| Signed format flags      | Value | Format                                                                                                    |
|--------------------------|-------|-----------------------------------------------------------------------------------------------------------|
| **D3DFMT\_V8U8**         | 60    | 16-bit bump-map format using 8 bits each for u and v data.                                                |
| **D3DFMT\_Q8W8V8U8**     | 63    | 32-bit bump-map format using 8 bits for each channel.                                                     |
| **D3DFMT\_V16U16**       | 64    | 32-bit bump-map format using 16 bits for each channel.                                                    |
| **D3DFMT\_Q16W16V16U16** | 110   | 64-bit bump-map format using 16 bits for each component.                                                  |
| **D3DFMT\_CxV8U8**       | 117   | 16-bit normal compression format. The texture sampler computes the C channel from: C = sqrt(1 - U² - V²). |



 

### Unsigned Formats

Data in an unsigned format must be positive. Unsigned formats use combinations of (R)ed, (G)reen, (B)lue, (A)lpha, (L)uminance, and (P)alette data. Palette data is also referred to as color indexed data because the data is used to index a color palette.



| Unsigned format flags             | Value | Format                                                                                                                                                                    |
|-----------------------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **D3DFMT\_R8G8B8**                | 20    | 24-bit RGB pixel format with 8 bits per channel.                                                                                                                          |
| **D3DFMT\_A8R8G8B8**              | 21    | 32-bit ARGB pixel format with alpha, using 8 bits per channel.                                                                                                            |
| **D3DFMT\_X8R8G8B8**              | 22    | 32-bit RGB pixel format, where 8 bits are reserved for each color.                                                                                                        |
| **D3DFMT\_R5G6B5**                | 23    | 16-bit RGB pixel format with 5 bits for red, 6 bits for green, and 5 bits for blue.                                                                                       |
| **D3DFMT\_X1R5G5B5**              | 24    | 16-bit pixel format where 5 bits are reserved for each color.                                                                                                             |
| **D3DFMT\_A1R5G5B5**              | 25    | 16-bit pixel format where 5 bits are reserved for each color and 1 bit is reserved for alpha.                                                                             |
| **D3DFMT\_A4R4G4B4**              | 26    | 16-bit ARGB pixel format with 4 bits for each channel.                                                                                                                    |
| **D3DFMT\_R3G3B2**                | 27    | 8-bit RGB texture format using 3 bits for red, 3 bits for green, and 2 bits for blue.                                                                                     |
| **D3DFMT\_A8**                    | 28    | 8-bit alpha only.                                                                                                                                                         |
| **D3DFMT\_A8R3G3B2**              | 29    | 16-bit ARGB texture format using 8 bits for alpha, 3 bits each for red and green, and 2 bits for blue.                                                                    |
| **D3DFMT\_X4R4G4B4**              | 30    | 16-bit RGB pixel format using 4 bits for each color.                                                                                                                      |
| **D3DFMT\_A2B10G10R10**           | 31    | 32-bit pixel format using 10 bits for each color and 2 bits for alpha.                                                                                                    |
| **D3DFMT\_A8B8G8R8**              | 32    | 32-bit ARGB pixel format with alpha, using 8 bits per channel.                                                                                                            |
| **D3DFMT\_X8B8G8R8**              | 33    | 32-bit RGB pixel format, where 8 bits are reserved for each color.                                                                                                        |
| **D3DFMT\_G16R16**                | 34    | 32-bit pixel format using 16 bits each for green and red.                                                                                                                 |
| **D3DFMT\_A2R10G10B10**           | 35    | 32-bit pixel format using 10 bits each for red, green, and blue, and 2 bits for alpha.                                                                                    |
| **D3DFMT\_A16B16G16R16**          | 36    | 64-bit pixel format using 16 bits for each component.                                                                                                                     |
| **D3DFMT\_A8P8**                  | 40    | 8-bit color indexed with 8 bits of alpha.                                                                                                                                 |
| **D3DFMT\_P8**                    | 41    | 8-bit color indexed.                                                                                                                                                      |
| **D3DFMT\_L8**                    | 50    | 8-bit luminance only.                                                                                                                                                     |
| **D3DFMT\_L16**                   | 81    | 16-bit luminance only.                                                                                                                                                    |
| **D3DFMT\_A8L8**                  | 51    | 16-bit using 8 bits each for alpha and luminance.                                                                                                                         |
| **D3DFMT\_A4L4**                  | 52    | 8-bit using 4 bits each for alpha and luminance.                                                                                                                          |
| **D3DFMT\_A1**                    | 118   | 1-bit monochrome. **Differences between Direct3D 9 and Direct3D 9Ex:** This flag is available in Direct3D 9Ex only.<br/>                                            |
| **D3DFMT\_A2B10G10R10\_XR\_BIAS** | 119   | 2.8-biased fixed point. **Differences between Direct3D 9 and Direct3D 9Ex:** This flag is available in Direct3D 9Ex only.<br/>                                      |
| **D3DFMT\_BINARYBUFFER**          | 199   | Binary format indicating that the data has no inherent type. **Differences between Direct3D 9 and Direct3D 9Ex:** This flag is available in Direct3D 9Ex only.<br/> |



 

### Other

This flag is used for undefined formats.



| Other flags         | Value | Format                    |
|---------------------|-------|---------------------------|
| **D3DFMT\_UNKNOWN** | 0     | Surface format is unknown |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> </dl>

 

 




