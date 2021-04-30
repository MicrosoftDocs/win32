---
title: Ray payload structure 
description: A user-defined structure that is provided as an inout argument in a TraceRay call, and as an inout parameter in the shader types that may access the ray payload.
ms.assetid: 
ms.localizationpriority: low
ms.topic: language-reference
ms.date: 05/31/2018
---

# Ray payload structure 

A user-defined structure that is provided as an inout argument in a [**TraceRay**](traceray-function.md) call, and as an inout parameter in the shader types that may access the ray payload, which include [any hit](any-hit-shader.md), [closest hit](closest-hit-shader.md), and [miss](miss-shader.md) shaders. Any shaders that access the ray payload must use the same structure as the one provided at the originating **TraceRay** call.  Even if one of these shaders doesn’t reference the ray payload at all, it still must specify the matching payload as the originating **TraceRay** call.

