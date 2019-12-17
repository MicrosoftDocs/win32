---
title: earlydepthstencil
description: Forces depth-stencil testing before a shader executes.
ms.assetid: f8a9fee7-4a8a-4a34-bf7c-56906592caac
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# earlydepthstencil

Forces depth-stencil testing before a shader executes.


```
earlydepthstencil   
```



## Remarks

Depth-stencil testing is normally done during pixel processing by a pixel shader. Forcing early depth-stencil testing causes the testing to be done prior to the shader execution; the purpose is to improve per-pixel performance by culling/reducing/avoiding unnecessary pixel processing.

An application can force early depth-stencil testing by supplying the attribute or the hardware may execute early depth-stencil testing provided no depth values are written and no unordered access operations are performed in a shader as an optimization.

This attribute is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     |         |



 

## Related topics

<dl> <dt>

[Shader Model 5 Attributes](d3d11-graphics-reference-sm5-attributes.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




