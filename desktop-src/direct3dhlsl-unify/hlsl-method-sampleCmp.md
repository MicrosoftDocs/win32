# SampleCmp Method

Samples a texture and compares a single component against the specified comparison value.

Method Signatures vary per supported TextureObject type:

### `All Mip Levels`

```syntax
ElementType Texture1D<ElementType>::SampleCmp(
      in  SamplerComparisonState  samp,
      in  float2                  coord,
      in  float                   compareValue,
      in  int                     offset,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType Texture1DArray<ElementType>::SampleCmp(
      in  SamplerComparisonState  samp,
      in  float3                  coord,
      in  float                   compareValue,
      in  int                     offset,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType Texture2D<ElementType>::SampleCmp(
      in  SamplerComparisonState  samp,
      in  float3                  coord,
      in  float                   compareValue,
      in  int2                    offset,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType Texture2DArray<ElementType>::SampleCmp(
      in  SamplerComparisonState  samp,
      in  float4                  coord,
      in  float                   compareValue,
      in  int2                    offset,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType TextureCube<ElementType>::SampleCmp(
      in  SamplerComparisonState  samp,
      in  float3                  coord,
      in  float                   compareValue,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType TextureCubeArray<ElementType>::SampleCmp(
      in  SamplerComparisonState  samp,
      in  float4                  coord,
      in  float                   compareValue,
   [, in  float                   clamp ]
   [, out uint                    status ] );
```

### `Mip Level Zero`

```syntax
ElementType Texture1D<ElementType>::SampleCmpLevelZero(
      in  SamplerComparisonState  samp,
      in  float                   coord,
      in  float                   compareValue,
      in  int                     offset,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType Texture1DArray<ElementType>::SampleCmpLevelZero(
      in  SamplerComparisonState  samp,
      in  float2                  coord,
      in  float                   compareValue,
      in  int                     offset,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType Texture2D<ElementType>::SampleCmpLevelZero(
      in  SamplerComparisonState  samp,
      in  float2                  coord,
      in  float                   compareValue,
      in  int2                    offset,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType Texture2DArray<ElementType>::SampleCmpLevelZero(
      in  SamplerComparisonState  samp,
      in  float3                  coord,
      in  float                   compareValue,
      in  int2                    offset,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType TextureCube<ElementType>::SampleCmpLevelZero(
      in  SamplerComparisonState  samp,
      in  float2                  coord,
      in  float                   compareValue,
   [, in  float                   clamp ]
   [, out uint                    status ] );

ElementType TextureCubeArray<ElementType>::SampleCmpLevelZero(
      in  SamplerComparisonState  samp,
      in  float3                  coord,
      in  float                   compareValue,
   [, in  float                   clamp ]
   [, out uint                    status ] );
```

