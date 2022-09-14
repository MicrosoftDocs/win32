---
title: WavePrefixCountBits function
description: Returns the sum of all the specified boolean variables set to true across all active lanes with indices smaller than the current lane.
ms.assetid: AEC9AFD7-6478-4397-B531-73990D30AA48
keywords:
- WavePrefixCountBits function HLSL
topic_type:
- apiref
api_name:
- WavePrefixCountBits
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WavePrefixCountBits function

Returns the sum of all the specified boolean variables set to true across all active lanes with indices smaller than the current lane.

## Syntax


``` syntax
uint WavePrefixCountBits(
   bool bBit
);
```



## Parameters

<dl> <dt>

*bBit* 
</dt> <dd>

The specified boolean variables.

</dd> </dl>

## Return value

The sum of all the specified Boolean variables set to true across all active lanes with indices smaller than the current lane.

## Remarks

This function is supported from shader model 6.0 in all shader stages. 



 

## Examples

The following code describes how to implement a compacted write to an ordered stream where the number of elements written per lane is either 1 or 0.

``` syntax
bool bDoesThisLaneHaveAnAppendItem = <expr>;
// compute number of items to append for the whole wave
uint laneAppendOffset = WavePrefixCountBits( bDoesThisLaneHaveAnAppendItem );
uint appendCount = WaveActiveCountBits( bDoesThisLaneHaveAnAppendItem);
// update the output location for this whole wave
uint appendOffset;
if ( WaveIsFirstLane () )
{
    // this way, we only issue one atomic for the entire wave, which reduces contention
    // and keeps the output data for each lane in this wave together in the output buffer
    InterlockedAdd(bufferSize, appendCount, appendOffset);
}
appendOffset = WaveReadLaneFirst( appendOffset ); // broadcast value
appendOffset += laneAppendOffset; // and add in the offset for this lane
buffer[appendOffset] = myData; // write to the offset location for this lane
```

## See also

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 6](shader-model-6-0.md)
</dt> </dl>

 

 




