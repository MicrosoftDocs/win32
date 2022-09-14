---
title: WaveActiveBitAnd function
description: Returns the bitwise AND of all the values of the expression across all active lanes in the current wave and replicates it back to all active lanes.
ms.assetid: 602884CD-E656-4DEB-A30A-8A7D127A2217
keywords:
- WaveActiveBitAnd function HLSL
topic_type:
- apiref
api_name:
- WaveActiveBitAnd
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveBitAnd function

Returns the bitwise AND of all the values of the expression across all active lanes in the current wave and replicates it back to all active lanes.

## Syntax


``` syntax
<int_type> WaveActiveBitAnd(
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

The bitwise AND value.

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




