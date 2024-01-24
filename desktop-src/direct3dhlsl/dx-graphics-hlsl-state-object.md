---
title: State Objects
description: Use HLSL to define state objects.
ms.assetid: a02432dc-f354-48c0-a7ac-1ff502f3b1d1
ms.topic: article
ms.date: 2/2/2021
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# State Objects

With shader models 6.3 and later, applications have the convenience and flexibility of being able to define DXR state objects directly in HLSL shader code in addition to using Direct3D 12 APIs.

In HLSL, state objects are declared with this syntax:

``` syntax
Type Name = 
{ 
    Field1,
    Field2,
    ...
};
```



| Item                                                                                         | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Type"></span><span id="type"></span><span id="TYPE"></span>**Type**<br/>     | Identifies the type of subobject. Must be one of the supported HLSL subobject types.<br/>     |
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>     | An ASCII string that uniquely identifies the variable name.<br/>                 |
| <span id="Field"></span><span id="field"></span><span id="FIELD"></span>**Field[1, 2, ...]**<br/> | Fields of the subobject. Specific fields for each type of subobject are described below.<br/> |




List of subobject types:
-   [StateObjectConfig](#stateobjectconfig)
-   [GlobalRootSignature](#globalrootsignature)
-   [LocalRootSignature](#localrootsignature)
-   [SubobjectToExportsAssocation](#subobjecttoexportsassocation)
-   [RaytracingShaderConfig](#raytracingshaderconfig)
-   [RaytracingPipelineConfig](#raytracingpipelineconfig)
-   [TriangleHitGroup](#trianglehitgroup)
-   [ProceduralPrimitiveHitGroup](#proceduralprimitivehitgroup)

## StateObjectConfig

The StateObjectConfig subobject type corresponds to a [D3D12_STATE_OBJECT_CONFIG](/windows/win32/api/d3d12/ns-d3d12-d3d12_state_object_config) structure.

It has one field, a bitwise flag, which is one or both of

* STATE_OBJECT_FLAGS_ALLOW_LOCAL_DEPENDENCIES_ON_EXTERNAL_DEFINITONS
* STATE_OBJECT_FLAGS_ALLOW_EXTERNAL_DEPENDENCIES_ON_LOCAL_DEFINITIONS

or, zero for neither of them.

Example:

```
StateObjectConfig MyStateObjectConfig = 
{ 
    STATE_OBJECT_FLAGS_ALLOW_LOCAL_DEPENDENCIES_ON_EXTERNAL_DEFINITONS
};
```

## GlobalRootSignature
A GlobalRootSignature corresponds to a [D3D12_GLOBAL_ROOT_SIGNATURE](/windows/win32/api/d3d12/ns-d3d12-d3d12_global_root_signature) structure.

The fields consist of some number of strings describing the parts of the root signature. For reference on this, see [Specifying Root Signatures in HLSL](../direct3d12/specifying-root-signatures-in-hlsl.md).

Example:
```
GlobalRootSignature MyGlobalRootSignature =
{
    "DescriptorTable(UAV(u0)),"                     // Output texture
    "SRV(t0),"                                      // Acceleration structure
    "CBV(b0),"                                      // Scene constants
    "DescriptorTable(SRV(t1, numDescriptors = 2))"  // Static index and vertex buffers.
};
```

## LocalRootSignature
A LocalRootSignature corresponds to a [D3D12_LOCAL_ROOT_SIGNATURE](/windows/win32/api/d3d12/ns-d3d12-d3d12_local_root_signature) structure.

Just like the global root signature subobject, the fields consist of some number of strings describing the parts of the root signature. For reference on this, see [Specifying Root Signatures in HLSL](../direct3d12/specifying-root-signatures-in-hlsl.md).

Example:
```
LocalRootSignature MyLocalRootSignature = 
{
    "RootConstants(num32BitConstants = 4, b1)"  // Cube constants 
};
```

## SubobjectToExportsAssocation
By default, a subobject merely declared in the same library as an export is able to apply to that export. However, applications have the ability to override that and get specific about what subobject goes with which export. In HLSL, this "explicit association" is done using SubobjectToExportsAssocation.

A SubobjectToExportsAssocation corresponds to a [D3D12_DXIL_SUBOBJECT_TO_EXPORTS_ASSOCIATION ](/windows/win32/api/d3d12/ns-d3d12-d3d12_dxil_subobject_to_exports_association) structure.

This subobject is declared with the syntax

``` syntax
SubobjectToExportsAssocation Name = 
{ 
    SubobjectName,
    Exports
};
```

| Item                                                                                         | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>     | An ASCII string that uniquely identifies the variable name.<br/>                 |
| <span id="SubobjectName"></span><span id="subobjectname"></span><span id="SUBOBJECTNAME"></span>**SubobjectName**<br/>     | String which identifies an exported subobject.<br/> |
| <span id="Exports"></span><span id="exports"></span><span id="EXPORTS"></span>**Exports**<br/> | String containing a semicolon-delimited list of exports.<br/> |


Example:
```
SubobjectToExportsAssociation MyLocalRootSignatureAssociation =
{
    "MyLocalRootSignature",    // Subobject name
    "MyHitGroup;MyMissShader"  // Exports association 
};
```

Note that both fields use *exported* names. An exported name may be different from the original name in HLSL, if the application chooses to do export-renaming.

## RaytracingShaderConfig

A RaytracingShaderConfig corresponds to a [D3D12_RAYTRACING_SHADER_CONFIG](/windows/win32/api/d3d12/ns-d3d12-d3d12_raytracing_shader_config) structure.

This subobject is declared with the syntax

``` syntax
RaytracingShaderConfig Name = 
{ 
    MaxPayloadSize,
    MaxAttributeSize
};
```

| Item                                                                                         | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>     | An ASCII string that uniquely identifies the variable name.<br/>                 |
| <span id="MaxPayloadSize"></span><span id="maxpayloadsize"></span><span id="MAXPAYLOADSIZE"></span>**MaxPayloadSize**<br/>     | Numerical value for the maximum storage for scalars (counted as 4 bytes each) in ray payloads for associated raytracing shaders.<br/> |
| <span id="MaxAttributeSize"></span><span id="maxattributesize"></span><span id="MAXATTRIBUTESIZE"></span>**MaxAttributeSize**<br/> | Numerical value for the maximum number of scalars (counted as 4 bytes each) that can be used for attributes in associated raytracing shaders. The value cannot exceed [D3D12_RAYTRACING_MAX_ATTRIBUTE_SIZE_IN_BYTES](../direct3d12/constants.md).<br/> |


Example:
```
RaytracingShaderConfig MyShaderConfig =
{
    16,  // Max payload size
    8    // Max attribute size
};
```

## RaytracingPipelineConfig

A RaytracingPipelineConfig corresponds to a [D3D12_RAYTRACING_PIPELINE_CONFIG](/windows/win32/api/d3d12/ns-d3d12-d3d12_raytracing_pipeline_config) structure.

This subobject is declared with the syntax

``` syntax
RaytracingPipelineConfig Name = 
{ 
    MaxTraceRecursionDepth
};
```

| Item                                                                                         | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>     | An ASCII string that uniquely identifies the variable name.<br/>                 |
| <span id="MaxTraceRecursionDepth"></span><span id="maxtracerecursiondepth"></span><span id="MAXTRACERECURSIONDEPTH"></span>**MaxTraceRecursionDepth**<br/>     | Numerical limit to use for ray recursion in the raytracing pipeline. It is a number between 0 and 31, inclusive. <br/> |


Example:
```
RaytracingPipelineConfig MyPipelineConfig =
{
    1  // Max trace recursion depth
};
```
Since there is a performance cost to raytracing recursion, applications should use the lowest recursion depth needed for the desired results.

If shader invocations haven't yet reached the maximum recursion depth, they can call [TraceRay](../direct3d12/traceray-function.md) any number of times. But if they reach or exceed the maximum recursion depth, calling TraceRay puts the device into removed state. Therefore, raytracing shaders should take care to stop calling TraceRay if they've met or exceeded the maximum recursion depth.

## TriangleHitGroup

A TriangleHitGroup corresponds to a [D3D12_HIT_GROUP_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_hit_group_desc) structure whose Type field is set to [D3D12_HIT_GROUP_TYPE_TRIANGLES](/windows/win32/api/d3d12/ne-d3d12-d3d12_hit_group_type#constants).

This subobject is declared with the syntax

``` syntax
TriangleHitGroup Name = 
{ 
    AnyHitShader,
    ClosestHitShader
};
```

| Item                                                                                         | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>     | An ASCII string that uniquely identifies the variable name.<br/>                 |
| <span id="AnyHitShader"></span><span id="anyhitshader"></span><span id="ANYHITSHADER"></span>**AnyHitShader**<br/>     | String name of the anyhit shader for the hit group, or an empty string.<br/> |
| <span id="ClosestHitShader"></span><span id="closesthitshader"></span><span id="CLOSESTHITSHADER"></span>**ClosestHitShader**<br/> | String name of the closest hit shader for the hit group, or an empty string.<br/> |


Example:
```
TriangleHitGroup MyHitGroup =
{
    "",                    // AnyHit
    "MyClosestHitShader",  // ClosestHit
};
```

Note that both fields use *exported* names. An exported name may be different from the original name in HLSL, if the application chooses to do export-renaming.

## ProceduralPrimitiveHitGroup

A ProceduralPrimitiveHitGroup corresponds to a [D3D12_HIT_GROUP_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_hit_group_desc) structure whose Type field is set to [D3D12_HIT_GROUP_TYPE_PROCEDURAL_PRIMITIVE](/windows/win32/api/d3d12/ne-d3d12-d3d12_hit_group_type#constants).

This subobject is declared with the syntax

``` syntax
ProceduralPrimitiveHitGroup Name = 
{ 
    AnyHitShader,
    ClosestHitShader,
    IntersectionShader
};
```

| Item                                                                                         | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>     | An ASCII string that uniquely identifies the variable name.<br/>                 |
| <span id="AnyHitShader"></span><span id="anyhitshader"></span><span id="ANYHITSHADER"></span>**AnyHitShader**<br/>     | String name of the anyhit shader for the hit group, or an empty string.<br/> |
| <span id="ClosestHitShader"></span><span id="closesthitshader"></span><span id="CLOSESTHITSHADER"></span>**ClosestHitShader**<br/> | String name of the closest hit shader for the hit group, or an empty string.<br/> |
| <span id="IntersectionShader"></span><span id="intersectionshader"></span><span id="INTERSECTIONSHADER"></span>**IntersectionShader**<br/> | String name of the intersection shader for the hit group, or an empty string.<br/> |


Example:
```
ProceduralPrimitiveHitGroup MyProceduralHitGroup
{
    "MyAnyHit",       // AnyHit
    "MyClosestHit",   // ClosestHit
    "MyIntersection"  // Intersection
};

```

Note that the three fields use *exported* names. An exported name may be different from the original name in HLSL, if the application chooses to do export-renaming.

## Remarks

Subobjects have the notion of "association", or "which subobject goes with which export".

When specifying subobjects through shader code, the choice of "which subobject goes with which export" follows the rules as outlined in the [DXR specification](https://microsoft.github.io/DirectX-Specs/d3d/Raytracing.html#subobject-association-behavior). In particular, suppose an application has some export. If an application associates that export with root signature A through shader-code and root signature B through application code, B is the one that gets used. The design of "use B" instead of "produce an error" gives applications the ability to conveniently override DXIL associations using application code, rather than be forced to recompile shaders to resolve mismatching things.

## Related topics

<dl> <dt>

[DirectX Developer Blog post "New in D3D12 – DirectX Raytracing (DXR) now supports library subobjects"](https://devblogs.microsoft.com/directx/dxr-library-subobjects/)

[DirectX Raytracing (DXR) Functional Spec](https://microsoft.github.io/DirectX-Specs/d3d/Raytracing.html)

[Sample: D3D12RaytracingLibrarySubobjects](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/develop/Samples/Desktop/D3D12Raytracing/src/D3D12RaytracingLibrarySubobjects)

</dt> </dl>