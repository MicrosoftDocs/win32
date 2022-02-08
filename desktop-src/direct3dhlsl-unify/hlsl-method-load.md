# Load Method

Reads texel data without any filtering or sampling.

```syntax
ElementType Texture1D<ElementType>::Load(
      in  int2          location
      in  int           offset
   [, out uint          status ] );

ElementType Texture1DArray<ElementType>::Load(
      in  int3          location
      in  int           offset
   [, out uint          status ] );

ElementType Texture2D<ElementType>::Load(
      in  int3          location,
      in  int2          offset
   [, out uint          status ] );

ElementType Texture2DArray<ElementType>::Load(
      in  int4          location,
      in  int2          offset
   [, out uint          status ] );

ElementType Texture2DMS<ElementType>::Load(
      in  int2          location,
      in  int           sampleIndex,
   [, in  int2          offset ]
   [, out uint          status ] );

ElementType Texture2DMSArray<ElementType>::Load(
      in  int3          location,
      in  int           sampleIndex,
   [, in  int2          offset ]
   [, out uint          status ] );

ElementType Texture3D<ElementType>::Load(
      in  int4          location,
      in  int3          offset
   [, out uint          status ] );
```

| Parameter | Description |
| - | - |
| in [`<LocationType> location`](#locationtype-location) | The texture coordinates. This method uses a 0-based coordinate system and not a 0.0-1.0 UV system. |
| in [`<OffsetType> offset`](#offsettype-offset) | The offset applied to the texture coordinates before sampling. |
| \[ in [`int sampleIndex`](#int-sampleindex) \] | The sample index. |
| \[ out [`uint status`](#uint-status) \] | The status of the operation. You can't access the status directly; instead, pass the status to the CheckAccessFullyMapped intrinsic function. CheckAccessFullyMapped returns TRUE if all values from the corresponding Sample, Gather, or Load operation accessed mapped tiles in a tiled resource. If any values were taken from an unmapped tile, CheckAccessFullyMapped returns FALSE. |

Types that depend on texture object:

| TextureObject | [`<LocationType>`](#locationtype-location) | [`<OffsetType>`](#offsettype-offset) |
| --- | --- | --- |
| `Texture1D` | `int2` | `int` |
| `Texture1DArray` | `int3` | `int` |
| `Texture2D` | `int3` | `int2` |
| `Texture2DArray` | `int4` | `int2` |
| `Texture2DMS` | `int2` | `int2` |
| `Texture2DMSArray` | `int2` | `int2` |
| `Texture3D` | `int4` | `int3` |

<b>Example</b>

```HLSL
// Object Declarations
Buffer<float4> g_ParticleBuffer;

// Shader body calling the intrinsic function
float4 PSPaint(PSQuadIn input) : SV_Target
{       
    ... 
    for( int i=g_ParticleStart; i<g_NumParticles; i+=g_ParticleStep )
    {
        ... 
        // load the particle
        float4 particlePos = g_ParticleBuffer.Load( i*4 );
        float4 particleColor = g_ParticleBuffer.Load( (i*4) + 2 );
        ...     
    }
    ...
}   
```

## Return Value

The return type matches the type in the Object declaration. For example, a Texture2D object that was declared as "Texture2d<uint4> myTexture;" has a return value of type uint4.

## Parameters

### `<LocationType> location`

The texture coordinates; the last component specifies the mipmap level. This method uses a 0-based coordinate system and not a 0.0-1.0 UV system. The argument type is dependent on the texture-object type.

| TextureObject | `<LocationType>` | x,y,z texel location | Array Index | Mip Level |
| --------------- | ------------ | ------------ | ----------- | ----------- |
| `Texture1D` | `int2` | x | - | y |
| `Texture1DArray` | `int3` | x | y | z |
| `Texture2D` | `int3` | xy | - | z |
| `Texture2DArray` | `int4` | xy | z | w |
| `Texture2DMS` | `int2` | xy | - | - |
| `Texture2DMSArray` | `int3` | xy | z | - |
| `Texture3D` | `int4` | xyz | - | z |

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
| `Texture2DMS` | `int2` | xy |
| `Texture2DMSArray` | `int2` | xy |
| `Texture3D` | `int3` | xyz |

### `int sampleIndex`

The sample index.

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