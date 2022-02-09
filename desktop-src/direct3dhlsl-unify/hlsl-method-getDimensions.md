# GetDimensions

Gets texture size information.

```syntax
void Texture1D<ElementType>::GetDimensions(
      in  uint  mipLevel,
      out uint  width,
      out uint  numberOfLevels );

out Texture1DArray<ElementType>::GetDimensions(
      in  uint  mipLevel,
      out uint  width,
      out uint  elements,
      out uint  numberOfLevels );

void Texture2D<ElementType>::GetDimensions(
      in  uint  mipLevel,
      out uint  width,
      out uint  height,
      out uint  numberOfLevels );

void Texture2DArray<ElementType>::GetDimensions(
      in  uint  mipLevel,
      out uint  width,
      out uint  height,
      out uint  elements,
      out uint  numberOfLevels );

void Texture3D<ElementType>::GetDimensions(
      in  uint  mipLevel,
      out uint  width,
      out uint  height,
      out uint  depth,
      out uint  numberOfLevels );

void Texture2DMS<ElementType>::GetDimensions(
      out uint  width,
      out uint  height,
      out uint  numberOfSamples );

void Texture2DMSArray<ElementType>::GetDimensions(
      out uint  width,
      out uint  height,
      out uint  elements,
      out uint  numberOfSamples );
```

| Parameter | Description |
| - | - |
| in [`uint mipLevel`](#uint-mipLevel) | A zero-based index that identifies the mipmap level. If this argument is not used, the first mip level is assumed. |
| out [`uint width`](#uint-width) | The texture width, in texels. |
| out [`uint numberOfLevels`](#uint-numberOfLevels) | The number of mipmap levels. |
| out [`uint elements`](#uint-elements) | The number of elements in an array. |
| out [`uint height`](#uint-height) | The texture height, in texels. |
| out [`uint depth`](#uint-depth) | The texture depth, in texels. |
| out [`uint numberOfSamples`](#uint-numberOfSamples) | The number of samples. |

<b>Example</b>

```HLSL
// None.
```

## Return Value

None.

## Parameters

### `uint mipLevel`

A zero-based index that identifies the mipmap level. If this argument is not used, the first mip level is assumed.

### `uint width`

The texture width, in texels.

### `uint numberOfLevels`

The number of mipmap levels.

### `uint elements`

The number of elements in an array.

### `uint height`

The texture height, in texels.

### `uint depth`

The texture depth, in texels.

### `uint numberOfSamples`

The number of samples.

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