| Parameter | Description |
| - | - |
| in [`SamplerComparisonState samp`](#samplercomparisonstate-samp) | A sampler-comparison state, which is the sampler state plus a comparison state (a comparison function and a comparison filter). See the sampler type for details and an example. |
| in [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| in [`float compareValue`](#float-comparevalue) | A floating-point value to use as a comparison value. |
| in [`<OffsetType> offset`](#offsettype-offset) | The offset applied to the texture coordinates before sampling. |
| \[ in [`float clamp`](#float-clamp) \] | An optional value to clamp sample LOD values to. For example, if you pass 2.0f for the clamp value, you ensure that no individual sample accesses a mip level less than 2.0f. |
| \[ out [`uint status`](#uint-status) \] | The status of the operation. You can't access the status directly; instead, pass the status to the CheckAccessFullyMapped intrinsic function. CheckAccessFullyMapped returns TRUE if all values from the corresponding Sample, Gather, or Load operation accessed mapped tiles in a tiled resource. If any values were taken from an unmapped tile, CheckAccessFullyMapped returns FALSE. |

Types that depend on texture object:

### `All Mip Levels`

| TextureObject | [`<CoordType>`](#coordtype-coord) | [`<OffsetType>`](#offsettype-offset) |
| --- | --- | --- |
| `Texture1D` | `float2` | `int` |
| `Texture1DArray` | `float3` | `int` |
| `Texture2D` | `float3` | `int2` |
| `Texture2DArray` | `float4` | `int2` |
| `TextureCube` | `float3` | N/A |
| `TextureCubeArray` | `float4` | N/A |

### `Mip Level Zero`

| TextureObject | [`<CoordType>`](#coordtype-coord) | [`<OffsetType>`](#offsettype-offset) |
| --- | --- | --- |
| `Texture1D` | `float` | `int` |
| `Texture1DArray` | `float2` | `int` |
| `Texture2D` | `float2` | `int2` |
| `Texture2DArray` | `float3` | `int2` |
| `TextureCube` | `float2` | N/A |
| `TextureCubeArray` | `float3` | N/A |

<b>Example</b>

```HLSL
// N/A
```

## Return Value

Returns a floating-point value in the range [0..1].

For each texel fetched (based on the sampler configuration of the filter mode), SampleCmp performs a comparison of the z value (3rd component of input) from the shader against the texel value (1 if the comparison passes; otherwise 0). SampleCmp then blends these 0 and 1 results for each texel together as in normal texture filtering (not an average) and returns the resulting [0..1] value to the shader.

## Parameters

### `SamplerComparisonState samp`

A sampler-comparison state, which is the sampler state plus a comparison state (a comparison function and a comparison filter). See the sampler type for details and an example.

### `<CoordType> coord`

The texture coordinates.  The argument type is dependent on the texture-object type.

#### `All Mip Levels`

| TextureObject | `<CoordType>` | x,y,z texel coord | Array Index | Mip Slice |
| --------------- | ------------ | ------------ | ----------- | ----------- |
| `Texture1D` | `float2` | x | - | y |
| `Texture1DArray` | `float3` | x | y | z |
| `Texture2D` | `float3` | xy | - | z |
| `Texture2DArray` | `float4` | xy | z | w |
| `TextureCube` | `float3` | xy | - | z |
| `TextureCubeArray` | `float4` | xy | z | w |

#### `Mip Level Zero`

| TextureObject | `<CoordType>` | x,y,z texel coord | Array Index |
| --------------- | ------------ | ------------ | ----------- |
| `Texture1D` | `float` | x | - |
| `Texture1DArray` | `float2` | x | y |
| `Texture2D` | `float2` | xy | - |
| `Texture2DArray` | `float3` | xy | z |
| `TextureCube` | `float2` | xy | - |
| `TextureCubeArray` | `float3` | xy | z |

### `float compareValue`

A floating-point value to use as a comparison value.

### `<OffsetType> offset`

An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the coord before sampling. The texture offsets need to be static. The argument type is dependent on the texture-object type. For more info, see Applying texture coordinate offsets.

> My alternate text:
> An integral offset in texels from the sampling coord in the texture.
> Each component must be an immediate value in the range of `[-8,7]` known at compile time.
> Cannot be used with TextureCube or TextureCubeArray objects.

Type: Depends on TextureObject.  Types and component meanings are defined in the following table.

| TextureObject | `<OffsetType>` | Integer offset in texels |
| --------------- | ------------ | ------------ |
| `Texture1D` | `int` | x |
| `Texture1DArray` | `int` | x |
| `Texture2D` | `int2` | xy |
| `Texture2DArray` | `int2` | xy |

### `float clamp`

An optional value to clamp sample LOD values to. For example, if you pass 2.0f for the clamp value, you ensure that no individual sample accesses a mip level less than 2.0f.

### `uint status`

The status of the operation. You can't access the status directly; instead, pass the status to the CheckAccessFullyMapped intrinsic function. CheckAccessFullyMapped returns TRUE if all values from the corresponding Sample, Gather, or Load operation accessed mapped tiles in a tiled resource. If any values were taken from an unmapped tile, CheckAccessFullyMapped returns FALSE.

## Remarks

Comparison filtering provides a basic filtering operation that is useful for percentage-closer-depth filtering.

When using this method on a floating-point resource (Instead of a signed-normalized or unsigned-normalized format), the comparison value is not automatically clamped between 0.0 and 1.0. Therefore, a manual clamp of the comparison value may be necessary for common shadowing techniques.

Use an offset only at an integer miplevel; otherwise, you may get different results depending on hardware implementation or driver settings.

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