---
title: Intersection attributes structure 
description: A structure declared in HLSL to represent hit attributes for fixed-function triangle intersection or axis-aligned bounding box for procedural primitive intersection.
ms.assetid: 
ms.localizationpriority: low
ms.topic: language-reference
ms.date: 05/31/2018
---

# Intersection attributes structure 

A structure declared in HLSL to represent hit attributes for fixed-function triangle intersection or axis-aligned bounding box for procedural primitive intersection.

## Fixed-function triangle intersection

The following structure is declared in HLSL to represent hit attributes for fixed-function triangle intersection:


```
struct BuiltInTriangleIntersectionAttributes
{
    float2 barycentrics;
};
```

[Any hit](any-hit-shader.md) and [closest hit](closest-hit-shader.md) shaders invoked using fixed-function triangle intersection must use this structure for hit attributes. Given attributes a0, a1 and a2 for the 3 vertices of a triangle, barycentrics.x is the weight for a1 and barycentrics.y is the weight for a2.  For example, the app can interpolate by doing:  a = a0 + barycentrics.x * (a1-a0) + barycentrics.y* (a2 – a0).

## Axis-aligned bounding box for procedural primitive intersection

When axis-aligned bounding boxes are used for intersection with procedural primitives, an intersection shader is triggered.  That shader provides a user-defined intersection attribute structure to the [**ReportHit**](reporthit-function.md) call.  The any hit and closest hit shaders bound in the same hit group with this intersection shader must use the same structure for hit attributes, even if the attributes are not referenced.  The maximum attribute structure size is 32 bytes, defined as **D3D12\_RAYTRACING\_MAX\_ATTRIBUTE\_SIZE\_IN\_BYTES**.


