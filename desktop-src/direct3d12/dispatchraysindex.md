---
description: Gets the current location within the width, height, and depth obtained with the [**DispatchRaysDimensions**](dispatchraysdimensions.md) system value intrinsic.
title: DispatchRaysIndex
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DispatchRaysIndex
api_type: 
- NA
---

# DispatchRaysIndex

Gets the current location within the width, height, and depth obtained with the [**DispatchRaysDimensions**](dispatchraysdimensions.md) system value intrinsic.

## Syntax

```syntax
uint3 DispatchRaysIndex();
```

## Remarks

This function can be called from the following raytracing shader types.

* [**Any Hit Shader**](any-hit-shader.md)
* [**Callable Shader**](callable-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Intersection Shader**](intersection-shader.md)
* [**Miss Shader**](miss-shader.md)
* [**Ray Generation Shader**](ray-generation-shader.md)

## See also

* [Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
