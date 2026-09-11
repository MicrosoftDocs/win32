---
title: SV_Barycentrics
description: Describes the system-value semantic that provides barycentric coordinates to pixel shaders in Shader Model 6.1 and later.
ms.topic: reference
ms.date: 08/12/2026
keywords:
- SV_Barycentrics HLSL
topic_type:
- apiref
api_name:
- SV_Barycentrics
api_type:
- NA
---

# SV_Barycentrics

Barycentric coordinates define a location within a geometric primitive such as a triangle or line. In Shader Model 6.1 and later, a pixel shader can use `SV_Barycentrics` to read the barycentric coordinates of the current pixel relative to the primitive.

The shader can use these coordinates for custom attribute interpolation, including higher-order interpolation, custom unpacking, and interpolation at application-defined precision. `SV_Barycentrics` provides the weights independently from the per-vertex attributes to which the weights are applied.

## System-generated barycentric coordinates

Declare `SV_Barycentrics` as a three-component, 32-bit floating-point pixel shader input:

```hlsl
float4 PSMain(float3 barycentrics : SV_Barycentrics) : SV_Target
{
    return float4(barycentrics, 1.0f);
}
```

The components are the barycentric weights of the current pixel relative to the vertices of the original API primitive before clipping. An `SV_Barycentrics` input doesn't consume pixel shader signature storage.

The three values aren't guaranteed to add up to exactly 1.0 in floating-point arithmetic. A shader that requires this property can reconstruct one coordinate from the other two:

```hlsl
barycentrics.z = 1.0f - barycentrics.x - barycentrics.y;
```

Individual weights aren't necessarily in the range 0 through 1. Screen-space barycentrics, screen-space quads, and external triangles can produce values outside that range.

For triangle primitives, all three weights typically have nonzero values. For line primitives, the third weight, `barycentrics.z`, is exactly 0.0. A shader can therefore evaluate a three-component barycentric sum for either triangles or lines.

### Interpolation modes

Barycentric coordinates support perspective-correct or `noperspective` (affine, screen-space) interpolation, with optional `centroid` or `sample` adjustment. The following pixel shader input declarations show the available combinations:

```syntax
// Perspective-correct barycentrics (the default).
linear float3 baryLinear : SV_Barycentrics;

// Centroid-adjusted affine barycentrics.
centroid noperspective float3 baryAffine : SV_Barycentrics;

// Sample-frequency affine barycentrics. Forces the shader to run at sample rate.
sample noperspective float3 baryAffineSample : SV_Barycentrics;
```

The `nointerpolation` modifier isn't allowed on an `SV_Barycentrics` input.

A pixel shader can declare at most two `SV_Barycentrics` inputs: one perspective-correct and one `noperspective`. Use distinct semantic indices 0 and 1:

```hlsl
float4 PSMain(
    float3 perspectiveWeights : SV_Barycentrics0,
    noperspective float3 affineWeights : SV_Barycentrics1) : SV_Target
{
    return float4(perspectiveWeights.xy, affineWeights.xy);
}
```

### Coordinate ordering

For a triangle whose vertices appear in the API stream as A, B, and C, the `x`, `y`, and `z` components contain the weights for A, B, and C, respectively. The `x` component corresponds to the provoking vertex.

Triangle strips reverse two vertices of every other triangle to maintain consistent winding. For example, the first two triangles of a strip with vertices 0, 1, 2, and 3 use the following component order:

| Triangle | `x` | `y` | `z` | Provoking vertex |
|-|-|-|-|-|
| 0 | 0 | 1 | 2 | 0 |
| 1 | 1 | 3 | 2 | 1 |

The second triangle swaps the weights for vertices 2 and 3 relative to their API stream order.

## Per-vertex attributes

To perform custom interpolation, declare the attribute with `nointerpolation`, and use `GetAttributeAtVertex` to retrieve its value at each primitive vertex:

```syntax
<attributeType> GetAttributeAtVertex(
    nointerpolation <attributeType> attribute,
    uint vertexIndex);
```

`vertexIndex` is in the range 0 through 2. The attribute must be a pixel shader input declared with `nointerpolation`. Implementations preserve every bit of these attributes across the vertex, domain, or geometry shader to pixel shader interface, so applications can use them as sets of 32-bit fields with application-defined interpretation.

The following example performs perspective-correct interpolation of a color:

```hlsl
enum VertexIndex
{
    First = 0,
    Second = 1,
    Third = 2
};

float3 PSMain(
    float3 barycentrics : SV_Barycentrics,
    nointerpolation float3 color : COLOR) : SV_Target
{
    float3 color0 = GetAttributeAtVertex(color, VertexIndex::First);
    float3 color1 = GetAttributeAtVertex(color, VertexIndex::Second);
    float3 color2 = GetAttributeAtVertex(color, VertexIndex::Third);

    return barycentrics.x * color0
         + barycentrics.y * color1
         + barycentrics.z * color2;
}
```

The vertex indices use the same ordering as the barycentric weights. Vertex index 0 corresponds to `barycentrics.x` and to the provoking vertex. Consequently, a shader can read attributes directly from vertex data and interpolate them consistently with the fixed-function interpolator.

The `nointerpolation` modifier can't be combined with `centroid` or `sample` on the same parameter.

## Interaction with clipping

Per-vertex attributes read by `GetAttributeAtVertex` aren't clipped. The pixel shader receives their values as output by the last geometry pipeline stage, including values for vertices outside the view frustum or behind the `W = 0` plane in clip space.

The barycentric coordinates remain relative to the original API primitive before clipping.

## Wireframe mode

With `D3D12_FILL_MODE_WIREFRAME`, barycentric coordinates follow the input vertex order. A coordinate on a wireframe triangle typically has one zero component and two nonzero components, but the zero component isn't necessarily `z`.

## Hardware support

To check support, call [**ID3D12Device::CheckFeatureSupport**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport) with `D3D12_FEATURE_D3D12_OPTIONS3` and inspect [**D3D12_FEATURE_DATA_D3D12_OPTIONS3::BarycentricsSupported**](/windows/win32/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options3).

## Related topics

- [HLSL Shader Model 6.1](hlsl-shader-model-6-1-features-for-direct3d-12.md)
- [Semantics](dx-graphics-hlsl-semantics.md)
