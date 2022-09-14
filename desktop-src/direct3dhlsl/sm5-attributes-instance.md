---
title: instance
description: Use this attribute to instance a geometry shader.
ms.assetid: 0e487e52-53d0-4193-99b2-fd018a061b42
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# instance

Use this attribute to instance a geometry shader.


```
instance(X)   
```



## Remarks

X is an integer index that indicates the number of instances to be executed for each drawn item (for example, for each triangle). When using this attribute, use [SV\_GSInstanceID](sv-gsinstanceid.md) to identify which instance of a geometry shader is being executed.

This attribute is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        | x        |       |         |



 

## Related topics

<dl> <dt>

[Shader Model 5 Attributes](d3d11-graphics-reference-sm5-attributes.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




