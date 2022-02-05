# Sample Method

Samples a texture with optional parameters for: immediate offset, level of detail clamp, residency status output.  Cube textures do not support immediate offsets.

Method Signatures vary per supported TextureObject type:

```syntax
ElementType Texture1D<ElementType>::Sample(
      in  SamplerState  samp,
      in  float         coord
   [, in  int           offset
   [, in  float         lodClamp
   [, out uint          status ] ] ]
);

ElementType Texture1DArray<ElementType>::Sample(
      in  SamplerState  samp,
      in  float2        coord
   [, in  int           offset
   [, in  float         lodClamp
   [, out uint          status ] ] ] );

ElementType Texture2D<ElementType>::Sample(
      in  SamplerState  samp,
      in  float2        coord
   [, in  int2          offset
   [, in  float         lodClamp
   [, out uint          status ] ] ] );

ElementType Texture2DArray<ElementType>::Sample(
      in  SamplerState  samp,
      in  float3        coord
   [, in  int2          offset
   [, in  float         lodClamp
   [, out uint          status ] ] ] );

ElementType Texture3D<ElementType>::Sample(
      in  SamplerState  samp,
      in  float3        coord
   [, in  int3          offset
   [, in  float         lodClamp
   [, out uint          status ] ] ] );

ElementType Texture1D<ElementType>::Sample(
      in  SamplerState  samp,
      in  float         coord
   [, in  int           offset
   [, in  float         lodClamp
   [, out uint          status ] ] ] );

ElementType TextureCube<ElementType>::Sample(
      in  SamplerState  samp,
      in  float3        coord
   [, in  float         lodClamp
   [, out uint          status ] ] ] );

ElementType TextureCubeArray<ElementType>::Sample(
      in  SamplerState  samp,
      in  float4        coord
   [, in  float         lodClamp
   [, out uint          status ] ] ] );
```

| Parameter | Description |
| - | - |
| in [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| in [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| \[ in [`<OffsetType> offset`](#offsettype-offset) \] | An integral offset in texels from the sampling location in the texture. |
| \[ in [`float lodClamp`](#float-lodclamp) \] | A value to clamp sample LOD values to. |
| \[ out [`uint status`](#out-uint-status) \] | The residency status of the operation. |

Types that depend on texture object:

| TextureObject | [`<CoordType>`](#coordtype-coord) | [`<OffsetType>`](#offsettype-offset) |
| --- | --- | --- |
| `Texture1D` | `float` | `int` |
| `Texture1DArray` | `float2` | `int` |
| `Texture2D` | `float2` | `int2` |
| `Texture2DArray` | `float3` | `int2` |
| `Texture3D` | `float3` | `int3` |
| `TextureCube` | `float3` | N/A |
| `TextureCubeArray` | `float4` | N/A |

<b>Example</b>

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

## Return Value

The texture's template type for the element, which may be a scalar or vector.
This provides the HLSL type for an element loaded from a texture.
The format stored in the resource is based on the texture resource view's DXGI_FORMAT,
which will determine how data is translated into the type specified in HLSL.

## Parameters

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

## Remarks

Texture sampling uses the texel position to look up a texel value. An offset can be applied to the position before lookup. The sampler state contains the sampling and filtering options. This method can be invoked within a pixel shader, but it is not supported in a vertex shader or a geometry shader.

Use an offset only at an integer miplevel; otherwise, you may get different results depending on hardware implementation or driver settings.

### Calculating texel positions

Texture coordinates are floating-point values that reference texture data, which is also known as normalized texture space. Address wrapping modes are applied in this order (texture coordinates + offsets + wrap mode) to modify texture coordinates outside the [0...1] range.

For texture arrays, an additional value in the location parameter specifies an index into a texture array. This index is treated as a scaled float value (instead of the normalized space for standard texture coordinates). The conversion to an integer index is done in the following order (float + round-to-nearest-even integer + clamp to the array range).

### Applying texture coordinate offsets

The offset parameter modifies the texture coordinates, in texel space. Even though texture coordinates are normalized floating-point numbers, the offset applies an integer offset. Also note that the texture offsets need to be static.

The data format returned is determined by the texture format. For example, if the texture resource was defined with the DXGI_FORMAT_A8B8G8R8_UNORM_SRGB format, the sampling operation converts sampled texels from gamma 2.0 to 1.0, filter, and writes the result as a floating-point value in the range [0..1].

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
