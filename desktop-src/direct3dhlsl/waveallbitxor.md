---
title: WaveActiveBitXor function
description: Returns the bitwise XOR of all the values of the expression across all active lanes in the current wave and replicates it back to all active lanes.
ms.assetid: A6807D17-1E6E-4997-AB52-32FAB5857219
keywords:
- WaveActiveBitXor function HLSL
topic_type:
- apiref
api_name:
- WaveActiveBitXor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveBitXor function

Returns the bitwise XOR of all the values of the expression across all active lanes in the current wave and replicates it back to all active lanes.

## Syntax

``` syntax
<int_type> WaveActiveBitXor(
   <int_type> expr
);
```

## Parameters

<dl> <dt>

*expr* 
</dt> <dd>

The expression to evaluate.

</dd> </dl>

## Return value

The bitwise XOR value.

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




