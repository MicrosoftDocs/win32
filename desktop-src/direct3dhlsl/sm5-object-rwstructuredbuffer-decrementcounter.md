---
title: RWStructuredBuffer::DecrementCounter function
description: Decrements the object's hidden counter.
ms.assetid: 24bc0b63-a482-4fa5-9898-2d43bca20cf4
keywords:
- DecrementCounter function HLSL
topic_type:
- apiref
api_name:
- DecrementCounter
api_location:
- 
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DecrementCounter function

Decrements the object's hidden counter.

## Syntax

``` syntax
uint DecrementCounter(void);
```

## Parameters

This function has no parameters.

## Return value

Type: **uint**

The post-decremented counter value.

## Remarks

The bound unordered access view must have [**D3D11\_BUFFER\_UAV\_FLAG\_COUNTER**](/windows/desktop/api/d3d11/ne-d3d11-d3d11_buffer_uav_flag) set during creationfor this method to work.

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |

## See also

<dl> <dt>

[RWStructuredBuffer](sm5-object-rwstructuredbuffer.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

