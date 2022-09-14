---
description: Called from an any hit shader to reject the hit and end the shader.
ms.assetid: 
title: IgnoreHit function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IgnoreHit
api_type: 
- NA
---

# IgnoreHit function

Called from an [any hit shader](any-hit-shader.md) to reject the hit and end the shader. The hit search continues on without committing the distance and attributes for the current hit.  The [**ReportHit**](reporthit-function.md) call in the [intersection shader](intersection-shader.md), if there is one, will return false.  Any modifications made to the ray payload up to this point in the any hit shader are preserved.

## Syntax

```
void IgnoreHit();

```


## Return Value

**void**

## Remarks

This function can be called from the following raytracing shader types:

* [**Any Hit Shader**](any-hit-shader.md)




## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




