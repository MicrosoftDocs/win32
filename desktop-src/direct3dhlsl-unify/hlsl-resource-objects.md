# HLSL Resource Objects

HLSL Resource objects in are used in HLSL to access resource views or samplers in D3D.  They may be bound through a root signature, or dynamically created by indexing descriptor heaps.  A "resource" from the perspective of HLSL is defined differently than the meaning used in the D3D API.

There are four resource classes:

| Abbrev. | binding | Resource Class | Description |
| - | - | - | - |
| [SRV](#srv-objects) | t | Shader Resource View | Read-only view into resource data |
| [UAV](#uav-objects) | u | Unordered Access View | Read/Write view into resource data |
| [CBV](#cbv-objects) | b | Constant Buffer View | Read-only view into constant buffer data |
| [Sampler](#sampler-objects) | s | Sampler | SamplerState or SamplerCmpState descriptor |

For each Resource Class, there are a number of specific object types, some of which can be grouped into some high level categories:

## SRV Objects

### SRV Textures

A texture resource is a structured collection of data designed to store texels. A texel represents the smallest unit of a texture that can be read or written to by the pipeline. Unlike buffers, textures can be filtered by texture samplers as they are read by shader units. The type of texture impacts how the texture is filtered. Each texel contains 1 to 4 components, arranged in one of the DXGI formats defined by the DXGI_FORMAT enumeration.

Textures are created as a structured resource with a known size. However, each texture may be typed or typeless when the resource is created as long as the type is fully specified using a view when the texture is bound to the pipeline.

```declarations
Texture2D <float4> MyTex;

Texture2DMS <float4, 8> MyMSTex;
```

| Object | Description |
| - | - |
| [Texture1D](hlsl-obj-texture1d.md) | read-only 1 dimensional texture |
| [Texture1DArray](hlsl-obj-texture1darray.md) | read-only 1 dimensional texture array |
| [Texture2D](hlsl-obj-texture2d.md) | read-only 2 dimensional texture |
| [Texture2DArray](hlsl-obj-texture2darray.md) | read-only 2 dimensional texture array |
| [Texture2DMS](hlsl-obj-texture2dms.md) | read-only 2 dimensional multi-sample texture |
| [Texture2DMSArray](hlsl-obj-texture2dmsarray.md) | read-only 2 dimensional multi-sample texture array |
| [Texture3D](hlsl-obj-texture3d.md) | read-only 3 dimensional texture |
| [TextureCube](hlsl-obj-texturecube.md) | read-only cube texture |
| [TextureCubeArray](hlsl-obj-texturecubearray.md) | read-only cube texture array |

### SRV Buffers

| Object | Description |
| - | - |
| [Buffer](hlsl-obj-buffer.md) | read-only typed buffer |
| [ByteAddressBuffer](hlsl-obj-byteaddressbuffer.md) | read-only raw byte buffer |
| [StructuredBuffer](hlsl-obj-structuredbuffer.md) | read-only structured buffer |
| [TextureBuffer](hlsl-obj-texturebuffer.md) | object for reading data in constant buffer layout from a typed buffer |

### SRV Other

| Object | Description |
| - | - |
| [RTAccelerationStructure](hlsl-obj-rtaccelerationstructure.md) | Acceleration structure object used for Raytracing (see: TraceRay) |

## UAV Objects

### UAV Textures

UAV textures are read/write views into texture resources.  The supported formats and operations are different than for SRV Textures.

| Object | Description |
| - | - |
| [RWTexture1D](hlsl-obj-rwtexture1d.md) | read/write 1 dimensional texture |
| [RWTexture1DArray](hlsl-obj-rwtexture1darray.md) | read/write 1 dimensional texture array |
| [RWTexture2D](hlsl-obj-rwtexture2d.md) | read/write 2 dimensional texture |
| [RWTexture2DArray](hlsl-obj-rwtexture2darray.md) | read/write 2 dimensional texture array |
| [RWTexture3D](hlsl-obj-rwtexture3d.md) | read/write 3 dimensional texture |

### UAV Buffers

| Object | Description |
| - | - |
| [RWBuffer](hlsl-obj-rwbuffer.md) | read/write typed buffer |
| [RWByteAddressBuffer](hlsl-obj-rwbyteaddressbuffer.md) | read/write raw byte buffer |
| [RWStructuredBuffer](hlsl-obj-rwstructuredbuffer.md) | read/write structured buffer (accessed as an array of structs) |

### UAV Other

| Object | Description |
| - | - |
| [FeedbackTexture2D](hlsl-obj-feedbacktexture2d.md) | resource for writing sampler feedback for a `Texture2D` |
| [FeedbackTexture2DArray](hlsl-obj-feedbacktexture2darray.md) | resource for writing sampler feedback for a `Texture2DArray` |

## Sampler Objects

| Object | Description |
| - | - |
| [SamplerState](hlsl-obj-samplerstate.md) | sampler state used in sampling operations |
| [SamplerComparisonState](hlsl-obj-samplercomparisonstate.md) | comparison sampler state used in comparison sampling operations |
