---
title: Shader Model 6
description: Shader model 6.0 adds a range of wave operation intrinsics for the pixel and compute shaders.
ms.assetid: 2F28F86D-F599-47EA-90D7-6833ABA976FC
ms.topic: article
ms.date: 05/31/2018
---

# Shader Model 6

All non-quad related Wave Intrinsics are available in all shader stages. Quad wave intrinsics are available only in pixel and compute shaders.

## In this section



| Topic                                                                 | Description                                                                                                                                                               |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**QuadReadAcrossDiagonal**](quadreadacrossdiagonal.md)<br/> | Returns the specified local value which is read from the diagonally opposite lane in this quad.<br/>                                                                |
| [**QuadReadLaneAt**](quadreadlaneat.md)<br/>                   | Returns the specified source value from the lane identified by the lane ID within the current quad.<br/>                                                            |
| [**QuadReadAcrossX**](quadswapx.md)<br/>                      | Returns the specified local value read from the other lane in this quad in the X direction.<br/>                                                                    |
| [**QuadReadAcrossY**](quadswapy.md)<br/>                      | Returns the specified source value read from the other lane in this quad in the Y direction.<br/>                                                                   |
| [**WaveActiveAllEqual**](waveactiveallequal.md)<br/>           | Returns true if the expression is the same for every active lane in the current wave (and thus uniform across it).<br/>                                             |
| [**WaveActiveBitAnd**](waveallbitand.md)<br/>                  | Returns the bitwise AND of all the values of the expression across all active lanes in the current wave and replicates it back to all active lanes. <br/>           |
| [**WaveActiveBitOr**](waveallbitor.md)<br/>                    | Returns the bitwise OR of all the values of the expression across all active lanes in the current wave and replicates it back to all active lanes. <br/>            |
| [**WaveActiveBitXor**](waveallbitxor.md)<br/>                  | Returns the bitwise XOR of all the values of the expression across all active lanes in the current wave and replicates it back to all active lanes. <br/>           |
| [**WaveActiveCountBits**](waveactivecountbits.md)<br/>         | Counts the number of boolean variables which evaluate to true across all active lanes in the current wave, and replicates the result to all lanes in the wave.<br/> |
| [**WaveActiveMax**](waveallmax.md)<br/>                        | Returns the maximum value of the expression across all active lanes in the current wave and replicates it back to all active lanes. <br/>                           |
| [**WaveActiveMin**](waveallmin.md)<br/>                        | Returns the minimum value of the expression across all active lanes in the current wave replicates it back to all active lanes. <br/>                               |
| [**WaveActiveProduct**](waveallproduct.md)<br/>                | Multiplies the values of the expression together across all active lanes in the current wave and replicates it back to all active lanes.<br/>                       |
| [**WaveActiveSum**](waveallsum.md)<br/>                        | Sums up the value of the expression across all active lanes in the current wave and replicates it to all lanes in the current wave.<br/>                            |
| [**WaveActiveAllTrue**](wavealltrue.md)<br/>                   | Returns true if the expression is true in all active lanes in the current wave.<br/>                                                                                |
| [**WaveActiveAnyTrue**](waveanytrue.md)<br/>                   | Returns true if the expression is true in any of the active lanes in the current wave.<br/>                                                                         |
| [**WaveActiveBallot**](waveballot.md)<br/>                     | Returns a 4-bit unsigned integer bitmask of the evaluation of the Boolean expression for all active lanes in the specified wave. <br/>                              |
| [**WaveGetLaneCount**](wavegetlanecount.md)<br/>               | Returns the number of lanes in a wave on this architecture. <br/>                                                                                                   |
| [**WaveGetLaneIndex**](wavegetlaneindex.md)<br/>               | Returns the index of the current lane within the current wave. <br/>                                                                                                |
| [**WaveIsFirstLane**](waveisfirstlane.md)<br/>                 | Returns true only for the active lane in the current wave with the smallest index. <br/>                                                                            |
| [**WavePrefixCountBits**](waveprefixcountbytes.md)<br/>        | Returns the sum of all the specified boolean variables set to true across all active lanes with indices smaller than the current lane. <br/>                        |
| [**WavePrefixProduct**](waveprefixproduct.md)<br/>             | Returns the product of all of the values in the active lanes in this wave with indices less than this lane.<br/>                                                    |
| [**WavePrefixSum**](waveprefixsum.md)<br/>                     | Returns the sum of all of the values in the active lanes with smaller indices than this one.<br/>                                                                   |
| [**WaveReadLaneFirst**](wavereadfirstlane.md)<br/>             | Returns the value of the expression for the active lane of the current wave with the smallest index. <br/>                                                          |
| [**WaveReadLaneAt**](wavereadlaneat.md)<br/>                   | Returns the value of the expression for the given lane index within the specified wave.<br/>                                                                        |



 

## Related topics

<dl> <dt>

[Overview of Shader Model 6](hlsl-shader-model-6-0-features-for-direct3d-12.md)
</dt> <dt>

[Shader Models vs Shader Profiles](dx-graphics-hlsl-models.md)
</dt> </dl>

 

 





