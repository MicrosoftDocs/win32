---
title: QuadReadAccrossDiagonal function
description: Returns the specified local value which is read from the diagonally opposite lane in this quad.
ms.assetid: 2914F1F9-5CE2-437A-ADDB-4955D2C1490B
keywords:
- QuadReadAccrossDiagonal function HLSL
topic_type:
- apiref
api_name:
- QuadReadAccrossDiagonal
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# QuadReadAccrossDiagonal function

Returns the specified local value which is read from the diagonally opposite lane in this quad.

## Syntax


```C++
<type> QuadReadAccrossDiagonal(
   <type> localValue
);
```



## Parameters

<dl> <dt>

*localValue* 
</dt> <dd>

The requested type.

</dd> </dl>

## Return value

The specified local value which is read from the diagonally opposite lane in this quad.

## Remarks

For more information on quads, refer to [Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md).

This function is supported from shader model 6.0, in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     |         |



 

## See also

<dl> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




