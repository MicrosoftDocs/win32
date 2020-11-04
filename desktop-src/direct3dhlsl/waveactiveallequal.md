---
title: WaveActiveAllEqual function
description: Returns true if the expression is the same for every active lane in the current wave (and thus uniform across it).
ms.assetid: E0A051A8-0ADD-4EC7-8D9A-8820CED9DA9D
keywords:
- WaveActiveAllEqual function HLSL
topic_type:
- apiref
api_name:
- WaveActiveAllEqual
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveAllEqual function

Returns true if the expression is the same for every active lane in the current wave (and thus uniform across it).

## Syntax


``` syntax
bool WaveActiveAllEqual(
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

True if the expression is the same for every active lane in the current wave.

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




