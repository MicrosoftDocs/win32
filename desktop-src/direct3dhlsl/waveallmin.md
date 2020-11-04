---
title: WaveActiveMin function
description: Returns the minimum value of the expression across all active lanes in the current wave replicates it back to all active lanes.
ms.assetid: BA762C02-894C-4AF9-A226-C1E3AAC286FF
keywords:
- WaveActiveMin function HLSL
topic_type:
- apiref
api_name:
- WaveActiveMin
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveMin function

Returns the minimum value of the expression across all active lanes in the current wave replicates it back to all active lanes.

## Syntax

``` syntax
<type> WaveActiveMin(
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

The minimum value.

## Remarks

The order of operations is undefined.

This function is supported from shader model 6.0 in all shader stages. 



 

## Examples

``` syntax
 float3 minPos = WaveActiveMin( myPoint.position );
    BoundingBox.min = min( minPos, BoundingBox.min );
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




