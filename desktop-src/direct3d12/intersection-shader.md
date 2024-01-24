---
description: A shader that is used to implement custom intersection primitives for rays intersecting an associated bounding volume (bounding box).
ms.assetid: 
title: Intersection Shader
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

# Intersection Shader

A shader that is used to implement custom intersection primitives for rays intersecting an associated bounding volume (bounding box). 

The intersection shader does not have access to the ray payload, but defines the intersection attributes for each hit through a call to [**ReportHit**](reporthit-function.md).  The handling of **ReportHit** may stop the intersection shader early, if the ray flag **RAY\_FLAG\_ACCEPT\_FIRST\_HIT_\AND\_\END\_SEARCH** is set, or [**AcceptHitAndEndSearch**](accepthitandendsearch-function.md) is called from an any hit shader.  Otherwise, it returns true if the hit was accepted or false if the hit was rejected.  This means that an any hit shader, if present, must execute before control conditionally returns to the intersection shader.

## Shader Type attribute


```
[shader("intersection")]
```



## Example

```
struct CustomPrimitiveDef { ... };
struct MyAttributes { ... };
struct CustomIntersectionIterator {...};
void InitCustomIntersectionIterator(CustomIntersectionIterator it) {...}
bool IntersectCustomPrimitiveFrontToBack(
    CustomPrimitiveDef prim,
    inout CustomIntersectionIterator it,
    float3 origin, float3 dir,
    float rayTMin, inout float curT,
    out MyAttributes attr);

[shader("intersection")]
void intersection_main()
{
    float THit = RayTCurrent();
    MyAttributes attr;
    CustomIntersectionIterator it;
    InitCustomIntersectionIterator(it); 
    while(IntersectCustomPrimitiveFrontToBack(
            CustomPrimitiveDefinitions[LocalConstants.PrimitiveIndex],
            it, ObjectRayOrigin(), ObjectRayDirection(), 
            RayTMin(), THit, attr))
    {
        // Exit on the first hit.  Note that if the ray has
        // RAY_FLAG_ACCEPT_FIRST_HIT_AND_END_SEARCH or an
        // anyhit shader is used and calls AcceptHitAndEndSearch(),
        // that would also fully exit this intersection shader (making
        // the “break” below moot in that case).        
        if (ReportHit(THit, /*hitKind*/ 0, attr) && (RayFlags() &  RAY_FLAG_FORCE_OPAQUE))
            break;
    }
}
```

 

 




