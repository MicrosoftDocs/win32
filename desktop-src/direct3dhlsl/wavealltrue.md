---
title: WaveActiveAllTrue function
description: Returns true if the expression is true in all active lanes in the current wave.
ms.assetid: C4EC5A02-6070-4FF4-B855-F597FFFE66F0
keywords:
- WaveActiveAllTrue function HLSL
topic_type:
- apiref
api_name:
- WaveActiveAllTrue
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveAllTrue function

Returns true if the expression is true in all active lanes in the current wave.

## Syntax

``` syntax
bool WaveActiveAllTrue(
   bool expr
);
```

## Parameters

<dl> <dt>

*expr* 
</dt> <dd>

The boolean expression to evaluate.

</dd> </dl>

## Return value

True if the expression is true in all lanes.

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




