---
title: Texture Block Compression in Direct3D 11
description: Block Compression (BC) support for textures has been extended in Direct3D 11 to include the BC6H and BC7 algorithms.
ms.assetid: E0735D4E-9C0F-45DC-854A-C27EB8367D86
ms.topic: article
ms.date: 05/31/2018
---

# Texture Block Compression in Direct3D 11

Block Compression (BC) support for textures has been extended in Direct3D 11 to include the BC6H and BC7 algorithms. BC6H supports high-dynamic range color source data, and BC7 provides better-than-average quality compression with less artifacts for standard RGB source data.

For more specific information about block compression algorithm support prior to Direct3D 11, including support for the BC1 through BC5 formats, see [Block Compression (Direct3D 10)](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-resources-block-compression).

**Note about File Formats:** The BC6H and BC7 texture compression formats use the DDS file format for storing the compressed texture data. For more information, see the [Programming Guide for DDS](/windows/desktop/direct3ddds/dx-graphics-dds-pguide) for details.

## Block Compression Formats Supported in Direct3D 11



| Source data                                  | Minimum required data compression resolution                              | Recommended format | Minimum supported feature level |
|----------------------------------------------|---------------------------------------------------------------------------|--------------------|---------------------------------|
| Three-channel color with alpha channel       | Three color channels (5 bits:6 bits:5 bits), with 0 or 1 bit(s) of alpha  | BC1                | Direct3D 9.1                    |
| Three-channel color with alpha channel       | Three color channels (5 bits:6 bits:5 bits), with 4 bits of alpha         | BC2                | Direct3D 9.1                    |
| Three-channel color with alpha channel       | Three color channels (5 bits:6 bits:5 bits) with 8 bits of alpha          | BC3                | Direct3D 9.1                    |
| One-channel color                            | One color channel (8 bits)                                                | BC4                | Direct3D 10                     |
| Two-channel color                            | Two color channels (8 bits:8 bits)                                        | BC5                | Direct3D 10                     |
| Three-channel high dynamic range (HDR) color | Three color channels (16 bits:16 bits:16 bits) in "half" floating point\* | BC6H               | Direct3D 11                     |
| Three-channel color, alpha channel optional  | Three color channels (4 to 7 bits per channel) with 0 to 8 bits of alpha  | BC7                | Direct3D 11                     |



 

\*"Half" floating point is a 16 bit value that consists of an optional sign bit, a 5 bit biased exponent, and a 10 or 11 bit mantissa.

## BC1, BC2, and B3 Formats

The BC1, BC2, and BC3 formats are equivalent to the Direct3D 9 DXTn texture compression formats, and are the same as the corresponding Direct3D 10 BC1, BC2, and BC3 formats. Support for these three formats is required by all feature levels (D3D\_FEATURE\_LEVEL\_9\_1, D3D\_FEATURE\_LEVEL\_9\_2, D3D\_FEATURE\_LEVEL\_9\_3, D3D\_FEATURE\_LEVEL\_10\_0, D3D\_FEATURE\_LEVEL\_10\_1, and D3D\_FEATURE\_LEVEL\_11\_0).



| Block compression format | DXGI format                                                                           | Direct3D 9 equivalent format                               | Bytes per 4x4 pixel block |
|--------------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------|---------------------------|
| BC1                      | DXGI\_FORMAT\_BC1\_UNORM, DXGI\_FORMAT\_BC1\_UNORM\_SRGB, DXGI\_FORMAT\_BC1\_TYPELESS | D3DFMT\_DXT1, FourCC="DXT1"                                | 8                         |
| BC2                      | DXGI\_FORMAT\_BC2\_UNORM, DXGI\_FORMAT\_BC2\_UNORM\_SRGB, DXGI\_FORMAT\_BC2\_TYPELESS | D3DFMT\_DXT2\*, FourCC="DXT2", D3DFMT\_DXT3, FourCC="DXT3" | 16                        |
| BC3                      | DXGI\_FORMAT\_BC3\_UNORM, DXGI\_FORMAT\_BC3\_UNORM\_SRGB, DXGI\_FORMAT\_BC3\_TYPELESS | D3DFMT\_DXT4\*, FourCC="DXT4", D3DFMT\_DXT5, FourCC="DXT5" | 16                        |



 

