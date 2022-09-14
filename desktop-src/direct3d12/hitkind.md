---
description: Returns the value passed as the HitKind parameter to ReportHit.
ms.assetid: 
title: HitKind
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HitKind
api_type: 
- NA
---

# HitKind

Returns the value passed as the **HitKind** parameter to [**ReportHit**](reporthit-function.md).

## Syntax

```
uint HitKind();

```



## Remarks

If the intersection was reported by fixed-function triangle intersection, **HitKind** will be one of **HIT\_KIND\_TRIANGLE\_FRONT\_FACE** (254) or **HIT\_KIND\_TRIANGLE\_BACK\_FACE** (255).

This function can be called from the following raytracing shader types:

* [**Any Hit Shader**](any-hit-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Intersection Shader**](intersection-shader.md)





## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




