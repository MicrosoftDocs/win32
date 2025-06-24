---
title: Any-hit shader
description: A shader that's invoked when ray intersections are not opaque.
ms.date: 05/31/2018
ms.topic: reference
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RAY_FLAG
api_type: 
- NA
---

# Any-hit shader

A shader that's invoked when ray intersections are not opaque.

An any-hit shader must declare a payload parameter, followed by an attributes parameter. When fixed function triangle intersection is used, each of those parameters must be a user-defined structure type matching types used for [**TraceRay**](./traceray-function.md) and [**ReportHit**](./reporthit-function.md) respectively, or the [**Intersection attributes structure**](./intersection-attributes.md).

An any-hit shader can perform the following kinds of operations:

* Read and modify the ray payload: (inout payload_t rayPayload).
* Read the intersection attributes: (in attr_t attributes).
* Call [**AcceptHitAndEndSearch**](./accepthitandendsearch-function.md), which accepts the current hit, ends the any-hit shader, ends the [intersection shader](./intersection-shader.md) if one is present, and executes the [closest hit shader](./closest-hit-shader.md) on the closest hit so far if it is active.
* Call [**IgnoreHit**](ignorehit-function.md), which ends the current any-hit shader, and tells the system to continue searching for hits, including returning control to an intersection shader, if it is currently executing, and returning false from the [**ReportHit**](./reporthit-function.md)* call site. 
* Return without calling either of these intrinsics, which accepts the current hit, and tells the system to continue searching for hits, including returning control to the intersection shader if there is one, and returning true at the [**ReportHit**](reporthit-function.md) call site to indicate that the hit was accepted.

Even if an any-hit shader invocation is ended by [**IgnoreHit**](./ignorehit-function.md) or [**AcceptHitAndEndSearch**](./accepthitandendsearch-function.md), any modifications made to the ray payload so far must still be retained.

## Shader type attribute

```
[shader("anyhit")]
```

## Example

```
[shader("anyhit")]
void anyhit_main( inout MyPayload payload, in MyAttributes attr )
{
    float3 hitLocation = ObjectRayOrigin() + ObjectRayDirection() * RayTCurrent();
    float alpha = computeAlpha(hitLocation, attr, ...);

    // Processing shadow and only care if a hit is registered?
    if (TerminateShadowRay(alpha))
        AcceptHitAndEndSearch(); // aborts function

    // Save alpha contribution and ignoring hit?
    if (SaveAndIgnore(payload, RayTCurrent(), alpha, attr, ...))
        IgnoreHit(); // aborts function

    // do something else.
    // return to accept and update closest hit
}
```
