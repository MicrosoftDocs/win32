---
description: Called by an intersection shader to report a ray intersection.
ms.assetid: 
title: ReportHit function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ReportHit
api_type: 
- NA
---

# ReportHit function

Called by an [intersection shader](intersection-shader.md) to report a ray intersection.

## Syntax
This intrinsic function definition is equivalent to the following function template:

```
template<attr_t>
bool ReportHit(float THit, uint HitKind, attr_t Attributes);
```



## Parameters

`THit`

A float value specifying the parametric distance of the intersection..

`HitKind`

An unsigned integer that identifies the type of hit that occurred.  This is a user-specified value in the range of 0-127.  The value can be read by [any hit](any-hit-shader.md) or [closest hit](closest-hit-shader.md) shaders with the **HitKind** intrinsic.

`Attributes`

The user-defined [**Intersection Attribute Structure**](intersection-attributes.md) structure specifying the intersection attributes.  

## Return Value

**bool** True if the hit was accepted.  A hit is rejected if *THit* is outside the current ray interval, or the any hit shader calls [**IgnoreHit**](ignorehit-function.md).  The current ray interval is defined by **RayTMin** and **RayTCurrent**.

## Remarks

This function can be called from the following raytracing shader types:

* [**Intersection Shader**](intersection-shader.md)





## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




