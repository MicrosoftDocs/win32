---
title: WavePrefixProduct function
description: Returns the product of all of the values in the active lanes in this wave with indices less than this lane.
ms.assetid: 3A5B271D-EF45-4511-9086-A9AD0D215D9A
keywords:
- WavePrefixProduct function HLSL
topic_type:
- apiref
api_name:
- WavePrefixProduct
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WavePrefixProduct function

Returns the product of all of the values in the active lanes in this wave with indices less than this lane.

## Syntax

``` syntax
<type> WavePrefixProduct(
   <type> value
);
```

## Parameters

*value* 

The value to multiply.

## Return value

The product of all the values.

## Remarks

The order of operations on this routine cannot be guaranteed. So, effectively, the \[precise\] flag is ignored within it.

A postfix product can be computed by multiplying the prefix product by the current lane's value.

Note that the active lane with the lowest index will always receive a 1 for its prefix product.

This function is supported from shader model 6.0 in all shader stages. 

## Examples

```hlsl
uint numToMultiply = 2;
uint prefixProduct = WavePrefixProduct( numToMultiply );
```

On a machine with a wave size of 8, and all lanes active except lanes 0 and 4, the following values would be returned from WavePrefixProduct.

| lane index | status   | prefixProduct | 
|------------|----------|---------------|
| 0          | inactive | n/a           |
| 1          | active   | = 1           |
| 2          | active   | = 1\*2        |
| 3          | active   | = 1\*2\*2     |
| 4          | inactive | n/a           |
| 5          | active   | = 1\*2\*2\*2       |
| 6          | active   | = 1\*2\*2\*2\*2    |
| 7          | active   | = 1\*2\*2\*2\*2\*2 |

## See also

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)

[Shader Model 6](shader-model-6-0.md)
