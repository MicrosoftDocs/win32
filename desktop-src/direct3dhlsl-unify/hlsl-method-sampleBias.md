# SampleBias Method

Samples a texture, after applying the bias value to the mipmap level.

Method Signatures vary per supported TextureObject type:

```syntax
ElementType Texture1D<ElementType>::SampleBias(
      in  SamplerState  samp,
      in  float         location,
      in  float         bias,
      in  int           offset,
   [, in  float         clamp ]
   [, out uint          status ] );

ElementType Texture1DArray<ElementType>::SampleBias(
      in  SamplerState  samp,
      in  float2        location,
      in  float         bias,
      in  int           offset,
   [, in  float         clamp ]
   [, out uint          status ] );

ElementType Texture2D<ElementType>::SampleBias(
      in  SamplerState  samp,
      in  float2        location,
      in  float         bias,
      in  int2          offset,
   [, in  float         clamp ]
   [, out uint          status ] );

ElementType Texture2DArray<ElementType>::SampleBias(
      in  SamplerState  samp,
      in  float3        location,
      in  float         bias,
      in  int2          offset,
   [, in  float         clamp ]
   [, out uint          status ] );

ElementType Texture3D<ElementType>::SampleBias(
      in  SamplerState  samp,
      in  float3        location,
      in  float         bias,
      in  int3          offset,
   [, in  float         clamp ]
   [, out uint          status ] );

ElementType TextureCube<ElementType>::SampleBias(
      in  SamplerState  samp,
      in  float3        location,
      in  float         bias,
   [, in  float         clamp ]
   [, out uint          status ] );

ElementType TextureCubeArray<ElementType>::SampleBias(
      in  SamplerState  samp,
      in  float4        location,
      in  float         bias,
   [, in  float         clamp ]
   [, out uint          status ] );
```

| Parameter | Description |
| - | - |
| in [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| in [`<LocationType> location`](#locationtype-location) | The texture coordinates. This method uses a 0-based coordinate system and not a 0.0-1.0 UV system. |
| in [`float bias`](#float-bias) | The bias value, which is a floating-point number between -16.0 and 15.99, is applied to a mip level before sampling. |
| in [`<OffsetType> offset`](#offsettype-offset) | The offset applied to the texture coordinates before sampling. |
| \[ in [`float clamp`](#float-clamp) \] | An optional value to clamp sample LOD values to. For example, if you pass 2.0f for the clamp value, you ensure that no individual sample accesses a mip level less than 2.0f. |
| \[ out [`uint status`](#uint-status) \] | The status of the operation. You can't access the status directly; instead, pass the status to the CheckAccessFullyMapped intrinsic function. CheckAccessFullyMapped returns TRUE if all values from the corresponding Sample, Gather, or Load operation accessed mapped tiles in a tiled resource. If any values were taken from an unmapped tile, CheckAccessFullyMapped returns FALSE. |

Types that depend on texture object:

| TextureObject | [`<LocationType>`](#locationtype-location) | [`<OffsetType>`](#offsettype-offset) |
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
// N/A
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

### `<LocationType> location`

The texture coordinates.  The argument type is dependent on the texture-object type.

| TextureObject | `<LocationType>` | x,y,z texel location | Array Index |
| --------------- | ------------ | ------------ | ----------- |
| `Texture1D` | `float` | x | - |
| `Texture1DArray` | `float2` | x | y |
| `Texture2D` | `float2` | xy | - |
| `Texture2DArray` | `float3` | xy | z |
| `Texture3D` | `float3` | xyz | - |
| `TextureCube` | `float3` | xyz | - |
| `TextureCubeArray` | `float4` | xyz | w |

### `float bias`

The bias value, which is a floating-point number between -16.0 and 15.99, is applied to a mip level before sampling.

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

### `float clamp`

An optional value to clamp sample LOD values to. For example, if you pass 2.0f for the clamp value, you ensure that no individual sample accesses a mip level less than 2.0f.

### `uint status`

The status of the operation. You can't access the status directly; instead, pass the status to the CheckAccessFullyMapped intrinsic function. CheckAccessFullyMapped returns TRUE if all values from the corresponding Sample, Gather, or Load operation accessed mapped tiles in a tiled resource. If any values were taken from an unmapped tile, CheckAccessFullyMapped returns FALSE.

## Remarks

None.

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