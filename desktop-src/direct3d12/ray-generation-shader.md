---
description: A shader that calls TraceRay to generate rays.
ms.assetid: 
title: Ray Generation Shader
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RAY_FLAG
api_type: 
- NA
---

# Ray Generation Shader

A shader that calls [**TraceRay**](traceray-function.md) to generate rays. The initial user-defined ray payload for each ray is provided to the **TraceRay** call site.  [**CallShader**](callshader-function.md) may also be used in ray generation shaders to invoke [callable shaders](callable-shader.md).

**DispatchRays** invokes a grid of ray generation shader invocations.  Each invocation (thread) of a ray generation shader knows its location in the overall grid, can generate arbitrary rays via [**TraceRay**](traceray-function.md), and operates independently of other invocations. There is no defined order of execution of threads with respect to each other.

## Shader Type attribute


```
[shader("raygeneration")]
```



## Example

```
struct SceneConstantStructure { ... };
ConstantBuffer<SceneConstantStructure> SceneConstants;
RaytracingAccelerationStructure MyAccelerationStructure : register(t3);
struct MyPayload { ... };

[shader("raygeneration")]
void raygen_main()
{
    RayDesc myRay = {
        SceneConstants.CameraOrigin,
        SceneConstants.TMin,
        computeRayDirection(SceneConstants.LensParams, DispatchRaysIndex(), 
                            DispatchRaysDimensions()),
        SceneConstants.TMax};
    MyPayload payload = { ... };    // init payload
    TraceRay(
        MyAccelerationStructure,
        SceneConstants.RayFlags,
        SceneConstants.InstanceInclusionMask,
        SceneConstants.RayContributionToHitGroupIndex,
        SceneConstants.MultiplierForGeometryContributionToHitGroupIndex,
        SceneConstants.MissShaderIndex,
        myRay,
        payload);
    WriteFinalPixel(DispatchRaysIndex(), payload);
}
```

 

 




