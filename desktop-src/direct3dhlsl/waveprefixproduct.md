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

<dl> <dt>

*value* 
</dt> <dd>

The value to multiply.

</dd> </dl>

## Return value

The product of all the values.

## Remarks

The order of operations on this routine cannot be guaranteed, so effectively the \[precise\] flag is ignored within it.

A postfix product can be computed by multiplying the prefix product by the current lane’s value.

This function is supported from shader model 6.0, in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## Examples

``` syntax
 // compute offset into buffer for this lane’s writes
    uint numWrites;      // number of DWORDs to write to the output from this lane
    uint offset = WavePrefixProduct( numWrites );
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




