---
title: WaveActiveBallot function
description: Returns a uint4 containing a bitmask of the evaluation of the Boolean expression for all active lanes in the current wave. 
ms.assetid: 67FE28E0-F397-431A-8CF8-64E4AD88CDBC
keywords:
- WaveActiveBallot function HLSL
topic_type:
- apiref
api_name:
- WaveActiveBallot
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WaveActiveBallot function

Returns a uint4 containing a bitmask of the evaluation of the Boolean expression for all active lanes in the current wave. 

## Syntax

``` syntax
uint4 WaveActiveBallot(
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

A uint4 containing a bitmask of the evaluation of the Boolean expression for all active lanes in the current wave. The least-significant bit corresponds to the lane with index zero. The bits corresponding to inactive lanes will be zero. The bits that are greater than or equal to [**WaveGetLaneCount**](wavegetlanecount.md) will be zero.

## Remarks

Different GPUs have different SIMD processor widths (lane counts). Most of these **WaveXXX** functions are able to operate at level of abstraction where SIMD machine width is concealed. To maximize portability of code across GPUs, use the intrinsics that don’t rely on machine width. For example, use:

``` syntax
uint result = WaveActiveCountBits( bBit );
```

Instead of:

``` syntax
uint result = countbits( WaveActiveBallot( bBit ) );
```

This function is supported from shader model 6.0 in all shader stages. 



 

## Examples

``` syntax
// get a bitwise representation of the number of currently active lanes:
uint4 waveBits = WaveActiveBallot( true ); // convert to bits 
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




