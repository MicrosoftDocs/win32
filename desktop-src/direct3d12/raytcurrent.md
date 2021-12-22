---
description: A float representing the current parametric ending point for the ray.
ms.assetid: 
title: RayTCurrent
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RayTCurrent
api_type: 
- NA
---

# RayTCurrent

A float representing the current parametric ending point for the ray.  

## Syntax

```
float RayTCurrent();

```


## Remarks

**RayTCurrent** defines the current ending point of the ray according to the following formula: Origin + (Direction * RayTCurrent).  *Origin* and *Direction* may be in either world or object space, which results in either a world or an object space ending point.

**RayTCurrent** is initialized in the call [**TraceRay**](traceray-function.md) call with the [**RayDesc::TMax**](raydesc.md) value and then is updated during the trace query as intersections are reported (in the any hit), and accepted.

In the [intersection shader](intersection-shader.md), it represents the distance to the closest intersection found so far.  It will be updated after () to the THit value provided if the hit was accepted.

In the [any hit shader](any-hit-shader.md), it represents the distance to the current intersection being reported.

In the [closest hit shader](closest-hit-shader.md), it represents the distance to the closest intersection accepted.

In the [miss shader](miss-shader.md), it is equal to *TMax* passed to the **TraceRay** call.


This function can be called from the following raytracing shader types:

* [**Any Hit Shader**](any-hit-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Intersection Shader**](intersection-shader.md)
* [**Miss Shader**](miss-shader.md)





## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




