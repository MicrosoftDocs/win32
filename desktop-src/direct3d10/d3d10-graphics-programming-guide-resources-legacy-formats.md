---
description: This table lists the Direct3D 9 formats that can be mapped to a Direct3D 10 format.
ms.assetid: 07c9b827-6e2e-4599-b48a-f726484b643d
title: 'Legacy Formats: Map Direct3D 9 Formats to Direct3D 10'
ms.topic: article
ms.date: 05/31/2018
---

# Legacy Formats: Map Direct3D 9 Formats to Direct3D 10

This table lists the Direct3D 9 formats that can be mapped to a Direct3D 10 format. The Direct3D 10 formats have diverged from the Direct3D 9 formats so that vertex and texture formats can be merged to enable cross-endian applications.



| Direct3D 9 Texture/Vertex/Index Format | Equivalent Direct3D 10 Format                                        |
|----------------------------------------|----------------------------------------------------------------------|
| D3DFMT\_UNKNOWN                        | DXGI\_FORMAT\_UNKNOWN                                                |
| D3DFMT\_R8G8B8                         | Not available                                                        |
| D3DFMT\_A8R8G8B8                       | DXGI\_FORMAT\_B8G8R8A8\_UNORM (DXGI 1.1)                             |
| D3DFMT\_X8R8G8B8                       | DXGI\_FORMAT\_B8G8R8X8\_UNORM (DXGI 1.1)                             |
| D3DFMT\_R5G6B5                         | DXGI\_FORMAT\_B5G6R5\_UNORM (DXGI 1.2)                               |
| D3DFMT\_X1R5G5B5                       | Not available                                                        |
| D3DFMT\_A1R5G5B5                       | DXGI\_FORMAT\_B5G5R5A1\_UNORM (DXGI 1.2)                             |
| D3DFMT\_A4R4G4B4                       | DXGI\_FORMAT\_B4G4R4A4\_UNORM (DXGI 1.2)                             |
| D3DFMT\_R3G3B2                         | Not available                                                        |
| D3DFMT\_A8                             | DXGI\_FORMAT\_A8\_UNORM                                              |
| D3DFMT\_A8R3G3B2                       | Not available                                                        |
| D3DFMT\_X4R4G4B4                       | Not available                                                        |
| D3DFMT\_A2B10G10R10                    | DXGI\_FORMAT\_R10G10B10A2                                            |
| D3DFMT\_A8B8G8R8                       | DXGI\_FORMAT\_R8G8B8A8\_UNORM or DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB |
| D3DFMT\_X8B8G8R8                       | Not available                                                        |
| D3DFMT\_G16R16                         | DXGI\_FORMAT\_R16G16\_UNORM                                          |
| D3DFMT\_A2R10G10B10                    | Not available                                                        |
| D3DFMT\_A16B16G16R16                   | DXGI\_FORMAT\_R16G16B16A16\_UNORM                                    |
| D3DFMT\_A8P8                           | Not available                                                        |
| D3DFMT\_P8                             | Not available                                                        |
| D3DFMT\_L8                             | DXGI\_FORMAT\_R8\_UNORM ¹                                            |
| D3DFMT\_A8L8                           | Not available                                                        |
| D3DFMT\_A4L4                           | Not available                                                        |
| D3DFMT\_V8U8                           | DXGI\_FORMAT\_R8G8\_SNORM                                            |
| D3DFMT\_L6V5U5                         | Not available                                                        |
| D3DFMT\_X8L8V8U8                       | Not available                                                        |
| D3DFMT\_Q8W8V8U8                       | DXGI\_FORMAT\_R8G8B8A8\_SNORM                                        |
| D3DFMT\_V16U16                         | DXGI\_FORMAT\_R16G16\_SNORM                                          |
| D3DFMT\_W11V11U10                      | Not available                                                        |
| D3DFMT\_A2W10V10U10                    | Not available                                                        |
| D3DFMT\_UYVY                           | Not available                                                        |
| D3DFMT\_R8G8\_B8G8                     | DXGI\_FORMAT\_G8R8\_G8B8\_UNORM ²                                    |
| D3DFMT\_YUY2                           | Not available                                                        |
| D3DFMT\_G8R8\_G8B8                     | DXGI\_FORMAT\_R8G8\_B8G8\_UNORM ²                                    |
| D3DFMT\_DXT1                           | DXGI\_FORMAT\_BC1\_UNORM or DXGI\_FORMAT\_BC1\_UNORM\_SRGB           |
| D3DFMT\_DXT2                           | DXGI\_FORMAT\_BC2\_UNORM or DXGI\_FORMAT\_BC2\_UNORM\_SRGB ³         |
| D3DFMT\_DXT3                           | DXGI\_FORMAT\_BC2\_UNORM or DXGI\_FORMAT\_BC2\_UNORM\_SRGB           |
| D3DFMT\_DXT4                           | DXGI\_FORMAT\_BC3\_UNORM or DXGI\_FORMAT\_BC3\_UNORM\_SRGB ³         |
| D3DFMT\_DXT5                           | DXGI\_FORMAT\_BC3\_UNORM or DXGI\_FORMAT\_BC3\_UNORM\_SRGB           |
| D3DFMT\_D16 and D3DFMT\_D16\_LOCKABLE  | DXGI\_FORMAT\_D16\_UNORM                                             |
| D3DFMT\_D32                            | Not available                                                        |
| D3DFMT\_D15S1                          | Not available                                                        |
| D3DFMT\_D24S8                          | Not available                                                        |
| D3DFMT\_D24X8                          | Not available                                                        |
| D3DFMT\_D24X4S4                        | Not available                                                        |
| D3DFMT\_D16                            | DXGI\_FORMAT\_D16\_UNORM                                             |
| D3DFMT\_D32F\_LOCKABLE                 | DXGI\_FORMAT\_D32\_FLOAT                                             |
| D3DFMT\_D24FS8                         | Not available                                                        |
| D3DFMT\_S1D15                          | Not available                                                        |
| D3DFMT\_S8D24                          | DXGI\_FORMAT\_D24\_UNORM\_S8\_UINT                                   |
| D3DFMT\_X8D24                          | Not available                                                        |
| D3DFMT\_X4S4D24                        | Not available                                                        |
| D3DFMT\_L16                            | DXGI\_FORMAT\_R16\_UNORM ¹                                           |
| D3DFMT\_INDEX16                        | DXGI\_FORMAT\_R16\_UINT                                              |
| D3DFMT\_INDEX32                        | DXGI\_FORMAT\_R32\_UINT                                              |
| D3DFMT\_Q16W16V16U16                   | DXGI\_FORMAT\_R16G16B16A16\_SNORM                                    |
| D3DFMT\_MULTI2\_ARGB8                  | Not available                                                        |
| D3DFMT\_R16F                           | DXGI\_FORMAT\_R16\_FLOAT                                             |
| D3DFMT\_G16R16F                        | DXGI\_FORMAT\_R16G16\_FLOAT                                          |
| D3DFMT\_A16B16G16R16F                  | DXGI\_FORMAT\_R16G16B16A16\_FLOAT                                    |
| D3DFMT\_R32F                           | DXGI\_FORMAT\_R32\_FLOAT                                             |
| D3DFMT\_G32R32F                        | DXGI\_FORMAT\_R32G32\_FLOAT                                          |
| D3DFMT\_A32B32G32R32F                  | DXGI\_FORMAT\_R32G32B32A32\_FLOAT                                    |
| D3DFMT\_CxV8U8                         | Not available                                                        |
| D3DDECLTYPE\_FLOAT1                    | DXGI\_FORMAT\_R32\_FLOAT                                             |
| D3DDECLTYPE\_FLOAT2                    | DXGI\_FORMAT\_R32G32\_FLOAT                                          |
| D3DDECLTYPE\_FLOAT3                    | DXGI\_FORMAT\_R32G32B32\_FLOAT                                       |
| D3DDECLTYPE\_FLOAT4                    | DXGI\_FORMAT\_R32G32B32A32\_FLOAT                                    |
| D3DDECLTYPED3DCOLOR                    | Not available                                                        |
| D3DDECLTYPE\_UBYTE4                    | DXGI\_FORMAT\_R8G8B8A8\_UINT ⁴                                       |
| D3DDECLTYPE\_SHORT2                    | DXGI\_FORMAT\_R16G16\_SINT                                           |
| D3DDECLTYPE\_SHORT4                    | DXGI\_FORMAT\_R16G16B16A16\_SINT                                     |
| D3DDECLTYPE\_UBYTE4N                   | DXGI\_FORMAT\_R8G8B8A8\_UNORM                                        |
| D3DDECLTYPE\_SHORT2N                   | DXGI\_FORMAT\_R16G16\_SNORM                                          |
| D3DDECLTYPE\_SHORT4N                   | DXGI\_FORMAT\_R16G16B16A16\_SNORM                                    |
| D3DDECLTYPE\_USHORT2N                  | DXGI\_FORMAT\_R16G16\_UNORM                                          |
| D3DDECLTYPE\_USHORT4N                  | DXGI\_FORMAT\_R16G16B16A16\_UNORM                                    |
| D3DDECLTYPE\_UDEC3                     | Not available                                                        |
| D3DDECLTYPE\_DEC3N                     | Not available                                                        |
| D3DDECLTYPE\_FLOAT16\_2                | DXGI\_FORMAT\_R16G16\_FLOAT                                          |
| D3DDECLTYPE\_FLOAT16\_4                | DXGI\_FORMAT\_R16G16B16A16\_FLOAT                                    |



 

1.  Use .r swizzle in a shader to duplicate red to other components to get Direct3D 9 behavior.
2.  In Direct3D 9, the data was scaled up by 255.0f which can be done in shader code instead.
3.  DXT2 and DXT3 are the same from an API perspective; DXT4 and DXT5 are the same from an API perspective. The only difference was premultiplied alpha, which can be tracked by an application and does not need a separate format.
4.  A shader gets UINT values, but if Direct3D 9 style integral floats (0.0f, 1.0f... 255.f) are needed, UINT can be converted to float32 in a shader.

## Related topics

<dl> <dt>

[Resources (Direct3D 10)](d3d10-graphics-programming-guide-resources.md)
</dt> </dl>

 

 



