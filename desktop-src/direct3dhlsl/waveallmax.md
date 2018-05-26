---
title: WaveActiveMax function
description: Returns the maximum value of the expression across all active lanes in the current wave and replicates it back to all active lanes.
ms.assetid: 19101C56-2618-4F34-8725-DF92198ABDA4
keywords:
- WaveAllMax function HLSL
topic_type:
- apiref
api_name:
- WaveAllMax
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WaveActiveMax function

Returns the maximum value of the expression across all active lanes in the current wave and replicates it back to all active lanes.

## Syntax

``` syntax
<type> WaveAllMax(
   <type> expr
);
```

## Parameters

<dl> <dt>

*expr* 
</dt> <dd>

The expression to evaluate.

</dd> </dl>

## Return value

The maximum value.

## Remarks

The order of operations is undefined.

This function is supported from shader model 6.0, in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## Examples

``` syntax
 float3 maxPos = WaveAllMax( myPoint.position );
    BoundingBox.max = max( maxPos, BoundingBox.max );
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




