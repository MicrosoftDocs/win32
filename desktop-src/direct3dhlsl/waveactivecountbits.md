---
title: WaveActiveCountBits function
description: Counts the number of boolean variables which evaluate to true across all active lanes in the current wave, and replicates the result to all lanes in the wave.
ms.assetid: 053E100C-7E09-4F9D-9F38-9D5E208A38CE
keywords:
- WaveActiveCountBits function HLSL
topic_type:
- apiref
api_name:
- WaveActiveCountBits
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveCountBits function

Counts the number of boolean variables which evaluate to true across all active lanes in the current wave, and replicates the result to all lanes in the wave.

## Syntax


``` syntax
uint WaveActiveCountBits(
   bool bBit
);
```



## Parameters

<dl> <dt>

*bBit* 
</dt> <dd>

The boolean variables to evaluate. Providing an explicit true Boolean value returns the number of active lanes.

</dd> </dl>

## Return value

The number of lanes for which the boolean variable evaluates to true, across all active lanes in the current wave.

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## Examples

This can be implemented more efficiently than a full WaveActiveSum, as described in the following example:

``` syntax
result = WaveActiveCountBits( WaveActiveBallot( bBit ) );
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




