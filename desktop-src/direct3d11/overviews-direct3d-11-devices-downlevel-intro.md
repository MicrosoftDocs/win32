---
title: Direct3D feature levels
description: This topic discusses Direct3D feature levels.
ms.assetid: 5ad0525c-249f-452d-950b-df8fa2addde2
keywords:
- DX feature level
- DirectX feature level
- feature level, DX
- feature level, DirectX
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D feature levels

To handle the diversity of video cards in new and existing machines, Microsoft Direct3D 11 introduces the concept of feature levels. This topic discusses Direct3D feature levels.

Each video card implements a certain level of Microsoft DirectX (DX) functionality depending on the graphics processing units (GPUs) installed. In prior versions of Microsoft Direct3D, you could find out the version of Direct3D the video card implemented, and then program your application accordingly.

-   [Numbering Systems](#numbering-systems)
-   [Overview For Each Feature Level](#overview-for-each-feature-level)
-   [Related topics](#related-topics)

With Direct3D 11, a new paradigm is introduced called feature levels. A feature level is a well defined set of GPU functionality. For instance, the 9\_1 feature level implements the functionality that was implemented in Microsoft Direct3D 9, which exposes the capabilities of shader models [ps\_2\_x](../direct3dhlsl/dx9-graphics-reference-asm-ps-2-x.md) and [vs\_2\_x](../direct3dhlsl/dx9-graphics-reference-asm-vs-2-x.md), while the 11\_0 feature level implements the functionality that was implemented in Direct3D 11.

Now when you create a device, you can attempt to create a device for the feature level that you want to request. If the device creation works, that feature level exists, if not, the hardware does not support that feature level. You can either try to recreate a device at a lower feature level or you can choose to exit the application. For more info about creating a device, see the [**D3D11CreateDevice**](/windows/win32/api/D3D11/nf-d3d11-d3d11createdevice) function.

Using feature levels, you can develop an application for Direct3D 9, Microsoft Direct3D 10, or Direct3D 11, and then run it on 9, 10 or 11 hardware (with some exceptions; for example, new 11 features will not run on an existing 9 card). Here is a couple of other basic properties of feature levels:

-   A GPU that allows a device to be created meets or exceeds the functionality of that feature level.
-   A feature level always includes the functionality of previous or lower feature levels.
-   A feature level does not imply performance, only functionality. Performance is dependent on hardware implementation.
-   Choose a feature level when you create a Direct3D 11 device.

For information about limitations creating nonhardware-type devices on certain feature levels, see [Limitations Creating WARP and Reference Devices](overviews-direct3d-11-devices-limitations.md).

To assist you in deciding what feature level to design with, compare the features for each feature level.

The [10Level9 Reference](d3d11-graphics-reference-10level9.md) section lists the differences between how various [**ID3D11Device**](/windows/win32/api/D3D11/nn-d3d11-id3d11device) and [**ID3D11DeviceContext**](/windows/win32/api/D3D11/nn-d3d11-id3d11devicecontext) methods behave at various 10Level9 feature levels.

## Numbering Systems

There are three distinct numbering systems, for Direct3D versions, shader models, and feature levels:

-   Direct3D versions use a period; for example, Direct3D 12.0.
-   Shader models use a period; for example, shader model 5.1.
-   Feature levels use an underscore; for example, feature level 12\_0.

## Overview For Each Feature Level

The following features are available for each Direct3D feature level.

The headings across the top row are Direct3D feature levels. The headings in the left-hand column are features.



| Feature \\ Feature Level                                                                                                 | 12\_1⁰                    | 12\_0⁰                    | 11\_1¹                   | 11\_0                    | 10\_1     | 10\_0     | 9\_3                                           | 9\_2                    | 9\_1                    |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------|--------------------------|--------------------------|-----------|-----------|------------------------------------------------|-------------------------|-------------------------|
| Shader Model (D3D11)                                                                                                       | 5.0²                      | 5.0²                      | 5.0²                     | 5.0²                     | 4.x       | 4.0       | 2.0 (4\_0\_level\_9\_3) \[vs\_2\_a/ps\_2\_x\]⁵ | 2.0 (4\_0\_level\_9\_1) | 2.0 (4\_0\_level\_9\_1) |
| Shader Model (D3D12)                                                                                                       | 5.1²                      | 5.1²                      | 5.1²                    | 5.1²                    | N/A       | N/A       | N/A  | N/A | N/A |
| [Tiled resources](tiled-resources.md)                                                                                   | Tier2⁶                    | Tier2⁶                    | Optional                 | Optional                 | No        | No        | No                                             | No                      | No                      |
| [Conservative Rasterization](conservative-rasterization.md)                                                             | Tier1⁶                    | Optional                  | Optional                 | No                       | No        | No        | No                                             | No                      | No                      |
| [Rasterizer Order Views](rasterizer-order-views.md)                                                                     | Yes                       | Optional                  | Optional                 | No                       | No        | No        | No                                             | No                      | No                      |
| [Min/Max Filters](/windows/win32/api/D3D11/ne-d3d11-d3d11_filter)                                                                                      | Yes                       | Yes                       | Optional                 | No                       | No        | No        | No                                             | No                      | No                      |
| Map Default Buffer                                                                                                       | Optional                  | Optional                  | Optional                 | Optional                 | No        | No        | No                                             | No                      | No                      |
| [Shader Specified Stencil Reference Value](shader-specified-stencil-reference-value.md)                                 | Optional                  | Optional                  | Optional                 | No                       | No        | No        | No                                             | No                      | No                      |
| Typed Unordered Access View Loads                                                                                        | 18 formats, more optional | 18 formats, more optional | 3 formats, more optional | 3 formats, more optional | No        | No        | No                                             | No                      | No                      |
| [Geometry Shader](/previous-versions/bb205146(v=vs.85)) | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | No                                             | No                      | No                      |
| [Stream Out](./d3d10-graphics-programming-guide-output-stream-stage.md)                                            | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | No                                             | No                      | No                      |
| [DirectCompute / Compute Shader](direct3d-11-advanced-stages-compute-shader.md)                                         | Yes                       | Yes                       | Yes                      | Yes                      | Optional  | Optional  | N/A                                            | N/A                     | N/A                     |
| [Hull and Domain Shaders](direct3d-11-advanced-stages-tessellation.md)                                                  | Yes                       | Yes                       | Yes                      | Yes                      | No        | No        | No                                             | No                      | No                      |
| [Texture Resource Arrays](overviews-direct3d-11-resources-textures-intro.md)                                            | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | No                                             | No                      | No                      |
| [Cubemap Resource Arrays](overviews-direct3d-11-resources-textures-intro.md)                                            | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | No        | No                                             | No                      | No                      |
| [BC4/BC5 Compression](../direct3d10/d3d10-graphics-programming-guide-resources-block-compression.md)                           | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | No                                             | No                      | No                      |
| [BC6H/BC7 Compression](texture-block-compression-in-direct3d-11.md)                                                     | Yes                       | Yes                       | Yes                      | Yes                      | No        | No        | No                                             | No                      | No                      |
| [Alpha-to-coverage](./d3d10-graphics-programming-guide-blend-state.md)         | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | No                                             | No                      | No                      |
| [Extended Formats (BGRA, and so on)](overviews-direct3d-11-devices-downlevel-exceptions.md)            | Yes                       | Yes                       | Yes                      | Yes                      | Optional  | Optional  | Yes                                            | Yes                     | Yes                     |
| [10-bit XR High Color Format](overviews-direct3d-11-devices-downlevel-exceptions.md)                   | Yes                       | Yes                       | Yes                      | Yes                      | Optional  | Optional  | N/A                                            | N/A                     | N/A                     |
| [Logic Operations (Output Merger)](/windows/win32/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options)                                                 | Yes                       | Yes                       | Yes                      | Optional¹                | Optional¹ | Optional¹ | No                                             | No                      | No                      |
| Target-independent rasterization                                                                                         | Yes                       | Yes                       | Yes                      | No                       | No        | No        | No                                             | No                      | No                      |
| [Multiple render target(MRT) with ForcedSampleCount 1](/windows/win32/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options)                             | Yes                       | Yes                       | Yes                      | Optional¹                | Optional¹ | Optional¹ | No                                             | No                      | No                      |
| UAV slots                                                                                                                | 64                        | 64                        | 64                       | 8                        | 1         | 1         | N/A                                            | N/A                     | N/A                     |
| UAVs at every stage                                                                                                      | Yes                       | Yes                       | Yes                      | No                       | No        | No        | N/A                                            | N/A                     | N/A                     |
| [Max forced sample count for UAV-only rendering](/windows/win32/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options)                                   | 16                        | 16                        | 16                       | 8                        | N/A       | N/A       | N/A                                            | N/A                     | N/A                     |
| Constant buffer offsetting and partial updates                                                                           | Yes                       | Yes                       | Yes                      | Optional¹                | Optional¹ | Optional¹ | Yes¹                                           | Yes¹                    | Yes¹                    |
| 16 bits per pixel (bpp) formats                                                                                          | Yes                       | Yes                       | Yes                      | Optional¹                | Optional¹ | Optional¹ | Optional¹                                      | Optional¹               | Optional¹               |
| Max Texture Dimension                                                                                                    | 16384                     | 16384                     | 16384                    | 16384                    | 8192      | 8192      | 4096                                           | 2048                    | 2048                    |
| Max Cubemap Dimension                                                                                                    | 16384                     | 16384                     | 16384                    | 16384                    | 8192      | 8192      | 4096                                           | 512                     | 512                     |
| Max Volume Extent                                                                                                        | 2048                      | 2048                      | 2048                     | 2048                     | 2048      | 2048      | 256                                            | 256                     | 256                     |
| Max Texture Repeat                                                                                                       | 16384                     | 16384                     | 16384                    | 16384                    | 8192      | 8192      | 8192                                           | 2048                    | 128                     |
| Max Anisotropy                                                                                                           | 16                        | 16                        | 16                       | 16                       | 16        | 16        | 16                                             | 16                      | 2                       |
| Max Primitive Count                                                                                                      | 2^32 – 1                  | 2^32 – 1                  | 2^32 – 1                 | 2^32 – 1                 | 2^32 – 1  | 2^32 – 1  | 1048575                                        | 1048575                 | 65535                   |
| Max Vertex Index                                                                                                         | 2^32 – 1                  | 2^32 – 1                  | 2^32 – 1                 | 2^32 – 1                 | 2^32 – 1  | 2^32 – 1  | 1048575                                        | 1048575                 | 65534                   |
| Max Input Slots                                                                                                          | 32                        | 32                        | 32                       | 32                       | 32        | 16        | 16                                             | 16                      | 16                      |
| Simultaneous Render Targets                                                                                              | 8                         | 8                         | 8                        | 8                        | 8         | 8         | 4                                              | 1                       | 1                       |
| Occlusion Queries                                                                                                        | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | Yes                                            | Yes                     | No                      |
| Separate Alpha Blend                                                                                                     | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | Yes                                            | Yes                     | No                      |
| Mirror Once                                                                                                              | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | Yes                                            | Yes                     | No                      |
| Overlapping Vertex Elements                                                                                              | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | Yes                                            | Yes                     | No                      |
| Independent Write Masks                                                                                                  | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | Yes                                            | No                      | No                      |
| Instancing                                                                                                               | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | Yes                                            | No                      | No                      |
| Nonpowers-of-2 conditionally³                                                                                            | No                        | No                        | No                       | No                       | No        | No        | Yes                                            | Yes                     | Yes                     |
| Nonpowers-of-2 unconditionally⁴                                                                                          | Yes                       | Yes                       | Yes                      | Yes                      | Yes       | Yes       | No                                             | No                      | No                      |



 

⁰ Requires the Direct3D 11.3 or Direct3D 12 runtime.

¹ Requires the Direct3D 11.1 runtime.

² Shader model 5.0 and above can optionally support double-precision shaders, extended double-precision shaders, the **SAD4** shader instruction, and partial-precision shaders. To determine the shader model 5.0 options that are available for DirectX 11, call [**ID3D11Device::CheckFeatureSupport**](/windows/win32/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport). Some compatibility depends on what hardware you are running on. Shader model 5.1 and above are only supported through the DirectX 12 API, regardless of the feature level that's being used. DirectX 11 only supports up to shader model 5.0. The DirectX 12 API only goes down to feature level 11\_0.

³ At feature levels 9\_1, 9\_2 and 9\_3, the display device supports the use of 2-D textures with dimensions that are not powers of two under two conditions. First, only one MIP-map level for each texture can be created, and second, no wrap sampler modes for textures are allowed (that is, the **AddressU**, **AddressV**, and **AddressW** members of [**D3D11\_SAMPLER\_DESC**](/windows/win32/api/D3D11/ns-d3d11-d3d11_sampler_desc) cannot be set to [**D3D11\_TEXTURE\_ADDRESS\_WRAP**](/windows/win32/api/D3D11/ne-d3d11-d3d11_texture_address_mode)).

⁴ At feature levels 10\_0, 10\_1 and 11\_0, the display device unconditionally supports the use of 2-D textures with dimensions that are not powers of two.

⁵ Vertex Shader 2a with 256 instructions, 32 temporary registers, static flow control of depth 4, dynamic flow control of depth 24, and D3DVS20CAPS\_PREDICATION. Pixel Shader 2x with 512 instructions, 32 temporary registers, static flow control of depth 4, dynamic flow control of depth 24, D3DPS20CAPS\_ARBITRARYSWIZZLE, D3DPS20CAPS\_GRADIENTINSTRUCTIONS, D3DPS20CAPS\_PREDICATION, D3DPS20CAPS\_NODEPENDENTREADLIMIT, and D3DPS20CAPS\_NOTEXINSTRUCTIONLIMIT.

⁶ Higher tiers optional.

For details of format support at different hardware feature levels, refer to:

-   [DXGI Format Support for Direct3D Feature Level 12.1 Hardware](../direct3ddxgi/hardware-support-for-direct3d-12-1-formats.md)
-   [DXGI Format Support for Direct3D Feature Level 12.0 Hardware](../direct3ddxgi/hardware-support-for-direct3d-12-0-formats.md)
-   [DXGI Format Support for Direct3D Feature Level 11.1 Hardware](../direct3ddxgi/format-support-for-direct3d-11-1-feature-level-hardware.md)
-   [DXGI Format Support for Direct3D Feature Level 11.0 Hardware](../direct3ddxgi/format-support-for-direct3d-11-0-feature-level-hardware.md)
-   [Hardware Support for Direct3D 10Level9 Formats](/previous-versions/ff471324(v=vs.85))
-   [Hardware Support for Direct3D 10.1 Formats](/previous-versions/cc627091(v=vs.85))
-   [Hardware Support for Direct3D 10 Formats](/previous-versions/cc627090(v=vs.85))

## Related topics

<dl> <dt>

[Direct3D 11 on Downlevel Hardware](overviews-direct3d-11-devices-downlevel.md)

[Hardware Feature Levels (Direct3D 12)](../direct3d12/hardware-feature-levels.md)
</dt> </dl>