---
title: maxtessfactor
description: Indicates the maximum value that the hull shader would return for any tessellation factor.
ms.assetid: 2c12ed56-cd64-4143-8dda-6998aa212356
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# maxtessfactor

Indicates the maximum value that the hull shader would return for any tessellation factor.


```
maxtessfactor(X)   
```



## Remarks

This attribute puts an upper bound on the amount of tessellation requested to help a driver determine the maximum amount of resources required for tessellation.

This attribute is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        | x    |        |          |       |         |



 

## Related topics

<dl> <dt>

[Shader Model 5 Attributes](d3d11-graphics-reference-sm5-attributes.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




