# Gather Method

Gets the four samples that would be used for bilinear interpolation when sampling a texture.

### `All Channels`

```syntax
ElementType Texture2D<ElementType>::Gather(
      in  SamplerState  samp,
      in  float2        coord,
      in  int2          offset,
   [, out uint          status ] );

ElementType Texture2DArray<ElementType>::Gather(
      in  SamplerState  samp,
      in  float3        coord,
      in  int2          offset,
   [, out uint          status ] );

ElementType TextureCube<ElementType>::Gather(
      in  SamplerState  samp,
      in  float3        coord,
   [, out uint          status ] );

ElementType TextureCubeArray<ElementType>::Gather(
      in  SamplerState  samp,
      in  float4        coord,
   [, out uint          status ] );
```

### `Red Channel`

```syntax
ElementType Texture2D<ElementType>::GatherRed(
      in  SamplerState  samp,
      in  float2        coord,
      in  int2          offset,
   [, in  int2          offset2]
   [, in  int2          offset3]
   [, in  int2          offset4]   
   [, out uint          status ] );

ElementType Texture2DArray<ElementType>::GatherRed(
      in  SamplerState  samp,
      in  float3        coord,
      in  int2          offset,
   [, in  int2          offset2]
   [, in  int2          offset3]
   [, in  int2          offset4]
   [, out uint          status ] );

ElementType TextureCube<ElementType>::GatherRed(
      in  SamplerState  samp,
      in  float3        coord,
   [, out uint          status ] );

ElementType TextureCubeArray<ElementType>::GatherRed(
      in  SamplerState  samp,
      in  float4        coord,
   [, out uint          status ] );
```

### `Green Channel`

```syntax
ElementType Texture2D<ElementType>::GatherGreen(
      in  SamplerState  samp,
      in  float2        coord,
      in  int2          offset,
   [, in  int2          offset2]
   [, in  int2          offset3]
   [, in  int2          offset4]   
   [, out uint          status ] );

ElementType Texture2DArray<ElementType>::GatherGreen(
      in  SamplerState  samp,
      in  float3        coord,
      in  int2          offset,
   [, in  int2          offset2]
   [, in  int2          offset3]
   [, in  int2          offset4]
   [, out uint          status ] );

ElementType TextureCube<ElementType>::GatherGreen(
      in  SamplerState  samp,
      in  float3        coord,
   [, out uint          status ] );

ElementType TextureCubeArray<ElementType>::GatherGreen(
      in  SamplerState  samp,
      in  float4        coord,
   [, out uint          status ] );
```

### `Blue Channel`

```syntax
ElementType Texture2D<ElementType>::GatherBlue(
      in  SamplerState  samp,
      in  float2        coord,
      in  int2          offset,
   [, in  int2          offset2]
   [, in  int2          offset3]
   [, in  int2          offset4]   
   [, out uint          status ] );

ElementType Texture2DArray<ElementType>::GatherBlue(
      in  SamplerState  samp,
      in  float3        coord,
      in  int2          offset,
   [, in  int2          offset2]
   [, in  int2          offset3]
   [, in  int2          offset4]
   [, out uint          status ] );

ElementType TextureCube<ElementType>::GatherBlue(
      in  SamplerState  samp,
      in  float3        coord,
   [, out uint          status ] );

ElementType TextureCubeArray<ElementType>::GatherBlue(
      in  SamplerState  samp,
      in  float4        coord,
   [, out uint          status ] );
```

### `Alpha Channel`

```syntax
ElementType Texture2D<ElementType>::GatherAlpha(
      in  SamplerState  samp,
      in  float2        coord,
      in  int2          offset,
   [, in  int2          offset2]
   [, in  int2          offset3]
   [, in  int2          offset4]   
   [, out uint          status ] );

ElementType Texture2DArray<ElementType>::GatherAlpha(
      in  SamplerState  samp,
      in  float3        coord,
      in  int2          offset,
   [, in  int2          offset2]
   [, in  int2          offset3]
   [, in  int2          offset4]
   [, out uint          status ] );

ElementType TextureCube<ElementType>::GatherAlpha(
      in  SamplerState  samp,
      in  float3        coord,
   [, out uint          status ] );

ElementType TextureCubeArray<ElementType>::GatherAlpha(
      in  SamplerState  samp,
      in  float4        coord,
   [, out uint          status ] );
```

| Parameter | Description |
| - | - |
| in [`SamplerState samp`](#samplerstate-samp) | SamplerState object that determines how sampling will take place. |
| in [`<CoordType> coord`](#coordtype-coord) | The texture coordinates. |
| in [`<OffsetType> offset`](#offsettype-offset) | The offset applied to the texture coordinates before sampling. |
| \[ out [`uint status`](#uint-status) \] | The status of the operation. You can't access the status directly; instead, pass the status to the CheckAccessFullyMapped intrinsic function. CheckAccessFullyMapped returns TRUE if all values from the corresponding Sample, Gather, or Load operation accessed mapped tiles in a tiled resource. If any values were taken from an unmapped tile, CheckAccessFullyMapped returns FALSE. |

Types that depend on texture object:

| TextureObject | [`<CoordType>`](#coordtype-coord) | [`<OffsetType>`](#offsettype-offset) |
| --- | --- | --- |
| `Texture2D` | `float2` | `int2` |
| `Texture2DArray` | `float3` | `int2` |
| `TextureCube` | `float3` | N/A |
| `TextureCubeArray` | `float4` | N/A |

<b>Example</b>

```HLSL
Texture2D<int1> Tex2d;
Texture2DArray<int2> Tex2dArray;
TextureCube<int3> TexCube;
TextureCubeArray<float2> TexCubeArray;

SamplerState s;

int4 main (float4 f : SV_Position) : SV_Target
{
    int2 iOffset = int2(2,3);

    int4 i1 = Tex2d.Gather(s, f.xy);
    int4 i2 = Tex2d.Gather(s, f.xy, iOffset);

    int4 i3 = Tex2dArray.Gather(s, f.xyz);
    int4 i4 = Tex2dArray.Gather(s, f.xyz, iOffset);

    int4 i5 = TexCube.Gather(s, f.xyzw);

    float4 f6 = TexCubeArray.Gather(s, f.xyzw);

    return i1+i2+i3+i4+i5+int4(i6);
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

The texture coordinates.  The argument type is dependent on the texture-object type.

| TextureObject | `<CoordType>` | x,y,z texel coord | Array Index |
| --------------- | ------------ | ------------ | ----------- |
| `Texture2D` | `float2` | xy | - |
| `Texture2DArray` | `float3` | xy | z |
| `TextureCube` | `float3` | xyz | - |
| `TextureCubeArray` | `float4` | xyz | w |

### `<OffsetType> offset`

An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the coord before sampling. The texture offsets need to be static. The argument type is dependent on the texture-object type. For more info, see Applying texture coordinate offsets.

> My alternate text:
> An integral offset in texels from the sampling coord in the texture.
> Each component must be an immediate value in the range of `[-8,7]` known at compile time.
> Cannot be used with TextureCube or TextureCubeArray objects.

Type: Depends on TextureObject.  Types and component meanings are defined in the following table.

| TextureObject | `<OffsetType>` | Integer offset in texels |
| --------------- | ------------ | ------------ |
| `Texture2D` | `int2` | xy |
| `Texture2DArray` | `int2` | xy |

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