---
title: WavePrefixSum function
description: Returns the sum of all of the values in the active lanes with smaller indices than this one.
ms.assetid: F51B90AB-3E85-4521-8A2C-7C16A4ECB1F9
keywords:
- WavePrefixSum function HLSL
topic_type:
- apiref
api_name:
- WavePrefixSum
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WavePrefixSum function

Returns the sum of all of the values in the active lanes with smaller indices than this one.

## Syntax

``` syntax
<type> WavePrefixSum(
   <type> value
);
```

## Parameters

<dl> <dt>

*value* 
</dt> <dd>

The value to sum up.

</dd> </dl>

## Return value

The sum of the values.

## Remarks

The order of operations on this routine cannot be guaranteed, so effectively the \[precise\] flag is ignored within it.

A postfix sum can be computed by adding the prefix sum to the current lane’s value.

This function is supported from shader model 6.0, in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## Examples

``` syntax
 // compute distinct offset into buffer for each lane
    uint numWrites; // number of values to write to the output from this lane
    uint offset = WavePrefixSum(numWrites); // offset for this lane
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




