---
title: WaveActiveMax function
description: Returns the maximum value of the expression across all active lanes in the current wave and replicates it back to all active lanes.
ms.assetid: 19101C56-2618-4F34-8725-DF92198ABDA4
keywords:
- WaveActiveMax function HLSL
topic_type:
- apiref
api_name:
- WaveActiveMax
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveMax function

Returns the maximum value of the expression across all active lanes in the current wave and replicates it back to all active lanes.

## Syntax

``` syntax
<type> WaveActiveMax(
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

This function is supported from shader model 6.0 in all shader stages. 



 

## Examples

``` syntax
 float3 maxPos = WaveActiveMax( myPoint.position );
    BoundingBox.max = max( maxPos, BoundingBox.max );
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




