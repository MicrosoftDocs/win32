---
title: WaveActiveAnyTrue function
description: Returns true if the expression is true in any of the active lanes in the current wave.
ms.assetid: 203E2E1D-0AA2-4E4A-80F7-D1FE7579A742
keywords:
- WaveAnyTrue function HLSL
topic_type:
- apiref
api_name:
- WaveAnyTrue
api_type:
- NA
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# WaveActiveAnyTrue function

Returns true if the expression is true in any of the active lanes in the current wave.

## Syntax

``` syntax
bool WaveAnyTrue(
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

True if the expression is true in any lane.

## Remarks

This function is supported from shader model 6.0, in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




