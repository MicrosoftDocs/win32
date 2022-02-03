# `<TextureObject>::Sample` Methods

- [`<TextureObject>::Sample` Methods](#textureobjectsample-methods)
  - [Definition](#definition)
    - [In this Article](#in-this-article)
  - [Supported Shader Models](#supported-shader-models)
  - [Remarks](#remarks)
    - [Calculating texel positions](#calculating-texel-positions)
    - [Applying texture coordinate offsets](#applying-texture-coordinate-offsets)
  - [Supported Objects](#supported-objects)
    - [`Texture1D`](#texture1d)
    - [`Texture1DArray`](#texture1darray)
    - [`Texture2D`](#texture2d)
    - [`Texture2DArray`](#texture2darray)
    - [`Texture3D`](#texture3d)
    - [`TextureCube`](#texturecube)
    - [`TextureCubeArray`](#texturecubearray)
  - [All Overloads](#all-overloads)
    - [Overloads without immediate offsets](#overloads-without-immediate-offsets)
    - [Overloads with immediate offsets](#overloads-with-immediate-offsets)
    - [`Sample( SamplerState samp, <CoordType> coord )`](#sample-samplerstate-samp-coordtype-coord-)
    - [`Sample( SamplerState samp, <CoordType> coord, float lodClamp )`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-)
    - [`Sample( SamplerState samp, <CoordType> coord, float lodClamp, out uint status )`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-)
    - [`Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset )`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-)
    - [`Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset, float lodClamp )`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-)
    - [`Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset, float lodClamp, out uint status )`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-out-uint-status-)
  - [Return Values](#return-values)
    - [`<ElementType>`](#elementtype)
  - [Parameters](#parameters)
    - [`SamplerState samp`](#samplerstate-samp)
    - [`<CoordType> coord`](#coordtype-coord)
    - [`<OffsetType> offset`](#offsettype-offset)
    - [`float lodClamp`](#float-lodclamp)
    - [`out uint status`](#out-uint-status)

> Please Ignore the above TOC - this is only for development purposes.  a list of sections, like the following, is probably more appropriate.

Many other things TBD:

- File naming convention
- Title naming convention
- Section ordering
- Various formatting decisions
- Supported Shader Models final layout
- Whether 'All Overloads' section should have the full set of methods listed in a table (or two) again
  - (plus) Could be useful to see all overloads across all objects without per-object duplicates.  You can see the argument types that are based on the object template, and get an idea of the overall pattern.
  - (minus) Looks odd when just finished with per-object overloads to see another set of all the overloads again.
- How to maintain duplicated content (generate?)
- Whether one shader model section will be good enough for all overloads and all objects (for other methods, there may be some special cases)
- What else to write into each method section
- Should method syntax separate each parameter onto a different line?

## Definition

Samples a texture.

```HLSL
Texture1D <float4> MyTex;
```

TODO: require exposition on Sample

### In this Article

- [Definition](#definition)
- [Supported Shader Models](#supported-shader-models)
- [Remarks](#remarks)
- [Supported Objects](#supported-objects)
- [All Overloads](#all-overloads)
- [Parameters](#parameters)
- [Return Values](#return-values)

## Supported Shader Models

| Shader Model | 6.0 | 6.1 | 6.2 | 6.3 | 6.4 | 6.5 | 6.6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Vertex | - | - | - | - | - | - | - |
| Hull | - | - | - | - | - | - | - |
| Domain | - | - | - | - | - | - | - |
| Geometry | - | - | - | - | - | - | - |
| Amplification | - | - | - | - | - | - | 1* |
| Mesh | - | - | - | - | - | - | 1* |
| Pixel | x | x | x | x | x | x | x |
| Compute | - | - | - | - | - | - | x |

| Key | Description |
| - | - |
| x | Supported |
| 1* | Supported with optional feature: `SHADER_FEATURE_DERIVATIVES_IN_MESH_AND_AMPLIFICATION_SHADERS` |

>TBD: Make optional feature into a link

Library `export` function support depends on the entry point that calls the function.

## Remarks

Texture sampling uses the texel position to look up a texel value. An offset can be applied to the position before lookup. The sampler state contains the sampling and filtering options. This method can be invoked within a pixel shader, but it is not supported in a vertex shader or a geometry shader.

Use an offset only at an integer miplevel; otherwise, you may get different results depending on hardware implementation or driver settings.

### Calculating texel positions

Texture coordinates are floating-point values that reference texture data, which is also known as normalized texture space. Address wrapping modes are applied in this order (texture coordinates + offsets + wrap mode) to modify texture coordinates outside the [0...1] range.

For texture arrays, an additional value in the location parameter specifies an index into a texture array. This index is treated as a scaled float value (instead of the normalized space for standard texture coordinates). The conversion to an integer index is done in the following order (float + round-to-nearest-even integer + clamp to the array range).

### Applying texture coordinate offsets

The offset parameter modifies the texture coordinates, in texel space. Even though texture coordinates are normalized floating-point numbers, the offset applies an integer offset. Also note that the texture offsets need to be static.

The data format returned is determined by the texture format. For example, if the texture resource was defined with the DXGI_FORMAT_A8B8G8R8_UNORM_SRGB format, the sampling operation converts sampled texels from gamma 2.0 to 1.0, filter, and writes the result as a floating-point value in the range [0..1].

## Supported Objects

| TextureObject | Supported | Overloads |
| --------------- | ------------ | ------------ |
| [`Texture1D`](#texture1d) | yes | [All Overloads](#all-overloads) |
| [`Texture1DArray`](#texture1darray) | yes | [All Overloads](#all-overloads) |
| [`Texture2D`](#texture2d) | yes | [All Overloads](#all-overloads) |
| [`Texture2DArray`](#texture2darray) | yes | [All Overloads](#all-overloads) |
| `Texture2DMS` | no |
| `Texture2DMSArray` | no |
| [`Texture3D`](#texture3d) | yes | [All Overloads](#all-overloads) |
| [`TextureCube`](#texturecube) | yes | [Overloads without immediate offsets](#overloads-without-immediate-offsets) |
| [`TextureCubeArray`](#texturecubearray) | yes | [Overloads without immediate offsets](#overloads-without-immediate-offsets) |
| `RWTexture1D` | no |
| `RWTexture1DArray` | no |
| `RWTexture2D` | no |
| `RWTexture2DArray` | no |
| `RWTexture3D` | no |

### `Texture1D`

> link from Texture1D page/section at "Sample()" method in methods table to this section in this Sample.md document.

The following method overloads are supported for `Texture1D::Sample(...)`.

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-) ( [`SamplerState samp`](#samplerstate-samp), [`float coord`](#coordtype-coord) ) | Samples a texture. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with a level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with a level of detail clamp; reports residency status. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-) ( [`SamplerState samp`](#samplerstate-samp), [`float coord`](#coordtype-coord), [`uint offset`](#offsettype-offset) ) | Samples a texture with an immediate offset. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float coord`](#coordtype-coord), [`uint offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with an immediate offset and level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float coord`](#coordtype-coord), [`uint offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with an immediate offset and level of detail clamp; reports residency status. |

### `Texture1DArray`

The following method overloads are supported for `Texture1DArray::Sample(...)`.

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord) ) | Samples a texture. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with a level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with a level of detail clamp; reports residency status. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`int offset`](#offsettype-offset) ) | Samples a texture with an immediate offset. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`int offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with an immediate offset and level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`int offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with an immediate offset and level of detail clamp; reports residency status. |

### `Texture2D`

The following method overloads are supported for `Texture2D::Sample(...)`.

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord) ) | Samples a texture. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with a level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with a level of detail clamp; reports residency status. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`int2 offset`](#offsettype-offset) ) | Samples a texture with an immediate offset. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`int2 offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with an immediate offset and level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float2 coord`](#coordtype-coord), [`int2 offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with an immediate offset and level of detail clamp; reports residency status. |

### `Texture2DArray`

The following method overloads are supported for `Texture2DArray::Sample(...)`.

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord) ) | Samples a texture. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with a level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with a level of detail clamp; reports residency status. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`int2 offset`](#offsettype-offset) ) | Samples a texture with an immediate offset. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`int2 offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with an immediate offset and level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`int2 offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with an immediate offset and level of detail clamp; reports residency status. |

### `Texture3D`

The following method overloads are supported for `Texture3D::Sample(...)`.

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord) ) | Samples a texture. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with a level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with a level of detail clamp; reports residency status. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`int3 offset`](#offsettype-offset) ) | Samples a texture with an immediate offset. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`int3 offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with an immediate offset and level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`int3 offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with an immediate offset and level of detail clamp; reports residency status. |

### `TextureCube`

The following method overloads are supported for `TextureCube::Sample(...)`.

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord) ) | Samples a texture. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with a level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float3 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with a level of detail clamp; reports residency status. |

### `TextureCubeArray`

The following method overloads are supported for `TextureCubeArray::Sample(...)`.

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-) ( [`SamplerState samp`](#samplerstate-samp), [`float4 coord`](#coordtype-coord) ) | Samples a texture. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`float4 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with a level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`float4 coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with a level of detail clamp; reports residency status. |

## All Overloads

> I Don't know if we need the tables here, but it does represent the canonical set of overload sections where each one is shared across object types.

### Overloads without immediate offsets

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-) ( [`SamplerState samp`](#samplerstate-samp), [`<CoordType> coord`](#coordtype-coord) ) | Samples a texture. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`<CoordType> coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with a level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`<CoordType> coord`](#coordtype-coord), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with a level of detail clamp; reports residency status. |

### Overloads with immediate offsets

These are not supported by `TextureCube` or `TextureCubeArray` objects.

| Method Signature | Description |
| --------- | ----------- |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-) ( [`SamplerState samp`](#samplerstate-samp), [`<CoordType> coord`](#coordtype-coord), [`<OffsetType> offset`](#offsettype-offset) ) | Samples a texture with an immediate offset. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-) ( [`SamplerState samp`](#samplerstate-samp), [`<CoordType> coord`](#coordtype-coord), [`<OffsetType> offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp) ) | Samples a texture with an immediate offset and level of detail clamp. |
| [`<ElementType>`](#elementtype) [`Sample`](#sample-samplerstate-samp-coordtype-coord-offsettype-offset-float-lodclamp-out-uint-status-) ( [`SamplerState samp`](#samplerstate-samp), [`<CoordType> coord`](#coordtype-coord), [`<OffsetType> offset`](#offsettype-offset), [`float lodClamp`](#float-lodclamp), [`out uint status`](#out-uint-status) ) | Samples a texture with an immediate offset and level of detail clamp; reports residency status. |

### `Sample( SamplerState samp, <CoordType> coord )`

Samples a texture.

<b>Syntax</b>

```syntax
<TextureObject>.Sample( SamplerState samp, <CoordType> coord );
```

| Parameter | Description |
| --------- | ----------- |
| [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |

Types that depend on texture object:

| TextureObject | [`<CoordType>`](#coordtype-coord) |
| --- | --- |
| `Texture1D` | `float` |
| `Texture1DArray` | `float2` |
| `Texture2D` | `float2` |
| `Texture2DArray` | `float3` |
| `Texture3D` | `float3` |
| `TextureCube` | `float3` |
| `TextureCubeArray` | `float4` |

<b>Example</b>

> Example only under this overload, because this is the one that's actually being used.  Also, this has been fixed and completed from what originally appeared in the documentation.

```HLSL
// Object Declarations
Texture2D g_MeshTexture;            // Color texture for mesh
SamplerState MeshTextureSampler;

struct VS_OUTPUT
{
    float4 Position   : SV_POSITION; // vertex position
    float4 Diffuse    : COLOR0;      // vertex diffuse color
    float2 TextureUV  : TEXCOORD0;   // vertex texture coords
};

float4 PSMain(VS_OUTPUT In) : SV_Target
{
  return g_MeshTexture.Sample(MeshTextureSampler, In.TextureUV) * In.Diffuse;
}
```

### `Sample( SamplerState samp, <CoordType> coord, float lodClamp )`

Samples a texture with a value to clamp sample level-of-detail (LOD) values to.

```syntax
<ElementType> <TextureObject>.Sample( SamplerState samp, <CoordType> coord, float lodClamp );
```

| Parameter | Description |
| --------- | ----------- |
| [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| [`float lodClamp`](#float-lodclamp) | A value to clamp sample LOD values to. |

Types that depend on texture object:

| TextureObject | [`<CoordType>`](#coordtype-coord) |
| --- | --- |
| `Texture1D` | `float` |
| `Texture1DArray` | `float2` |
| `Texture2D` | `float2` |
| `Texture2DArray` | `float3` |
| `Texture3D` | `float3` |
| `TextureCube` | `float3` |
| `TextureCubeArray` | `float4` |

### `Sample( SamplerState samp, <CoordType> coord, float lodClamp, out uint status )`

Samples a texture with aa value to clamp sample level-of-detail (LOD) values to, and returns status of the operation.

```syntax
<ElementType> <TextureObject>.Sample( SamplerState samp, <CoordType> coord, float lodClamp, out uint status );
```

| Parameter | Description |
| --------- | ----------- |
| [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| [`float lodClamp`](#float-lodclamp) | A value to clamp sample LOD values to. |
| [`out uint status`](#out-uint-status) | The residency status of the operation. |

Types that depend on texture object:

| TextureObject | [`<CoordType>`](#coordtype-coord) |
| --- | --- |
| `Texture1D` | `float` |
| `Texture1DArray` | `float2` |
| `Texture2D` | `float2` |
| `Texture2DArray` | `float3` |
| `Texture3D` | `float3` |
| `TextureCube` | `float3` |
| `TextureCubeArray` | `float4` |

### `Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset )`

Samples a texture with an immediate offset.  Not supported by TextureCube and TextureCubeArray objects.

```syntax
<ElementType> <TextureObject>.Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset );
```

| Parameter | Description |
| --------- | ----------- |
| [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| [`<OffsetType> offset`](#offsettype-offset) | An integral offset in texels from the sampling location in the texture. |

Types that depend on texture object:

| TextureObject | [`<CoordType>`](#coordtype-coord) | [`<OffsetType>`](#offsettype-offset) |
| --- | --- | --- |
| `Texture1D` | `float` | `int` |
| `Texture1DArray` | `float2` | `int` |
| `Texture2D` | `float2` | `int2` |
| `Texture2DArray` | `float3` | `int2` |
| `Texture3D` | `float3` | `int3` |

### `Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset, float lodClamp )`

Samples a texture with an optional value to clamp sample level-of-detail (LOD) values to.

```syntax
<ElementType> <TextureObject>.Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset, float lodClamp );
```

| Parameter | Description |
| --------- | ----------- |
| [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| [`<OffsetType> offset`](#offsettype-offset) | An integral offset in texels from the sampling location in the texture. |
| [`float lodClamp`](#float-lodclamp) | A value to clamp sample LOD values to. |

Types that depend on texture object:

| TextureObject | [`<CoordType>`](#coordtype-coord) | [`<OffsetType>`](#offsettype-offset) |
| --- | --- | --- |
| `Texture1D` | `float` | `int` |
| `Texture1DArray` | `float2` | `int` |
| `Texture2D` | `float2` | `int2` |
| `Texture2DArray` | `float3` | `int2` |
| `Texture3D` | `float3` | `int3` |

### `Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset, float lodClamp, out uint status )`

Samples a texture with an optional value to clamp sample level-of-detail (LOD) values to, and returns status of the operation.

```syntax
<ElementType> <TextureObject>.Sample( SamplerState samp, <CoordType> coord, <OffsetType> offset, float lodClamp, out uint status );
```

| Parameter | Description |
| --------- | ----------- |
| [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| [`<OffsetType> offset`](#offsettype-offset) | An integral offset in texels from the sampling location in the texture. |
| [`float lodClamp`](#float-lodclamp) | A value to clamp sample LOD values to. |
| [`out uint status`](#out-uint-status) | The residency status of the operation. |

Types that depend on texture object:

| TextureObject | [`<CoordType>`](#coordtype-coord) | [`<OffsetType>`](#offsettype-offset) |
| --- | --- | --- |
| `Texture1D` | `float` | `int` |
| `Texture1DArray` | `float2` | `int` |
| `Texture2D` | `float2` | `int2` |
| `Texture2DArray` | `float3` | `int2` |
| `Texture3D` | `float3` | `int3` |

## Return Values

### `<ElementType>`

The texture's template type for the element, which may be a scalar or vector.
This provides the HLSL type for an element loaded from a texture.
The format stored in the resource is based on the texture resource view's DXGI_FORMAT,
which will determine how data is translated into the type specified in HLSL.

## Parameters

| Parameter | Description |
| --------- | ----------- |
| [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| [`<OffsetType> offset`](#offsettype-offset) | An integral offset in texels from the sampling location in the texture. |
| [`float lodClamp`](#float-lodclamp) | A value to clamp sample LOD values to. |
| [`out uint status`](#out-uint-status) | The residency status of the operation. |

### `SamplerState samp`

A Sampler state. This is an object declared in an effect file that contains state assignments.

> My alternate text:
> SamplerState object that determines how sampling will take place.

Type: `SamplerState`

> TBD: Link to document describing SamplerState object.

### `<CoordType> coord`

The texture coordinates. The argument type is dependent on the texture-object type.

> My alternate text:
> The normalized (u,v,w) location of appropriate dimension for the texture, and an array index when applicable.

Type: Depends on TextureObject.  Types and component meanings are defined in the following table.

| TextureObject | `<CoordType>` | Normalized (u,v,w) location | Array Index |
| --------------- | ------------ | ------------ | ----------- |
| `Texture1D` | `float` | x | - |
| `Texture1DArray` | `float2` | x | y |
| `Texture2D` | `float2` | xy | - |
| `Texture2DArray` | `float3` | xy | z |
| `Texture3D` | `float3` | xyz | - |
| `TextureCube` | `float3` | xyz | - |
| `TextureCubeArray` | `float4` | xyz | w |

### `<OffsetType> offset`

An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the location before sampling. The texture offsets need to be static. The argument type is dependent on the texture-object type. For more info, see Applying texture coordinate offsets.

> My alternate text:
> An integral offset in texels from the sampling location in the texture.
> Each component must be an immediate value in the range of `[-8,7]` known at compile time.
> Cannot be used with TextureCube or TextureCubeArray objects.

Type: Depends on TextureObject.  Types and component meanings are defined in the following table.

| TextureObject | `<OffsetType>` | Integer offset in texels |
| --------------- | ------------ | ------------ |
| `Texture1D` | `int` | x |
| `Texture1DArray` | `int` | x |
| `Texture2D` | `int2` | xy |
| `Texture2DArray` | `int2` | xy |
| `Texture3D` | `int3` | xyz |

### `float lodClamp`

A value to clamp sample LOD values to. For example, if you pass 2.0f for the clamp value, you ensure that no individual sample accesses a mip level less than 2.0f.

Type: float

### `out uint status`

The residency status of the operation. You can't access the status directly; instead, pass the status to the CheckAccessFullyMapped intrinsic function. CheckAccessFullyMapped returns TRUE if all values from the corresponding Sample, Gather, or Load operation accessed mapped tiles in a tiled resource. If any values were taken from an unmapped tile, CheckAccessFullyMapped returns FALSE.

Type: uint
