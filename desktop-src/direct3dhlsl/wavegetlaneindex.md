---
title: WaveGetLaneIndex function
description: Returns the index of the current lane within the current wave.
ms.assetid: C05BD814-23DF-432F-8669-C03842B77AC7
keywords:
- WaveGetLaneIndex function HLSL
topic_type:
- apiref
api_name:
- WaveGetLaneIndex
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveGetLaneIndex function

Returns the index of the current lane within the current wave.

## Syntax

``` syntax
uint WaveGetLaneIndex(void);
```

## Parameters

This function has no parameters.

## Return value

The index of the current lane. The result is greater than or equal to zero and less than the value returned by [**WaveGetLaneCount**](wavegetlanecount.md).

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




