---
description: Used in an any hit shader to commit the current hit and then stop searching for more hits for the ray.
ms.assetid: 
title: AcceptHitAndEndSearch function
ms.date: 05/31/2018
ms.localizationpriority: low
ms.topic: reference
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AcceptHitAndEndSearch
api_type: 
- NA
---

# AcceptHitAndEndSearch function

Used in an [any hit shader](any-hit-shader.md) to commit the current hit and then stop searching for more hits for the ray. If there is an intersection shader running, it's execution stops.  Execution passes to the [closest hit shader](closest-hit-shader.md), if enabled, with the closest hit recorded so far.

## Syntax

```
void AcceptHitAndEndSearch();
```




## Return Value

**void**

## Remarks

This function can be called from the following raytracing shader types:

* [**Callable Shader**](callable-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Miss Shader**](miss-shader.md)
* [**Ray Generation Shader**](ray-generation-shader.md)



## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




