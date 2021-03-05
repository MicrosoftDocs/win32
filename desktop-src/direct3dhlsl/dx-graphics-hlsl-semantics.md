---
title: Semantics
description: A semantic is a string attached to a shader input or output that conveys information about the intended use of a parameter.
ms.assetid: 6f5c504c-1940-4d1c-b594-a2132599376b
keywords:
- BINORMAL, semantics (DirectX HLSL)
- BLENDINDICES, semantics (DirectX HLSL)
- BLENDWEIGHT, semantics (DirectX HLSL)
- COLOR, semantics (DirectX HLSL)
- FOG, semantics (DirectX HLSL)
- POSITIONT, semantics (DirectX HLSL)
- PSIZE, semantics (DirectX HLSL)
- TANGENT, semantics (DirectX HLSL)
- TESSFACTOR, semantics (DirectX HLSL)
- TEXCOORD, semantics (DirectX HLSL)
- VFACE, semantics (DirectX HLSL)
- VPOS, semantics (DirectX HLSL)
- System-Value Semantics
- System Value Semantics
- ClipDistance, semantics (DirectX HLSL)
- Coverage, semantics (DirectX HLSL)
- CullDistance, semantics (DirectX HLSL)
- Depth, semantics (DirectX HLSL)
- InstanceID, semantics (DirectX HLSL)
- IsFrontFace, semantics (DirectX HLSL)
- Position, semantics (DirectX HLSL)
- PrimitiveID, semantics (DirectX HLSL)
- RenderTargetArrayIndex, semantics (DirectX HLSL)
- Target, semantics (DirectX HLSL)
- SampleIndex, semantics (DirectX HLSL)
- VertexID, semantics (DirectX HLSL)
- ViewportArrayIndex, semantics (DirectX HLSL)
- SV_ClipDistance, semantics (DirectX HLSL)
- SV_CullDistance, semantics (DirectX HLSL)
- SV_Depth, semantics (DirectX HLSL)
- SV_DepthGreaterEqual, semantics (DirectX HLSL)
- SV_DepthLessEqual, semantics (DirectX HLSL)
- SV_IsFrontFace, semantics (DirectX HLSL)
- SV_Position, semantics (DirectX HLSL)
- SV_RenderTargetArrayIndex, semantics (DirectX HLSL)
- SV_Target, semantics (DirectX HLSL)
- SV_ViewportArrayIndex, semantics (DirectX HLSL)
- SV_InstanceID, semantics (DirectX HLSL)
- SV_PrimitiveID, semantics (DirectX HLSL)
- SV_VertexID, semantics (DirectX HLSL)
- SV_Coverage, semantics (DirectX HLSL)
- SV_SampleIndex, semantics (DirectX HLSL)
- SV_InnerCoverage, semanitcs (DirectX HLSL)
- SV_StencilRef, semantics (DirectX HLSL)
- SV_GroupID, semantics (DirectX HLSL)
- SV_GroupThreadID, semantics (DirectX HLSL)
- SV_DispatchThreadID semantics (DirectX HLSL)
- SV_GroupIndex, semantics (DirectX HLSL)
- SV_OutputControlPointID, semantics (DirectX HLSL)
- SV_TessFactor, semantics (DirectX HLSL)
- SV_InsideTessFactor, semantics (DirectX HLSL)
- SV_DomainLocation, semantics (DirectX HLSL)
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Semantics

A semantic is a string attached to a shader input or output that conveys information about the intended use of a parameter. Semantics are required on all variables passed between shader stages. The syntax for adding a semantic to a shader variable is shown here ([Variable Syntax (DirectX HLSL)](dx-graphics-hlsl-variable-syntax.md)).

