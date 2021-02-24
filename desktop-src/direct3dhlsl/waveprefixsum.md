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
ms.topic: reference
ms.date: 05/31/2018
api_location: 
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

*value* 

The value to sum up.

## Return value

The sum of the values.

## Remarks

The order of operations on this routine cannot be guaranteed. So, effectively, the \[precise\] flag is ignored within it.

A postfix sum can be computed by adding the prefix sum to the current lane's value.

Note that the active lane with the lowest index will always receive a 0 for its prefix sum.

This function is supported from shader model 6.0 in all shader stages. 

## Examples

```hlsl
uint numToSum = 2;
uint prefixSum = WavePrefixSum( numToSum );
```

On a machine with a wave size of 8, and all lanes active except lanes 0 and 4, the following values would be returned from WavePrefixSum.

| lane index | status   | prefixSum     | 
|------------|----------|---------------|
| 0          | inactive | n/a           |
| 1          | active   | = 0           |
| 2          | active   | = 0+2         |
| 3          | active   | = 0+2+2       |
| 4          | inactive | n/a           |
| 5          | active   | = 0+2+2+2     |
| 6          | active   | = 0+2+2+2+2   |
| 7          | active   | = 0+2+2+2+2+2 |

## See also

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)

[Shader Model 6](shader-model-6-0.md)
