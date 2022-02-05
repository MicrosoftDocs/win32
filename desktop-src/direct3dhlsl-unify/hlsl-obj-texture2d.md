# HLSL Texture2D Object

Object for accessing a read-only 2D texture shader resource view.  See [SRV Textures](hlsl-resource-objects.md#srv-textures).
A template argument indicates the data type to use in HLSL for the texture element.
Textures are typed resources, so a data conversion step will translate between the DXGI_FORMAT and the element type declared in HLSL.

```HLSL
// prototype
template<typename ElementType = float4> class Texture2D;

// example declarations:
Texture2D ColorTexture;
Texture2D<float> DepthTexture;
```

## Methods

| Method | Description |
| - | - |
| [operators](hlsl-texture-operators.md) | Access texture elements using `operator[]` and `.mips[][]` syntax. |
| [Load](hlsl-texture-load.md) | Load a texture element using an integer texel location. |
| [Sample](hlsl-method-sample.md) | Samples a texture. |
| [SampleCmp](hlsl-method-samplecmp.md) | Samples a texture and returns the comparison against a provided value. |
| [Gather, GatherRed, GatherGreen, GatherBlue, GatherAlpha](hlsl-method-gather.md) | Gather four samples of one component that would be used for bilinear filtering when sampling a texture. |
| [GatherCmp, GatherCmpRed, GatherCmpGreen, GatherCmpBlue, GatherCmpAlpha](hlsl-method-gathercmp.md) | Gather four samples of one component that would be used for bilinear filtering and return each comparison against a provided value. |