In general, data passed between pipeline stages is completely generic and is not uniquely interpreted by the system; arbitrary semantics are allowed which have no special meaning. Parameters (in Direct3D 10 and later) which contain these special semantics are referred to as [System-Value Semantics](#system-value-semantics).

## Semantics Supported in Direct3D 9 and Direct3D 10 and later

The following types of semantics are supported in both Direct3D 9 and Direct3D 10 and later.

- [Vertex Shader Semantics](#vertex-shader-semantics)
- [Pixel Shader Semantics](#pixel-shader-semantics)

### Vertex Shader Semantics

These semantics have meaning when attached to a vertex-shader parameter. These semantics are supported in both Direct3D 9 and Direct3D 10 and later.

| Input | Description | Type |
|-|-|-|
| BINORMAL\[n\] | Binormal | float4 |
| BLENDINDICES\[n\] | Blend indices | uint |
| BLENDWEIGHT\[n\] | Blend weights | float |
| COLOR\[n\] | Diffuse and specular color | float4 |
| NORMAL\[n\] | Normal vector | float4 |
| POSITION\[n\] | Vertex position in object space. | float4 |
| POSITIONT | Transformed vertex position. | float4 |
| PSIZE\[n\] | Point size | float |
| TANGENT\[n\] | Tangent | float4 |
| TEXCOORD\[n\] | Texture coordinates | float4 |
| Output | Description | Type |
| COLOR\[n\] | Diffuse or specular color | float4 |
| FOG | Vertex fog | float |
| POSITION\[n\] | Position of a vertex in homogenous space. Compute position in screen-space by dividing (x,y,z) by w. Every vertex shader must write out a parameter with this semantic. | float4 |
| PSIZE | Point size | float |
| TESSFACTOR\[n\] | Tessellation factor | float |

`n` is an optional integer between 0 and the number of resources supported. For example, POSITION0, TEXCOORD1, etc.

### Pixel Shader Semantics

These semantics have meaning when attached to a pixel-shader input parameter. These semantics are supported in both Direct3D 9 and Direct3D 10 and later.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Input</th>
<th>Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>COLOR[n]</td>
<td>Diffuse or specular color.</td>
<td>float4</td>
</tr>
<tr class="even">
<td>TEXCOORD[n]</td>
<td>Texture coordinates</td>
<td>float4</td>
</tr>
<tr class="odd">
<td>VFACE</td>
<td>Floating-point scalar that indicates a back-facing primitive. A negative value faces backwards, while a positive value faces the camera.
<blockquote>
[!Note]<br />
This semantic is available in <a href="dx-graphics-hlsl-sm3.md">Direct3D 9 Shader Model 3.0</a>. For Direct3D 10 and later, use <a href="#semantics-supported-only-for-direct3d-10-and-newer">SV_IsFrontFace</a> instead.
</blockquote>
<br/></td>
<td>float</td>
</tr>
<tr class="even">
<td>VPOS</td>
<td>The pixel location (x,y) in screen space. To convert a Direct3D 9 shader (that uses this semantic) to a Direct3D 10 and later shader, see <a href="#direct3d-9-vpos-and-direct3d-10-sv_position">Direct3D 9 VPOS and Direct3D 10 SV_Position</a>)</td>
<td>float2</td>
</tr>
<tr class="odd">
<td>Output</td>
<td>Description</td>
<td>Type</td>
</tr>
<tr class="even">
<td>COLOR[n]</td>
<td>Output color</td>
<td>float4</td>
</tr>
<tr class="odd">
<td>DEPTH[n]</td>
<td>Output depth</td>
<td>float</td>
</tr>
</tbody>
</table>

`n` is an optional integer between 0 and the number of resources supported. For example, PSIZE0, COLOR1, etc.

The COLOR semantic is only valid in shader compatibility mode (that is, when the shader is created using D3D10\_SHADER\_ENABLE\_BACKWARDS\_COMPATIBILITY).

## Semantics Supported Only for Direct3D 10 and Newer.

The following types of semantics have been newly introduced for Direct3D 10 and are not available to Direct3D 9.

- [System-Value Semantics](#system-value-semantics)

### System-Value Semantics

System-value semantics are new to Direct3D 10. All system-values begin with an SV\_ prefix, a common example is SV\_POSITION, which is interpreted by the rasterizer stage. The system-values are valid at other parts of the pipeline. For instance, SV\_Position can be specified as an input to a vertex shader as well as an output. Pixel shaders can only write to parameters with the SV\_Depth and SV\_Target system-value semantics.

Other system values (SV\_VertexID, SV\_InstanceID, SV\_IsFrontFace) can only be input into the first active shader in the pipeline that can interpret the particular value; after that the shader function must pass the values to subsequent stages.

SV\_PrimitiveID is an exception to this rule of only being input into the first active shader in the pipeline that can interpret the particular value; the hardware can provide the same ID value as input to the hull-shader stage, domain-shader stage, and after that whichever stage is the first enabled: geometry-shader stage or pixel-shader stage.

If tessellation is enabled, the hull-shader stage and domain-shader stage are present. For a given patch, the same PrimitiveID applies to the patch's hull-shader invocation, and all tessellated domain shader invocations. The same PrimitiveID also propagates to the next active stage; geometry-shader stage or pixel-shader stage if enabled.

If the geometry shader inputs SV\_PrimitiveID and because it can output zero or one or more primitives per invocation, the shader must program its own choice of SV\_PrimitiveID value for each output primitive if a subsequent pixel shader inputs SV\_PrimtiveID.

As another example, SV\_PrimitiveID cannot be interpreted by the vertex-shader stage because a vertex can be a member of multiple primitives.

These semantics have been added to Direct3D 10; they are not available in Direct3D 9.

System-value semantics for the rasterizer stage.

| System-Value Semantic | Description | Type |
|-|-|-|
| SV\_ClipDistance\[n\] | Clip distance data. SV\_ClipDistance values are each assumed to be a float32 signed distance to a plane. Primitive setup only invokes rasterization on pixels for which the interpolated plane distance(s) are >= 0. Multiple clip planes can be implemented simultaneously, by declaring multiple component(s) of one or more vertex elements as the SV\_ClipDistance. The combined clip and cull distance values are at most D3D\#\_CLIP\_OR\_CULL\_DISTANCE\_COUNT components in at most D3D\#\_CLIP\_OR\_CULL\_DISTANCE\_ELEMENT\_COUNT registers. Available to all shaders to be read or written to, except the vertex shader which can write the value but not take it as input.<br/> The **clipplanes** attribute works like SV\_ClipDistance but works on all hardware [feature level](../direct3d11/overviews-direct3d-11-devices-downlevel-intro.md) 9\_x and higher. For more info, see [User clip planes on feature level 9 hardware](./user-clip-planes-on-10level9.md).<br/> | float |
| SV\_CullDistance\[n\] | Cull distance data. When component(s) of vertex Element(s) are given this label, these values are each assumed to be a float32 signed distance to a plane. Primitives will be completely discarded if the plane distance(s) for all of the vertices in the primitive are < 0. Multiple cull planes can be used simultaneously, by declaring multiple component(s) of one or more vertex elements as the SV\_CullDistance. The combined clip and cull distance values are at most D3D\#\_CLIP\_OR\_CULL\_DISTANCE\_COUNT components in at most D3D\#\_CLIP\_OR\_CULL\_DISTANCE\_ELEMENT\_COUNT registers. Available to all shaders to be read or written to, except the vertex shader which can write the value but not take it as input.<br/> | float |
| SV\_Coverage | A mask that can be specified on input, output, or both of a pixel shader. <br/> For SV\_Coverage on a pixel shader, OUTPUT is supported on ps\_4\_1 or higher. <br/> For SV\_Coverage on a pixel shader, INPUT requires ps\_5\_0 or higher. <br/> | uint |
| SV\_Depth | Depth buffer data. Can be written by pixel shader. | float |
| SV\_DepthGreaterEqual | In a pixel shader, allows outputting depth, as long as it is greater than or equal to the value determined by the rasterizer. Enables adjusting depth without disabling early Z. | float |
| SV\_DepthLessEqual | In a pixel shader, allows outputting depth, as long as it is less than or equal to the value determined by the rasterizer. Enables adjusting depth without disabling early Z. | float |
| [SV\_DispatchThreadID](sv-dispatchthreadid.md) | Defines the global thread offset within the Dispatch call, per dimension of the group. Available as input to compute shader. (read only) | uint3 |
| [SV\_DomainLocation](sv-domainlocation.md) | Defines the location on the hull of the current domain point being evaluated. Available as input to the domain shader. (read only) | float2\|3 |
| [SV\_GroupID](sv-groupid.md) | Defines the group offset within a Dispatch call, per dimension of the dispatch call. Available as input to the compute shader. (read only) | uint3 |
| [SV\_GroupIndex](sv-groupindex.md) | Provides a flattened index for a given thread within a given group. Available as input to the compute shader. (read only) | uint |
| [SV\_GroupThreadID](sv-groupthreadid.md) | Defines the thread offset within the group, per dimension of the group. Available as input to the compute shader. (read only) | uint3 |
| [SV\_GSInstanceID](sv-gsinstanceid.md) | Defines the instance of the geometry shader. Available as input to the geometry shader. The instance is needed as a geometry shader can be invoked up to 32 times on the same geometry primitive. | uint |
| SV\_InnerCoverage | Represents underestimated conservative rasterization information (i.e. whether a pixel is guaranteed-to-be-fully covered). Can be read or written by the pixel shader. | |
| [SV\_InsideTessFactor](sv-insidetessfactor.md) | Defines the tessellation amount within a patch surface. Available in the hull shader for writing, and available in the domain shader for reading. | float\|float\[2\] |
| SV\_InstanceID | Per-instance identifier automatically generated by the runtime (see [Using System-Generated Values (Direct3D 10)](../direct3d11/d3d10-graphics-programming-guide-input-assembler-stage-using.md)). Available to all shaders. | |
| SV\_IsFrontFace | Specifies whether a triangle is front facing. For lines and points, IsFrontFace has the value true. The exception is lines drawn out of triangles (wireframe mode), which sets IsFrontFace the same way as rasterizing the triangle in solid mode. Can be written to by the geometry shader, and read by the pixel shader. | bool |
| [SV\_OutputControlPointID](sv-outputcontrolpointid.md) | Defines the index of the control point ID being operated on by an invocation of the main entry point of the hull shader. Can be read by the hull shader only. | uint |
| SV\_Position | When SV\_Position is declared for input to a shader, it can have one of two interpolation modes specified: linearNoPerspective or linearNoPerspectiveCentroid, where the latter causes centroid-snapped xyzw values to be provided when multisample antialiasing. When used in a shader, SV\_Position describes the pixel location. Available in all shaders to get the pixel center with a 0.5 offset. | float4 |
| SV\_PrimitiveID | Per-primitive identifier automatically generated by the runtime (see [Using System-Generated Values (Direct3D 10)](../direct3d11/d3d10-graphics-programming-guide-input-assembler-stage-using.md)). Can be written to by the geometry or pixel shaders, and read by the geometry, pixel, hull or domain shaders. | uint |
| SV\_RenderTargetArrayIndex | Render-target array index. Applied to geometry shader output, and indicates the render target array slice that the primitive will be drawn to by the pixel shader. SV\_RenderTargetArrayIndex is valid only if the render target is an array resource. This semantic applies only to primitives; if a primitive has more than one vertex, then the value from the leading vertex is used. This value also indicates which array slice of a depth/stencil view is used for read/write purposes.<br/> Can be written from the geometry shader, and read by the pixel shader.<br/> If [D3D11_FEATURE_DATA_D3D11_OPTIONS3::VPAndRTArrayIndexFromAnyShaderFeedingRasterizer](/windows/win32/api/d3d11/ns-d3d11-d3d11_feature_data_d3d11_options3) is `true`, then SV\_RenderTargetArrayIndex is applied to any shader feeding the rasterizer. | uint |
| SV\_SampleIndex | Sample frequency index data. Available to be read or written to by the pixel shader only. | uint |
| SV\_StencilRef | Represents the current pixel shader stencil reference value. Can be written by the pixel shader only. | uint |
| SV\_Target\[n\], where 0 <= n <= 7 | The output value that will be stored in a render target. The index indicates which of the 8 possibly bound render targets to write to. The value is available to all shaders. | float\[2\|3\|4\] |
| [SV\_TessFactor](sv-tessfactor.md) | Defines the tessellation amount on each edge of a patch. Available for writing in the hull shader and reading in the domain shader. | float\[2\|3\|4\] |
| SV\_VertexID | Per-vertex identifier automatically generated by the runtime (see [Using System-Generated Values (Direct3D 10)](../direct3d11/d3d10-graphics-programming-guide-input-assembler-stage-using.md)). Available as the input to the vertex shader only. | uint |
| SV\_ViewportArrayIndex | Viewport array index. Applied to geometry shader output, and indicates which viewport to use for the primitive currently being written out. Can be read by the pixel shader. The primitive will be transformed and clipped against the viewport specified by the index before it is passed to the rasterizer. This semantic applies only to primitives; if a primitive has more than one vertex, then the value from the leading vertex is used. <br/> If [D3D11_FEATURE_DATA_D3D11_OPTIONS3::VPAndRTArrayIndexFromAnyShaderFeedingRasterizer](/windows/win32/api/d3d11/ns-d3d11-d3d11_feature_data_d3d11_options3) is `true`, then SV\_ViewportArrayIndex is applied to any shader feeding the rasterizer. | uint |
| SV\_ShadingRate | Defines, through shading rate [values](/windows/win32/api/d3d12/ne-d3d12-d3d12_shading_rate), the number of pixels written by one pixel shader invocation for [Variable Shading Rate Tier 2](/windows/win32/api/d3d12/ne-d3d12-d3d12_variable_shading_rate_tier) or higher devices. Can be read from the pixel shader. Can be written from a vertex or geometry shader. | uint |

### Limitations when writing SV\_Depth:

- When multisampling (MultisampleEnable is **TRUE** in [**D3D10\_RASTERIZER\_DESC**](/windows/win32/api/d3d10/ns-d3d10-d3d10_rasterizer_desc)) and writing a depth value (using a pixel shader), the single value written out is also used in the [depth test](../direct3d11/d3d10-graphics-programming-guide-depth-stencil.md); so the ability to render primitive edges at higher resolution is lost when multisampling.
- When using dynamic-flow control, it is impossible to determine at compile time whether a shader that writes SV\_Depth in some paths will be guaranteed to write SV\_Depth in every execution. Failure to write SV\_Depth when declared results in undefined behavior (which may or may not include discard of the pixel).
- Any float32 value including +/-INF and NaN can be written to SV\_Depth.
- Writing SV\_Depth is still valid when performing Dual Source Color Blending.

## Migration from Direct3D 9 to Direct3D 10 and later

The following issues should be considered when migrating code from Direct3D 9 to Direct3D 10 and later:

### Mapping to Direct3D 9 Semantics

A few of the Direct3D 10 and later semantics map directly to Direct3D 9 semantics.

| Direct3D 10 Semantic | Direct3D 9 Equivalent Semantic |
|-|-|
| SV\_Depth | DEPTH |
| SV\_Position | POSITION |
| SV\_Target | COLOR |

> [!]
> Note to Direct3D 9 developers: For Direct3D 9 targets, shader semantics must map to valid Direct3D 9 semantics. For backwards compatibility POSITION0 (and its variant names) is treated as SV\_Position, COLOR is treated as SV\_TARGET.

- [Mapping to Direct3D 9 Semantics](#mapping-to-direct3d-9-semantics)
- [Direct3D 9 VPOS and Direct3D 10 SV\_Position](#direct3d-9-vpos-and-direct3d-10-sv_position)
- [User clip planes in HLSL](#user-clip-planes-in-hlsl)

### Direct3D 9 VPOS and Direct3D 10 SV\_Position

The D3D10 semantic SV\_Position provides similar functionality to the Direct3D 9 shader model 3 VPOS semantic. For instance, in Direct3D 9 the following syntax is used for a pixel shader using screen space coordinates:

```HLSL
float4 psMainD3D9( float4 screenSpace : VPOS ) : COLOR
{
    // code here 
}
```

VPOS was added for shader model 3 support, to specify screen space coordinates, since the POSITION semantic was intended for object-space coordinates.

In Direct3D 10 and later, the SV\_Position semantic (when used in the context of a pixel shader) specifies screen space coordinates (offset by 0.5). Therefore, the Direct3D 9 shader would be roughly equivalent (without accounting for the 0.5 offset) to the following:

```HLSL
float4 psMainD3D10( float4 screenSpace : SV_Position ) : COLOR
{
    // code here
}
```

When migrating from Direct3D 9 to Direct3D 10 and later, you will need to be aware of this when translating your shaders.

### User clip planes in HLSL

Starting with Windows 8, you can use the **clipplanes** function attribute in an HLSL [function declaration](dx-graphics-hlsl-function-syntax.md) rather than SV\_ClipDistance to make your shader work on [feature level](../direct3d11/overviews-direct3d-11-devices-downlevel-intro.md) 9\_x as well as feature level 10 and higher. For more info, see [User clip planes on feature level 9 hardware](./user-clip-planes-on-10level9.md).

## Related topics

* [Language Syntax](dx-graphics-hlsl-language-syntax.md)
* [Variables (DirectX HLSL)](dx-graphics-hlsl-variables.md)