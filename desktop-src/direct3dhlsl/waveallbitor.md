---
title: WaveActiveBitOr function
description: Returns the bitwise OR of all the values of the expression across all active lanes in the current wave and replicates it back to all active lanes.
ms.assetid: FC8E5987-DAA7-41E6-A1AB-AA0E6A82CFC7
keywords:
- WaveActiveBitOr function HLSL
topic_type:
- apiref
api_name:
- WaveActiveBitOr
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveBitOr function

Returns the bitwise OR of all the values of <expr> across all active non-helper lanes in the current wave and replicates it back to all active non-helper lanes.

## Syntax

``` syntax
<int_type> WaveActiveBitOr(
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

The bitwise OR value.

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




