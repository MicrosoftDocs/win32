---
title: HLSL Shader Model 6.0
description: Describes the wave operation intrinsics added to HLSL Shader Model 6.0.
ms.assetid: BF968CD3-AC67-48DB-B93F-EF54B680106F
ms.topic: article
ms.date: 05/31/2018
---

# HLSL Shader Model 6.0

Describes the wave operation intrinsics added to HLSL Shader Model 6.0.

- [Shader model 6.0](#shader-model-60)
- [Terminology](#terminology)
- [Shading language intrinsics](#shading-language-intrinsics)
    - [Wave Query](#wave-query)
    - [Wave Vote](#wave-vote)
    - [Wave Broadcast](#wave-broadcast)
    - [Wave Reduction](#wave-reduction)
    - [Wave Scan and Prefix](#wave-scan-and-prefix)
    - [Quad-wide Shuffle operations](#quad-wide-shuffle-operations)
- [Hardware capability](#hardware-capability)
- [Related topics](#related-topics)

## Shader Model 6.0

For earlier shader models, HLSL programming exposes only a single thread of execution. New wave-level operations are provided, starting with model 6.0, to explicitly take advantage of the parallelism of current GPUs - many threads can be executing in lockstep on the same core simultaneously. For example, the model 6.0 intrinsics enable the elimination of barrier constructs when the scope of synchronization is within the width of the SIMD processor, or some other set of threads that are known to be atomic relative to each other.

Potential use cases include: stream compaction, reductions, block transpose, bitonic sort or Fast Fourier Transforms (FFT), binning, stream de-duplication, and similar scenarios.

Most of the intrinsics appear in pixel shaders and compute shaders, though there are some exceptions (noted for each function). The functions have been added to the requirements for DirectX Feature Level 12.0, under API level 12.

The *&lt;type&gt;* parameter and return value for these functions implies the type of the expression, the supported types are those from the following list that are *also* present in the target shader model for your app:

- half, half2, half3, half4
- float, float2, float3, float4
- double, double2, double3, double4
- int, int2, int3, int4
- uint, uint2, uint3, uint4
- short, short2, short3, short4
- ushort, ushort2, ushort3, ushort4
- uint64\_t, uint64\_t2, uint64\_t3, uint64\_t4

Some operations (such as the bitwise operators) only support the integer types.

## Terminology

| **Term** | **Definition** |
|-|-|
| Lane | A single thread of execution. The shader models before version 6.0 expose only one of these at the language level, leaving expansion to parallel SIMD processing entirely up to the implementation. |
| Wave | A set of lanes (threads) executed simultaneously in the processor. No explicit barriers are required to guarantee that they execute in parallel. Similar concepts include "warp" and "wavefront." |
| Inactive Lane | A lane which is not being executed, for example due to the flow of control, or insufficient work to fill the minimum size of the wave. |
| Active Lane | A lane for which execution is being performed. In pixel shaders, it may include any helper pixel lanes. |
| Quad | A set of 4 adjacent lanes corresponding to pixels arranged in a 2x2 square. They are used to estimate gradients by differencing in either x or y. A wave may be comprised of multiple quads. All pixels in an active quad are executed (and may be "Active Lanes"), but those that do not produce visible results are termed "Helper Lanes". |
| Helper Lane | A lane which is executed solely for the purpose of gradients in pixel shader quads. The output of such a lane will be discarded, and so not render to the destination surface. |

## Shading language intrinsics

All the operations of this shader model have been added in a range of intrinsic functions.

### Wave Query

The intrinsics for querying a single wave.

| **Intrinsic** | **Description** | **Pixel shader** | **Compute shader** |
|-|-|-|-|
| [**WaveGetLaneCount**](wavegetlanecount.md) | Returns the number of lanes in the current wave. | \* | \* |
| [**WaveGetLaneIndex**](wavegetlaneindex.md) | Returns the index of the current lane within the current wave. | \* | \* |
| [**WaveIsFirstLane**](waveisfirstlane.md) | Returns true only for the active lane in the current wave with the smallest index | \* | \* |

### Wave Vote

This set of intrinsics compare values across threads currently active from the current wave.

| **Intrinsic** | **Description** | **Pixel shader** | **Compute shader** |
|-|-|-|-|
| [**WaveActiveAnyTrue**](waveanytrue.md) | Returns true if the expression is true in any active lane in the current wave. | \* | \* |
| [**WaveActiveAllTrue**](wavealltrue.md) | Returns true if the expression is true in all active lanes in the current wave. | \* | \* |
| [**WaveActiveBallot**](waveballot.md) | Returns a 64-bit unsigned integer bitmask of the evaluation of the Boolean expression for all active lanes in the specified wave. | \* | \* |

### Wave Broadcast

These intrinsics enable all active lanes in the current wave to receive the value from the specified lane, effectively broadcasting it. The return value from an invalid lane is undefined.

| **Intrinsic** | **Description** | **Pixel shader** | **Compute shader** |
|-|-|-|-|
| [**WaveReadLaneAt**](wavereadlaneat.md) | Returns the value of the expression for the given lane index within the specified wave. | \* | \* |
| [**WaveReadLaneFirst**](wavereadfirstlane.md) | Returns the value of the expression for the active lane of the current wave with the smallest index. | \* | \* |

### Wave Reduction

These intrinsics compute the specified operation across all active lanes in the wave and broadcast the final result to all active lanes. Therefore, the final output is guaranteed uniform across the wave.

| **Intrinsic** | **Description** | **Pixel shader** | **Compute shader** |
|-|-|-|-|
| [**WaveActiveAllEqual**](waveactiveallequal.md) | Returns true if the expression is the same for every active lane in the current wave (and thus uniform across it). | \* | \* |
| [**WaveActiveBitAnd**](waveallbitand.md) | Returns the bitwise AND of all the values of the expression across all active lanes in the current wave, and replicates the result to all lanes in the wave. | \* | \* |
| [**WaveActiveBitOr**](waveallbitor.md) | Returns the bitwise OR of all the values of the expression across all active lanes in the current wave, and replicates the result to all lanes in the wave. | \* | \* |
| [**WaveActiveBitXor**](waveallbitxor.md) | Returns the bitwise Exclusive OR of all the values of the expression across all active lanes in the current wave, and replicates the result to all lanes in the wave. | \* | \* |
| [**WaveActiveCountBits**](waveactivecountbits.md) | Counts the number of boolean variables which evaluate to true across all active lanes in the current wave, and replicates the result to all lanes in the wave. | \* | \* |
| [**WaveActiveMax**](waveallmax.md) | Computes the maximum value of the expression across all active lanes in the current wave, and replicates the result to all lanes in the wave. | \* | \* |
| [**WaveActiveMin**](waveallmin.md) | Computes the minimum value of the expression across all active lanes in the current wave, and replicates the result to all lanes in the wave. | \* | \* |
| [**WaveActiveProduct**](waveallproduct.md) | Multiplies the values of the expression together across all active lanes in the current wave, and replicates the result to all lanes in the wave. | \* | \* |
| [**WaveActiveSum**](waveallsum.md) | Sums up the value of the expression across all active lanes in the current wave and replicates it to all lanes in the current wave, and replicates the result to all lanes in the wave. | \* | \* |

### Wave Scan and Prefix

These intrinsics apply the operation to each lane and leave each partial result of the computation in the corresponding lane.

| **Intrinsic** | **Description** | **Pixel shader** | **Compute shader** |
|-|-|-|-|
| [**WavePrefixCountBits**](waveprefixcountbytes.md) | Returns the sum of all the specified boolean variables set to true across all active lanes with indices smaller than the current lane. | \* | \* |
| [**WavePrefixSum**](waveprefixsum.md) | Returns the sum of all of the values in the active lanes with smaller indices than this one. | \* | \* |
| [**WavePrefixProduct**](waveprefixproduct.md) | Returns the product of all of the values in the lanes before this one of the specified wave. | \* | \* |

### Quad-wide Shuffle operations

These intrinsics perform swap operations on the values across a wave known to contain pixel shader quads as defined here. The indices of the pixels in the quad are defined in scan-line or reading order - where the coordinates within a quad are:

+---------> X 

| [0] [1] 

| [2] [3] 

v 

Y 


These routines work in either compute shaders or pixel shaders. In compute shaders they operate in quads defined as evenly divided groups of 4 within an SIMD wave. In pixel shaders they should be used on waves captured by WaveQuadLanes, otherwise results are undefined.

| **Intrinsic** | **Description** | **Pixel shader** | **Compute shader** |
|-|-|-|-|
| [**QuadReadLaneAt**](quadreadlaneat.md) | Returns the specified source value read from the lane of the current quad identified by quadLaneID \[0..3\] which must be uniform across the quad. | \* | |
| [**QuadReadAcrossDiagonal**](quadreadacrossdiagonal.md) | Returns the specified local value which is read from the diagonally opposite lane in this quad. | \* | |
| [**QuadReadAcrossX**](quadswapx.md) | Returns the specified source value read from the other lane in this quad in the X direction. | \* | |
| [**QuadReadAcrossY**](quadswapy.md) | Returns the specified source value read from the other lane in this quad in the Y direction. | \* | |

## Hardware capability

In order to check that the wave operation features are available on any specific hardware, call [**ID3D12Device::CheckFeatureSupport**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport), noting the description and use of the [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options1) structure.

## Related topics

* [Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
* [Shader Model 6 intrinsics](shader-model-6-0.md)
