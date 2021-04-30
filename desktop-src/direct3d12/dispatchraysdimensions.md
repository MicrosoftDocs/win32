---
description: The width, height and depth values from the D3D12_DISPATCH_RAYS_DESC structure specified in the originating DispatchRays call.
ms.assetid: 
title: DispatchRaysDimensions
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DispatchRaysDimensions
api_type: 
- NA
---

# DispatchRaysDimensions

The width, height and depth values from the **D3D12\_DISPATCH\_RAYS\_DESC** structure specified in the originating [**DispatchRays**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-dispatchrays) call.

## Syntax

```
uint3 DispatchRaysDimensions();
```

## Remarks

This function can be called from the following raytracing shader types:

* [**Any Hit Shader**](any-hit-shader.md)
* [**Callable Shader**](callable-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Intersection Shader**](intersection-shader.md)
* [**Miss Shader**](miss-shader.md)
* [**Ray Generation Shader**](ray-generation-shader.md)

## See also

* [Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
