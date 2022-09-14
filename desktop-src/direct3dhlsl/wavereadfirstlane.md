---
title: WaveReadLaneFirst function
description: Returns the value of the expression for the active lane of the current wave with the smallest index.
ms.assetid: 89CA4FD5-4573-42ED-88D3-01C79C69FF6F
keywords:
- WaveReadLaneFirst function HLSL
topic_type:
- apiref
api_name:
- WaveReadLaneFirst
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveReadLaneFirst function

Returns the value of the expression for the active lane of the current wave with the smallest index.

## Syntax

``` syntax
<type> WaveReadLaneFirst(
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

The resulting value is uniform across the wave.

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




