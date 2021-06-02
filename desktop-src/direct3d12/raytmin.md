---
description: A float representing the current parametric starting point for the ray.
ms.assetid: 
title: RayTMin
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RayTMin
api_type: 
- NA
---

# RayTMin

A float representing the current parametric starting point for the ray. 

## Syntax

```
float RayTMin();

```

## Remarks

**RayTMin** defines the starting point of the ray according to the following formula: Origin + (Direction * RayTMin).  *Origin* and *Direction* may be in either world or object space, which results in either a world or an object space starting point.

**RayTMin** is specified in the call to [**TraceRay**](traceray-function.md), and is constant for the duration of that call.




This function can be called from the following raytracing shader types:

* [**Any Hit Shader**](any-hit-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Intersection Shader**](intersection-shader.md)
* [**Miss Shader**](miss-shader.md)





## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




