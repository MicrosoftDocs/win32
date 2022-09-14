---
title: WaveReadLaneAt function
description: Returns the value of the expression for the given lane index within the specified wave.
ms.assetid: CA9467D9-8885-4A5D-87F3-5BA40AE78993
keywords:
- WaveReadLaneAt function HLSL
topic_type:
- apiref
api_name:
- WaveReadLaneAt
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveReadLaneAt function

Returns the value of the expression for the given lane index within the specified wave.

## Syntax

``` syntax
<type> WaveReadLaneAt(
   <type> expr,
   uint laneIndex
);
```

## Parameters

<dl> <dt>

*expr* 
</dt> <dd>

The expression to evaluate.

</dd> <dt>

*laneIndex* 
</dt> <dd>

The index of the lane for which the *expr* result will be returned.

</dd> </dl>

## Return value

The resulting value is the result of *expr*. It will be uniform if *laneIndex* is uniform.

## Remarks

This function is effectively a broadcast of the value in the *laneIndex*'th lane.

This function is supported from shader model 6.0 in all shader stages.

## See also

* [Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
* [Shader Model 6](shader-model-6-0.md)
