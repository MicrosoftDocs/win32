---
title: WaveActiveSum function
description: Sums up the value of the expression across all active lanes in the current wave and replicates it to all lanes in the current wave.
ms.assetid: 94CEF4AA-D6DE-4B00-9743-F491F255FE3D
keywords:
- WaveAllSum function HLSL
topic_type:
- apiref
api_name:
- WaveAllSum
api_type:
- NA
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# WaveActiveSum function

Sums up the value of the expression across all active lanes in the current wave and replicates it to all lanes in the current wave.

## Syntax

``` syntax
<type> WaveAllSum(
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

The sum value.

## Remarks

The order of operations is undefined.

This function is supported from shader model 6.0, in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## Examples

``` syntax
float3 total = WaveAllSum( position ); // sum positions in wave
float3 center = total/count;           // compute average of these positions
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




