---
title: WaveIsFirstLane function
description: Returns true only for the active lane in the current wave with the smallest index.
ms.assetid: 5D90F713-08C7-4BD4-867B-2E7CA3A85E87
keywords:
- WaveIsHelperLane function HLSL
topic_type:
- apiref
api_name:
- WaveIsHelperLane
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WaveIsFirstLane function

Returns true only for the active lane in the current wave with the smallest index.

## Syntax


```C++
bool WaveIsHelperLane(void);
```



## Parameters

This function has no parameters.

## Return value

True only for the active lane in the current wave with the smallest index.

## Remarks

This function can be used to identify operations that are to be executed only once per wave.

This function is supported from shader model 6.0, in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## Examples

``` syntax
 if ( WaveIsFirstLane() )
{
    . . . // once per-wave code
}
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




