# Texture Object

## Definition

A texture resource is a structured collection of data designed to store texels. A texel represents the smallest unit of a texture that can be read or written to by the pipeline. Unlike buffers, textures can be filtered by texture samplers as they are read by shader units. The type of texture impacts how the texture is filtered. Each texel contains 1 to 4 components, arranged in one of the DXGI formats defined by the DXGI_FORMAT enumeration.

Textures are created as a structured resource with a known size. However, each texture may be typed or typeless when the resource is created as long as the type is fully specified using a view when the texture is bound to the pipeline.

```declarations
Texture2D <float4> MyTex;

Texture2DMS <float4, 8> MyMSTex;
```

## Objects

| Object | Description |
| - | - |
| [Texture1D](#texture1d) | read-only 1 dimensional texture |
| [Texture1DArray](#texture1darray) | read-only 1 dimensional texture array |
| [Texture2D](#texture2d) | read-only 2 dimensional texture |
| [Texture2DArray](#texture2darray) | read-only 2 dimensional texture array |
| [Texture2DMS](#texture2dms) | read-only 2 dimensional multi-sample texture |
| [Texture2DMSArray](#texture2dmsarray) | read-only 2 dimensional multi-sample texture array |
| [Texture3D](#texture3d) | read-only 3 dimensional texture |
| [TextureCube](#texturecube) | read-only cube texture |
| [TextureCubeArray](#texturecubearray) | read-only cube texture array |
| [RWTexture1D](#rwtexture1d) | read/write 1 dimensional texture |
| [RWTexture1DArray](#rwtexture1darray) | read/write 1 dimensional texture array |
| [RWTexture2D](#rwtexture2d) | read/write 2 dimensional texture |
| [RWTexture2DArray](#rwtexture2darray) | read/write 2 dimensional texture array |
| [RWTexture3D](#rwtexture3d) | read/write 3 dimensional texture |

> Each object section could be a page instead of a section on this page, potentially.

### Texture1D

> TBD: What do we put here to make object template clear?

```HLSL
// template < typename ElementType = float4 > class Texture1D;
Texture1D<float> MyTex;
```

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texture1d) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texture1d) | Samples a texture. |
| [Load](texture-load.md#texture1d) | Load texel data without sampling. |
| ... | ... |

### Texture1DArray

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texture1darray) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texture1darray) | Samples a texture. |
| [Load](texture-load.md#texture1darray) | Load texel data without sampling. |
| ... | ... |

### Texture2D

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texture2d) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texture2d) | Samples a texture. |
| [Load](texture-load.md#texture2d) | Load texel data without sampling. |
| ... | ... |

### Texture2DArray

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texture2darray) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texture2darray) | Samples a texture. |
| [Load](texture-load.md#texture2darray) | Load texel data without sampling. |
| ... | ... |

### Texture2DMS

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texture2dms) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texture2dms) | Samples a texture. |
| [Load](texture-load.md#texture2dms) | Load texel data without sampling. |
| ... | ... |

### Texture2DMSArray

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texture2dmsarray) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texture2dmsarray) | Samples a texture. |
| [Load](texture-load.md#texture2dmsarray) | Load texel data without sampling. |
| ... | ... |

### Texture3D

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texture3d) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texture3d) | Samples a texture. |
| [Load](texture-load.md#texture3d) | Load texel data without sampling. |
| ... | ... |

### TextureCube

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texturecube) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texturecube) | Samples a texture. |
| ... | ... |

### TextureCubeArray

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#texturecubearray) | Get dimensions for the texture. |
| [Sample](texture-sample.md#texturecubearray) | Samples a texture. |
| ... | ... |

### RWTexture1D

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#rwtexture1d) | Get dimensions for the texture. |
| [Load](texture-load.md#rwtexture1d) | Load texel data without sampling. |
| ... | ... |

### RWTexture1DArray

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#rwtexture1darray) | Get dimensions for the texture. |
| [Load](texture-load.md#rwtexture1darray) | Load texel data without sampling. |
| ... | ... |

### RWTexture2D

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#rwtexture2d) | Get dimensions for the texture. |
| [Load](texture-load.md#rwtexture2d) | Load texel data without sampling. |
| ... | ... |

### RWTexture2DArray

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#rwtexture2darray) | Get dimensions for the texture. |
| [Load](texture-load.md#rwtexture2darray) | Load texel data without sampling. |
| ... | ... |

### RWTexture3D

| Method | Description |
| - | - |
| [GetDimensions](texture-getdimensions.md#rwtexture3d) | Get dimensions for the texture. |
| [Load](texture-load.md#rwtexture3d) | Load texel data without sampling. |
| ... | ... |

## All Methods

> Just a prototype seeing what it would look like to try to unify a table with one entry per-method.

| Objects | Method | Description |
| - | - | - |
| Texture1D[Array], Texture2D[Array], Texture2DMS[Array], Texture3D, TextureCube[Array] | [Sample](texture-sample.md#texture1d) | Samples a texture. |
| [RW]Texture1D[Array], [RW]Texture2D[Array], Texture2DMS[Array], [RW]Texture3D, TextureCube[Array] | [GetDimensions](texture-getdimensions.md#texture1d) | Get dimensions for the texture. |
| [RW]Texture1D[Array], [RW]Texture2D[Array], Texture2DMS[Array], [RW]Texture3D | [Load](texture-load.md#texture1d) | Load texel data without sampling. |
| RWTexture1D[Array], RWTexture2D[Array], Texture2DMS[Array], RWTexture3D | Store | Store texel data |