\*These compression schemes (DXT2 and DXT4) make no distinction between the Direct3D 9 pre-multiplied alpha formats and the standard alpha formats. This distinction must be handled by the programmable shaders at render time.

## BC4 and BC5 Formats



| Block compression format | DXGI format                                                                     | Direct3D 9 equivalent format | Bytes per 4x4 pixel block |
|--------------------------|---------------------------------------------------------------------------------|------------------------------|---------------------------|
| BC4                      | DXGI\_FORMAT\_BC4\_UNORM, DXGI\_FORMAT\_BC4\_SNORM, DXGI\_FORMAT\_BC4\_TYPELESS | FourCC="ATI1"                | 8                         |
| BC5                      | DXGI\_FORMAT\_BC5\_UNORM, DXGI\_FORMAT\_BC5\_SNORM, DXGI\_FORMAT\_BC5\_TYPELESS | FourCC="ATI2"                | 16                        |



 

## BC6H Format

For more detailed information about this format, see the [BC6H Format](bc6h-format.md) documentation.



| Block compression format | DXGI format                                                                      | Direct3D 9 equivalent format | Bytes per 4x4 pixel block |
|--------------------------|----------------------------------------------------------------------------------|------------------------------|---------------------------|
| BC6H                     | DXGI\_FORMAT\_BC6H\_UF16, DXGI\_FORMAT\_BC6H\_SF16, DXGI\_FORMAT\_BC6H\_TYPELESS | N/A                          | 16                        |



 

The BC6H format can select different encoding modes for each 4x4 pixel block. A total of 14 different encoding modes are available, each with slightly different trade-offs in the resulting visual quality of the displayed texture. The choice of modes allows for fast decoding by the hardware with the quality level selected or adapted according to the source content, but it also greatly increases the complexity of the search space.

## BC7 Format

For more detailed information about this format, see the [BC7 Format](bc7-format.md) documentation.



| Block compression format | DXGI format                                                                           | Direct3D 9 equivalent format | Bytes per 4x4 pixel block |
|--------------------------|---------------------------------------------------------------------------------------|------------------------------|---------------------------|
| BC7                      | DXGI\_FORMAT\_BC7\_UNORM, DXGI\_FORMAT\_BC7\_UNORM\_SRGB, DXGI\_FORMAT\_BC7\_TYPELESS | N/A                          | 16                        |



 

The BC7 format can select different encoding modes for each 4x4 pixel block. A total of 8 different encoding modes are available, each with slightly different trade-offs in the resulting visual quality of the displayed texture. The choice of modes allows for fast decoding by the hardware with the quality level selected or adapted according to the source content, but it also greatly increases the complexity of the search space.

## In this section



| Topic                                                                 | Description                                                                                                                          |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [BC6H Format](bc6h-format.md)<br/>                             | The BC6H format is a texture compression format designed to support high-dynamic range (HDR) color spaces in source data.<br/> |
| [BC7 Format](bc7-format.md)<br/>                               | The BC7 format is a texture compression format used for high-quality compression of RGB and RGBA data.<br/>                    |
| [BC7 Format Mode Reference](bc7-format-mode-reference.md)<br/> | This documentation contains a list of the 8 block modes and bit allocations for BC7 texture compression format blocks.<br/>    |



 

## Related topics

<dl> <dt>

[Block Compression (Direct3D 10)](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-resources-block-compression)
</dt> <dt>

[Textures](overviews-direct3d-11-resources-textures.md)
</dt> </dl>

 

