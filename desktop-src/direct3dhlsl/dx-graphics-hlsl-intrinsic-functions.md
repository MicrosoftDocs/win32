---
title: Intrinsic Functions
description: The following table lists the intrinsic functions available in HLSL. Each function has a brief description, and a link to a reference page that has more detail about the input argument and return type.
ms.assetid: 7f1a3284-6053-4b6d-bd2e-5b33264fe883
keywords:
- Intrinsic Functions HLSL
topic_type:
- apiref
api_name:
- Intrinsic Functions
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Intrinsic Functions

The following table lists the intrinsic functions available in HLSL. Each function has a brief description, and a link to a reference page that has more detail about the input argument and return type.



| Name                                                                                    | Description                                                                                                                                                     | Minimum shader model |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| [**abort**](abort.md)                                                                  | Terminates the current draw or dispatch call being executed.                                                                                                    | 4                    |
| [**abs**](dx-graphics-hlsl-abs.md)                                                     | Absolute value (per component).                                                                                                                                 | 1¹                   |
| [**acos**](dx-graphics-hlsl-acos.md)                                                   | Returns the arccosine of each component of x.                                                                                                                   | 1¹                   |
| [**all**](dx-graphics-hlsl-all.md)                                                     | Test if all components of x are nonzero.                                                                                                                        | 1¹                   |
| [**AllMemoryBarrier**](allmemorybarrier.md)                                            | Blocks execution of all threads in a group until all memory accesses have been completed.                                                                       | 5                    |
| [**AllMemoryBarrierWithGroupSync**](allmemorybarrierwithgroupsync.md)                  | Blocks execution of all threads in a group until all memory accesses have been completed and all threads in the group have reached this call.                   | 5                    |
| [**any**](dx-graphics-hlsl-any.md)                                                     | Test if any component of x is nonzero.                                                                                                                          | 1¹                   |
| [**asdouble**](asdouble.md)                                                            | Reinterprets a cast value into a double.                                                                                                                        | 5                    |
| [**asfloat**](dx-graphics-hlsl-asfloat.md)                                             | Convert the input type to a float.                                                                                                                              | 4                    |
| [**asin**](dx-graphics-hlsl-asin.md)                                                   | Returns the arcsine of each component of x.                                                                                                                     | 1¹                   |
| [**asint**](dx-graphics-hlsl-asint.md)                                                 | Convert the input type to an integer.                                                                                                                           | 4                    |
| [**asuint**](asuint.md)                                                                | Reinterprets the bit pattern of a 64-bit type to a uint.                                                                                                        | 5                    |
| [**asuint**](dx-graphics-hlsl-asuint.md)                                               | Convert the input type to an unsigned integer.                                                                                                                  | 4                    |
| [**atan**](dx-graphics-hlsl-atan.md)                                                   | Returns the arctangent of x.                                                                                                                                    | 1¹                   |
| [**atan2**](dx-graphics-hlsl-atan2.md)                                                 | Returns the arctangent of two values (x,y).                                                                                                                  | 1¹                   |
| [**ceil**](dx-graphics-hlsl-ceil.md)                                                   | Returns the smallest integer which is greater than or equal to x.                                                                                               | 1¹                   |
| [**CheckAccessFullyMapped**](checkaccessfullymapped.md)                                | Determines whether all values from a **Sample** or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). | 5                    |
| [**clamp**](dx-graphics-hlsl-clamp.md)                                                 | Clamps x to the range \[min, max\].                                                                                                                             | 1¹                   |
| [**clip**](dx-graphics-hlsl-clip.md)                                                   | Discards the current pixel, if any component of x is less than zero.                                                                                            | 1¹                   |
| [**cos**](dx-graphics-hlsl-cos.md)                                                     | Returns the cosine of x.                                                                                                                                        | 1¹                   |
| [**cosh**](dx-graphics-hlsl-cosh.md)                                                   | Returns the hyperbolic cosine of x.                                                                                                                             | 1¹                   |
| [**countbits**](countbits.md)                                                          | Counts the number of bits (per component) in the input integer.                                                                                                 | 5                    |
| [**cross**](dx-graphics-hlsl-cross.md)                                                 | Returns the cross product of two 3D vectors.                                                                                                                    | 1¹                   |
| [**D3DCOLORtoUBYTE4**](dx-graphics-hlsl-d3dcolortoubyte4.md)                           | Swizzles and scales components of the 4D vector xto compensate for the lack of UBYTE4 support in some hardware.                                                 | 1¹                   |
| [**ddx**](dx-graphics-hlsl-ddx.md)                                                     | Returns the partial derivative of x with respect to the screen-space x-coordinate.                                                                              | 2¹                   |
| [**ddx\_coarse**](ddx-coarse.md)                                                       | Computes a low precision partial derivative with respect to the screen-space x-coordinate.                                                                      | 5                    |
| [**ddx\_fine**](ddx-fine.md)                                                           | Computes a high precision partial derivative with respect to the screen-space x-coordinate.                                                                     | 5                    |
| [**ddy**](dx-graphics-hlsl-ddy.md)                                                     | Returns the partial derivative of x with respect to the screen-space y-coordinate.                                                                              | 2¹                   |
| [**ddy\_coarse**](ddy-coarse.md)                                                       | Computes a low precision partial derivative with respect to the screen-space y-coordinate.                                                                      | 5                    |
| [**ddy\_fine**](ddy-fine.md)                                                           | Computes a high precision partial derivative with respect to the screen-space y-coordinate.                                                                     | 5                    |
| [**degrees**](dx-graphics-hlsl-degrees.md)                                             | Converts x from radians to degrees.                                                                                                                             | 1¹                   |
| [**determinant**](dx-graphics-hlsl-determinant.md)                                     | Returns the determinant of the square matrix m.                                                                                                                 | 1¹                   |
| [**DeviceMemoryBarrier**](devicememorybarrier.md)                                      | Blocks execution of all threads in a group until all device memory accesses have been completed.                                                                | 5                    |
| [**DeviceMemoryBarrierWithGroupSync**](devicememorybarrierwithgroupsync.md)            | Blocks execution of all threads in a group until all device memory accesses have been completed and all threads in the group have reached this call.            | 5                    |
| [**distance**](dx-graphics-hlsl-distance.md)                                           | Returns the distance between two points.                                                                                                                        | 1¹                   |
| [**dot**](dx-graphics-hlsl-dot.md)                                                     | Returns the dot product of two vectors.                                                                                                                         | 1                    |
| [**dst**](dst.md)                                                                      | Calculates a distance vector.                                                                                                                                   | 5                    |
| [**errorf**](errorf.md)                                                                | Submits an error message to the information queue.                                                                                                              | 4                    |
| [**EvaluateAttributeCentroid**](evaluateattributecentroid.md)                          | Evaluates at the pixel centroid.                                                                                                                                | 5                    |
| [**EvaluateAttributeAtSample**](evaluateattributeatsample.md)                          | Evaluates at the indexed sample location.                                                                                                                       | 5                    |
| [**EvaluateAttributeSnapped**](evaluateattributesnapped.md)                            | Evaluates at the pixel centroid with an offset.                                                                                                                 | 5                    |
| [**exp**](dx-graphics-hlsl-exp.md)                                                     | Returns the base-e exponent.                                                                                                                                    | 1¹                   |
| [**exp2**](dx-graphics-hlsl-exp2.md)                                                   | Base 2 exponent (per component).                                                                                                                                | 1¹                   |
| [**f16tof32**](f16tof32.md)                                                            | Converts the float16 stored in the low-half of the uint to a float.                                                                                             | 5                    |
| [**f32tof16**](f32tof16.md)                                                            | Converts an input into a float16 type.                                                                                                                          | 5                    |
| [**faceforward**](dx-graphics-hlsl-faceforward.md)                                     | Returns -n \* sign(dot(i, ng)).                                                                                                                                 | 1¹                   |
| [**firstbithigh**](firstbithigh.md)                                                    | Gets the location of the first set bit starting from the highest order bit and working downward, per component.                                                 | 5                    |
| [**firstbitlow**](firstbitlow.md)                                                      | Returns the location of the first set bit starting from the lowest order bit and working upward, per component.                                                 | 5                    |
| [**floor**](dx-graphics-hlsl-floor.md)                                                 | Returns the greatest integer which is less than or equal to x.                                                                                                  | 1¹                   |
| [**fma**](dx-graphics-hlsl-fma.md)                                                     | Returns the double-precision fused multiply-addition of a \* b + c.                                                                                             | 5                    |
| [**fmod**](dx-graphics-hlsl-fmod.md)                                                   | Returns the floating point remainder of x/y.                                                                                                                    | 1¹                   |
| [**frac**](dx-graphics-hlsl-frac.md)                                                   | Returns the fractional part of x.                                                                                                                               | 1¹                   |
| [**frexp**](dx-graphics-hlsl-frexp.md)                                                 | Returns the mantissa and exponent of x.                                                                                                                         | 2¹                   |
| [**fwidth**](dx-graphics-hlsl-fwidth.md)                                               | Returns abs(ddx(x)) + abs(ddy(x))                                                                                                                               | 2¹                   |
| [**GetRenderTargetSampleCount**](dx-graphics-hlsl-getrendertargetsamplecount.md)       | Returns the number of render-target samples.                                                                                                                    | 4                    |
| [**GetRenderTargetSamplePosition**](dx-graphics-hlsl-getrendertargetsampleposition.md) | Returns a sample position (x,y) for a given sample index.                                                                                                       | 4                    |
| [**GroupMemoryBarrier**](groupmemorybarrier.md)                                        | Blocks execution of all threads in a group until all group shared accesses have been completed.                                                                 | 5                    |
| [**GroupMemoryBarrierWithGroupSync**](groupmemorybarrierwithgroupsync.md)              | Blocks execution of all threads in a group until all group shared accesses have been completed and all threads in the group have reached this call.             | 5                    |
| [**InterlockedAdd**](interlockedadd.md)                                                | Performs a guaranteed atomic add of value to the dest resource variable.                                                                                        | 5                    |
| [**InterlockedAnd**](interlockedand.md)                                                | Performs a guaranteed atomic and.                                                                                                                               | 5                    |
| [**InterlockedCompareExchange**](interlockedcompareexchange.md)                        | Atomically compares the input to the comparison value and exchanges the result.                                                                                 | 5                    |
| [**InterlockedCompareStore**](interlockedcomparestore.md)                              | Atomically compares the input to the comparison value.                                                                                                          | 5                    |
| [**InterlockedExchange**](interlockedexchange.md)                                      | Assigns value to dest and returns the original value.                                                                                                           | 5                    |
| [**InterlockedMax**](interlockedmax.md)                                                | Performs a guaranteed atomic max.                                                                                                                               | 5                    |
| [**InterlockedMin**](interlockedmin.md)                                                | Performs a guaranteed atomic min.                                                                                                                               | 5                    |
| [**InterlockedOr**](interlockedor.md)                                                  | Performs a guaranteed atomic or.                                                                                                                                | 5                    |
| [**InterlockedXor**](interlockedxor.md)                                                | Performs a guaranteed atomic xor.                                                                                                                               | 5                    |
| [**isfinite**](dx-graphics-hlsl-isfinite.md)                                           | Returns true if x is finite, false otherwise.                                                                                                                   | 1¹                   |
| [**isinf**](dx-graphics-hlsl-isinf.md)                                                 | Returns true if x is +INF or -INF, false otherwise.                                                                                                             | 1¹                   |
| [**isnan**](dx-graphics-hlsl-isnan.md)                                                 | Returns true if x is NAN or QNAN, false otherwise.                                                                                                              | 1¹                   |
| [**ldexp**](dx-graphics-hlsl-ldexp.md)                                                 | Returns x \* 2exp                                                                                                                                               | 1¹                   |
| [**length**](dx-graphics-hlsl-length.md)                                               | Returns the length of the vector v.                                                                                                                             | 1¹                   |
| [**lerp**](dx-graphics-hlsl-lerp.md)                                                   | Returns x + s(y - x).                                                                                                                                           | 1¹                   |
| [**lit**](dx-graphics-hlsl-lit.md)                                                     | Returns a lighting vector (ambient, diffuse, specular, 1)                                                                                                       | 1¹                   |
| [**log**](dx-graphics-hlsl-log.md)                                                     | Returns the base-e logarithm of x.                                                                                                                              | 1¹                   |
| [**log10**](dx-graphics-hlsl-log10.md)                                                 | Returns the base-10 logarithm of x.                                                                                                                             | 1¹                   |
| [**log2**](dx-graphics-hlsl-log2.md)                                                   | Returns the base-2 logarithm of x.                                                                                                                              | 1¹                   |
| [**mad**](mad.md)                                                                      | Performs an arithmetic multiply/add operation on three values.                                                                                                  | 5                    |
| [**max**](dx-graphics-hlsl-max.md)                                                     | Selects the greater of x and y.                                                                                                                                 | 1¹                   |
| [**min**](dx-graphics-hlsl-min.md)                                                     | Selects the lesser of x and y.                                                                                                                                  | 1¹                   |
| [**modf**](dx-graphics-hlsl-modf.md)                                                   | Splits the value x into fractional and integer parts.                                                                                                           | 1¹                   |
| [**msad4**](dx-graphics-hlsl-msad4.md)                                                 | Compares a 4-byte reference value and an 8-byte source value and accumulates a vector of 4 sums.                                                                | 5                    |
| [**mul**](dx-graphics-hlsl-mul.md)                                                     | Performs matrix multiplication using x and y.                                                                                                                   | 1                    |
| [**noise**](dx-graphics-hlsl-noise.md)                                                 | Generates a random value using the Perlin-noise algorithm.                                                                                                      | 1¹                   |
| [**normalize**](dx-graphics-hlsl-normalize.md)                                         | Returns a normalized vector.                                                                                                                                    | 1¹                   |
| [**pow**](dx-graphics-hlsl-pow.md)                                                     | Returns x<sup>y</sup>.                                                                                                                                          | 1¹                   |
| [**printf**](printf.md)                                                                | Submits a custom shader message to the information queue.                                                                                                       | 4                    |
| [**Process2DQuadTessFactorsAvg**](process2dquadtessfactorsavg.md)                      | Generates the corrected tessellation factors for a quad patch.                                                                                                  | 5                    |
| [**Process2DQuadTessFactorsMax**](process2dquadtessfactorsmax.md)                      | Generates the corrected tessellation factors for a quad patch.                                                                                                  | 5                    |
| [**Process2DQuadTessFactorsMin**](process2dquadtessfactorsmin.md)                      | Generates the corrected tessellation factors for a quad patch.                                                                                                  | 5                    |
| [**ProcessIsolineTessFactors**](processisolinetessfactors.md)                          | Generates the rounded tessellation factors for an isoline.                                                                                                      | 5                    |
| [**ProcessQuadTessFactorsAvg**](processquadtessfactorsavg.md)                          | Generates the corrected tessellation factors for a quad patch.                                                                                                  | 5                    |
| [**ProcessQuadTessFactorsMax**](processquadtessfactorsmax.md)                          | Generates the corrected tessellation factors for a quad patch.                                                                                                  | 5                    |
| [**ProcessQuadTessFactorsMin**](processquadtessfactorsmin.md)                          | Generates the corrected tessellation factors for a quad patch.                                                                                                  | 5                    |
| [**ProcessTriTessFactorsAvg**](processtritessfactorsavg.md)                            | Generates the corrected tessellation factors for a tri patch.                                                                                                   | 5                    |
| [**ProcessTriTessFactorsMax**](processtritessfactorsmax.md)                            | Generates the corrected tessellation factors for a tri patch.                                                                                                   | 5                    |
| [**ProcessTriTessFactorsMin**](processtritessfactorsmin.md)                            | Generates the corrected tessellation factors for a tri patch.                                                                                                   | 5                    |
| [**radians**](dx-graphics-hlsl-radians.md)                                             | Converts x from degrees to radians.                                                                                                                             | 1                    |
| [**rcp**](rcp.md)                                                                      | Calculates a fast, approximate, per-component reciprocal.                                                                                                       | 5                    |
| [**reflect**](dx-graphics-hlsl-reflect.md)                                             | Returns a reflection vector.                                                                                                                                    | 1                    |
| [**refract**](dx-graphics-hlsl-refract.md)                                             | Returns the refraction vector.                                                                                                                                  | 1¹                   |
| [**reversebits**](reversebits.md)                                                      | Reverses the order of the bits, per component.                                                                                                                  | 5                    |
| [**round**](dx-graphics-hlsl-round.md)                                                 | Rounds x to the nearest integer                                                                                                                                 | 1¹                   |
| [**rsqrt**](dx-graphics-hlsl-rsqrt.md)                                                 | Returns 1 / sqrt(x)                                                                                                                                             | 1¹                   |
| [**saturate**](dx-graphics-hlsl-saturate.md)                                           | Clamps x to the range \[0, 1\]                                                                                                                                  | 1                    |
| [**sign**](dx-graphics-hlsl-sign.md)                                                   | Computes the sign of x.                                                                                                                                         | 1¹                   |
| [**sin**](dx-graphics-hlsl-sin.md)                                                     | Returns the sine of x                                                                                                                                           | 1¹                   |
| [**sincos**](dx-graphics-hlsl-sincos.md)                                               | Returns the sine and cosine of x.                                                                                                                               | 1¹                   |
| [**sinh**](dx-graphics-hlsl-sinh.md)                                                   | Returns the hyperbolic sine of x                                                                                                                                | 1¹                   |
| [**smoothstep**](dx-graphics-hlsl-smoothstep.md)                                       | Returns a smooth Hermite interpolation between 0 and 1.                                                                                                         | 1¹                   |
| [**sqrt**](dx-graphics-hlsl-sqrt.md)                                                   | Square root (per component)                                                                                                                                     | 1¹                   |
| [**step**](dx-graphics-hlsl-step.md)                                                   | Returns (x >= a) ? 1 : 0                                                                                                                                     | 1¹                   |
| [**tan**](dx-graphics-hlsl-tan.md)                                                     | Returns the tangent of x                                                                                                                                        | 1¹                   |
| [**tanh**](dx-graphics-hlsl-tanh.md)                                                   | Returns the hyperbolic tangent of x                                                                                                                             | 1¹                   |
| [**tex1D(s, t)**](dx-graphics-hlsl-tex1d.md)                                           | 1D texture lookup.                                                                                                                                              | 1                    |
| [**tex1D(s, t, ddx, ddy)**](dx-graphics-hlsl-tex1d-s-t-ddx-ddy.md)                     | 1D texture lookup.                                                                                                                                              | 2¹                   |
| [**tex1Dbias**](dx-graphics-hlsl-tex1dbias.md)                                         | 1D texture lookup with bias.                                                                                                                                    | 2¹                   |
| [**tex1Dgrad**](dx-graphics-hlsl-tex1dgrad.md)                                         | 1D texture lookup with a gradient.                                                                                                                              | 2¹                   |
| [**tex1Dlod**](dx-graphics-hlsl-tex1dlod.md)                                           | 1D texture lookup with LOD.                                                                                                                                     | 3¹                   |
| [**tex1Dproj**](dx-graphics-hlsl-tex1dproj.md)                                         | 1D texture lookup with projective divide.                                                                                                                       | 2¹                   |
| [**tex2D(s, t)**](dx-graphics-hlsl-tex2d.md)                                           | 2D texture lookup.                                                                                                                                              | 1¹                   |
| [**tex2D(s, t, ddx, ddy)**](dx-graphics-hlsl-tex2d-s-t-ddx-ddy.md)                     | 2D texture lookup.                                                                                                                                              | 2¹                   |
| [**tex2Dbias**](dx-graphics-hlsl-tex2dbias.md)                                         | 2D texture lookup with bias.                                                                                                                                    | 2¹                   |
| [**tex2Dgrad**](dx-graphics-hlsl-tex2dgrad.md)                                         | 2D texture lookup with a gradient.                                                                                                                              | 2¹                   |
| [**tex2Dlod**](dx-graphics-hlsl-tex2dlod.md)                                           | 2D texture lookup with LOD.                                                                                                                                     | 3                    |
| [**tex2Dproj**](dx-graphics-hlsl-tex2dproj.md)                                         | 2D texture lookup with projective divide.                                                                                                                       | 2¹                   |
| [**tex3D(s, t)**](dx-graphics-hlsl-tex3d.md)                                           | 3D texture lookup.                                                                                                                                              | 1¹                   |
| [**tex3D(s, t, ddx, ddy)**](dx-graphics-hlsl-tex3d-s-t-ddx-ddy.md)                     | 3D texture lookup.                                                                                                                                              | 2¹                   |
| [**tex3Dbias**](dx-graphics-hlsl-tex3dbias.md)                                         | 3D texture lookup with bias.                                                                                                                                    | 2¹                   |
| [**tex3Dgrad**](dx-graphics-hlsl-tex3dgrad.md)                                         | 3D texture lookup with a gradient.                                                                                                                              | 2¹                   |
| [**tex3Dlod**](dx-graphics-hlsl-tex3dlod.md)                                           | 3D texture lookup with LOD.                                                                                                                                     | 3¹                   |
| [**tex3Dproj**](dx-graphics-hlsl-tex3dproj.md)                                         | 3D texture lookup with projective divide.                                                                                                                       | 2¹                   |
| [**texCUBE(s, t)**](dx-graphics-hlsl-texcube.md)                                       | Cube texture lookup.                                                                                                                                            | 1¹                   |
| [**texCUBE(s, t, ddx, ddy)**](dx-graphics-hlsl-texcube-s-t-ddx-ddy.md)                 | Cube texture lookup.                                                                                                                                            | 2¹                   |
| [**texCUBEbias**](dx-graphics-hlsl-texcubebias.md)                                     | Cube texture lookup with bias.                                                                                                                                  | 2¹                   |
| [**texCUBEgrad**](dx-graphics-hlsl-texcubegrad.md)                                     | Cube texture lookup with a gradient.                                                                                                                            | 2¹                   |
| [**texCUBElod**](dx-graphics-hlsl-texcubelod.md)                                       | Cube texture lookup with LOD.                                                                                                                                   | 3¹                   |
| [**texCUBEproj**](dx-graphics-hlsl-texcubeproj.md)                                     | Cube texture lookup with projective divide.                                                                                                                     | 2¹                   |
| [**transpose**](dx-graphics-hlsl-transpose.md)                                         | Returns the transpose of the matrix m.                                                                                                                          | 1                    |
| [**trunc**](dx-graphics-hlsl-trunc.md)                                                 | Truncates floating-point value(s) to integer value(s)                                                                                                           | 1                    |
| [**NonUniformResourceIndex**](NonUniformResourceIndex.md)          | Ensures non-uniform indexing for resources like textures in shaders | 6.0    |
| [**AddUint64**](AddUint64.md)                                      | Unsigned add of 32-bit operand with the carry |  6.0   |
| [**GetAttributeAtVertex**](GetAttributeAtVertex.md)                | Returns the values of the attributes at the vertex | 6.1 |
| [**asfloat16**](GetAttributeAtVertex.md)                           | Converts integer bit patterns to half-precision floating-point values. | 6.2 |
| [**asint16**](asint16.md)                                          | Converts bit patterns to 16-bit integer values. | 6.2 |
| [**asuint16**](asuint16.md)                                        | Converts bit patterns to 16-bit unsigned integer values.| 6.2 |
| [**WaveGetLaneCount**](wavegetlanecount.md)                        | Returns the number of lanes in the current wave. | 6.0 |
| [**WaveGetLaneIndex**](wavegetlaneindex.md)                        | Returns the index of the current lane within its wave. | 6.0 |
| [**WaveIsFirstLane**](waveisfirstlane.md)                          | Checks if the current lane is the first lane in its wave. | 6.0 |
| [**WaveActiveAnyTrue**](waveanytrue.md)                            | Returns true if any lane in the wave evaluates to true. | 6.0 |
| [**WaveActiveAllTrue**](wavealltrue.md)                            | Returns true if all lanes in the wave evaluate to true. | 6.0 |
| [**WaveActiveBallot**](waveballot.md)                              | Returns a bitmask where each bit represents if the condition is true for each lane. | 6.0 |
| [**WaveReadLaneAt**](wavereadlaneat.md)                            | Reads the value of a specific lane within the wave using an index. | 6.0 |
| [**WaveReadLaneFirst**](wavereadfirstlane.md)                      | Reads the value from the first lane in the current wave. | 6.0 |
| [**WaveActiveAllEqual**](waveactiveallequal.md)                    | Checks if all lanes in the wave have equal values. | 6.0 |
| [**WaveActiveBitAnd**](waveallbitand.md)                           | Performs a bitwise AND operation across all lanes in the wave and returns the result. | 6.0 |
| [**WaveActiveBitOr**](waveallbitor.md)                             | Performs a bitwise OR operation across all lanes in the wave and returns the result. | 6.0 |
| [**WaveActiveBitXor**](waveallbitxor.md)                           | Performs a bitwise XOR operation across all lanes in the wave and returns the result. | 6.0 |
| [**WaveActiveCountBits**](waveactivecountbits.md)                  | Counts the number of active lanes (lanes where the condition is true) in the wave. | 6.0 |
| [**WaveActiveMax**](waveallmax.md)                                 | Returns the maximum value among all active lanes in the wave. | 6.0 |
| [**WaveActiveMin**](waveallmin.md)                                 | Returns the minimum value among all active lanes in the wave. | 6.0 |
| [**WaveActiveProduct**](waveallproduct.md)                         | Computes the product of values across all active lanes in the wave. | 6.0 |
| [**WaveActiveSum**](waveallsum.md)                                 | Computes the sum of values across all active lanes in the wave.| 6.0 |
| [**WavePrefixCountBits**](waveprefixcountbytes.md)                 | Computes the prefix count of active bits up to the current lane in the wave. | 6.0 |
| [**WavePrefixSum**](waveprefixsum.md)                              | Computes the prefix sum up to the current lane in the wave. | 6.0 |
| [**WavePrefixProduct**](waveprefixproduct.md)                      | Computes the prefix product up to the current lane in the wave. | 6.0 |
| [**QuadReadLaneAt**](quadreadlaneat.md)                            | Reads the value of a specific lane within the quad using an index. | 6.0 |
| [**QuadReadAcrossDiagonal**](quadreadacrossdiagonal.md)            | Reads values across the diagonal of a quad group. | 6.0 |
| [**QuadReadAcrossX**](quadswapx.md)                                | Reads values across the X axis of a quad group. | 6.0 |
| [**QuadReadAcrossY**](quadswapy.md)                                | Reads values across the Y axis of a quad group.| 6.0 |
| [**dot4add_u8packed**](dot4add_u8packed.md)                        | Unsigned dot product of 4 x u8 vectors packed into i32, with accumulate to i32.	| 6.4 |
| [**dot4add_i8packed**](dot4add_i8packed.md)                        | Signed dot product of 4 x i8 vectors packed into i32, with accumulate to i32. | 6.4 |
| [**dot2add**](dot2add.md)                                          | 2D half dot product with accumulate to float. | 6.4 |
| [**WaveMultiPrefixCountBits**](WaveMultiPrefixCountBits.md)        | Returns the count of bits set to 1 on groups of lanes identified by a bitmask.	| 6.5 |
| [**WaveMultiPrefixProduct**](WaveMultiPrefixProduct.md)            | Returns the result of the operation on groups of lanes identified by a bitmask. | 6.5 |
| [**WaveMatch**](WaveMatch.md)                                      | Checks if all lanes in the wave have the same value. | 6.5 |
| [**WaveMultiPrefixBitAnd**](WaveMultiPrefixBitAnd.md)              | Performs a multi-wave prefix AND operation across all lanes in the wave and returns the result. | 6.5 |
| [**WaveMultiPrefixBitOr**](WaveMultiPrefixBitOr.md)                | Performs a multi-wave prefix OR operation across all lanes in the wave and returns the result. | 6.5 |
| [**WaveMultiPrefixBitXor**](WaveMultiPrefixBitXor.md)              | Performs a multi-wave prefix XOR operation across all lanes in the wave and returns the result. | 6.5 |
| [**WaveMultiPrefixSum**](WaveMultiPrefixSum.md)                    | Performs a multi-wave prefix sum operation across all lanes in the wave and returns the result.| 6.5 |
| [**IsHelperLane**](IsHelperLane.md)                                | Returns true on helper lanes in pixel shaders. | 6.6 |
| [**QuadAny**](QuadAny.md)                                          | Compares boolean accross a quad. | 6.7 |
| [**QuadAll**](QuadAll.md)                                          | Compares boolean accross a quad. | 6.7 |
| [**TraceRay**](../direct3d12/traceray-function.md)                 | Initiates ray tracing, allowing intersection testing and tracing rays into the scene geometry. | 6.6 |
| [**ReportHit**](../direct3d12/reporthit-function.md)               | Used to report a hit when a ray intersects with geometry to record info about the intersection. | 6.6 |
| [**CallShader**](../direct3d12/callshader-function.md)             | Used to invoke a callable shader, allowing shaders to be modular and reusable within a ray tracing pipeline. | 6.6 |
| [**IgnoreHit**](../direct3d12/ignorehit-function.md)               | Used to skip uneeded calculations by indicating a hit should be ignored or not processed further. | 6.6 |
| [**AcceptHitAndEndSearch**](../direct3d12/accepthitandendsearch-function.md) | Used to indicate that a hit has been accepted and to terminate further intersection testing. | 6.6 |
| [**DispatchRaysIndex**](../direct3d12/dispatchraysindex.md)            | Used to dispatch rays with an index indicating the starting point for ray dispatch. | 6.6 |
| [**DispatchRaysDimensions**](../direct3d12/dispatchraysdimensions.md)  | Used to dispatch rays specifying the dimensions (width and height) for the ray dispatch. | 6.6 |
| [**WorldRayOrigin**](../direct3d12/worldrayorigin.md)                  | Represents the origin point of a ray in world coordinates. | 6.6 |
| [**WorldRayDirection**](../direct3d12/worldraydirection.md)            | Represents the direction vector of a ray in world coordinates. | 6.6 |
| [**ObjectRayOrigin**](../direct3d12/objectrayorigin.md)                | Origin of a ray in object-local coordinates, used in ray tracing shaders | 6.6 |
| [**ObjectRayDirection**](../direct3d12/objectraydirection.md)          | Direction of a ray in object-local coordinates, used in ray tracing shaders. | 6.6 |
| [**RayTMin**](../direct3d12/raytmin.md)                                | Minimum t-value along a ray's direction, used in ray tracing shaders. | 6.6 |
| [**RayTCurrent**](../direct3d12/raytcurrent.md)                        | Current t-value along a ray's direction, used in ray tracing shaders. | 6.6 |
| [**PrimitiveIndex**](../direct3d12/primitiveindex.md)                  | Index of the primitive being processed, used in geometry shaders. | 6.6 |
| [**InstanceID**](../direct3d12/instanceid.md)                          | ID of the instance being processed, used in instanced rendering. | 6.6 |
| [**InstanceIndex**](../direct3d12/instanceindex.md)                    | Index of the instance being processed, used in instanced rendering. | 6.6 |
| [**GeometryIndex**](../direct3d12/geometryindex.md)                    | Index of the geometry being processed, used in geometry shaders. | 6.6 |
| [**HitKind**](../direct3d12/hitkind.md)                                | Hit result reported in a ray tracing shader, indicating what type of intersection was found. | 6.6 |
| [**RayFlags**](../direct3d12/rayflags.md)                              | Represents flags associated with a ray, used to convey how the ray should be processed. | 6.6 |
| [**ObjectToWorld3x4**](../direct3d12/objecttoworld3x4.md)              | Represents a 3x4 matrix used to transform coordinates from object-local space to world space. | 6.6 |
| [**WorldToObject3x4**](../direct3d12/worldtoobject3x4.md)              | Represents a 3x4 matrix used to transform coordinates from world space to object-local space. | 6.6 |
| [**ObjectToWorld4x3**](../direct3d12/objecttoworld4x3.md)              | Represents a 4x3 matrix used to transform coordinates from object-local space to world space. | 6.6 |
| [**WorldToObject4x3**](../direct3d12/worldtoobject4x3.md)              | Represents a 4x3 matrix used to transform coordinates from world space to object-local space. | 6.6 |
| [**ObjectToWorld**](ObjectToWorld.md)                                  | Converts object-space coordinates to world-space. | 6.6 |
| [**WorldToObject**](WorldToObject.md)                                  | Converts world-space coordinates to object-space. | 6.6 |
| [**InterlockedCompareStoreFloatBitwise**](InterlockedCompareStoreFloatBitwise.md)       | Atomic compare and store for floats. | 6.6 |
| [**InterlockedCompareExchangeFloatBitwise**](InterlockedCompareExchangeFloatBitwise.md) | Atomic compare and exchange for floats. | 6.6 |
| [**unpack_s8s16**](unpack_s8s16.md)                                    | Unpacks a signed 8-bit value into a signed 16-bit value. | 6.6 |
| [**unpack_u8u16**](unpack_u8u16.md)                                    | Unpacks an unsigned 8-bit value into an unsigned 16-bit value. | 6.6 |
| [**unpack_s8s32**](unpack_s8s32.md)                                    | Unpacks a signed 8-bit value into a signed 32-bit value. | 6.6 |
| [**unpack_u8u32**](unpack_u8u32.md)                                    | Unpacks an unsigned 8-bit value into an unsigned 32-bit value. | 6.6 |
| [**pack_s8**](pack_s8.md)                                              | Packs a signed 8-bit value. | 6.6 |
| [**pack_u8**](pack_u8.md)                                              | Packs an unsigned 8-bit value. | 6.6 |
| [**pack_clamp_s8**](pack_clamp_s8.md)                                  | Packs and clamps a signed 8-bit value. | 6.6 |
| [**pack_clamp_u8**](pack_clamp_u8.md)                                  | Packs and clamps an unsigned 8-bit value.| 6.6 |
| [**SetMeshOutputCounts**](../direct3d12/setmeshoutputcounts.md)        | Is used to set the output counts for different types of mesh primitives in geometry shaders. | 6.5 |
| [**DispatchMesh**](DispatchMesh.md)                                    | Is used to dispatch mesh shader threads for processing mesh primitives. | 6.5 |
| [**AllocateRayQuery**](AllocateRayQuery.md)                            | Allocates resources for ray queries in ray tracing shaders. | 6.5 |
| [**CreateResourceFromHeap**](CreateResourceFromHeap.md)                | Creates a resource from a heap, typically used for dynamic resource allocation. | 6.6 |
| [**and**](and.md)                                                      | A replacement for logical `and` for vector and matrix types.| HLSL 2021 |
| [**or**](or.md)                                                        | A replacement for logical `or` for vector and matrix types.| HLSL 2021 |
| [**select**](select.md)                                                | A conditional selection function that chooses between two values based on a condition. | HLSL 2021 |
| [**Barrier**](Barrier.md)                                              | Request a barrier for a set of memory types and/or thread group execution sync | 6.8 |
| [**GetRemainingRecursionLevels**](GetRemainingRecursionLevels.md)      | Returns how many levels of recursion remain | 6.8 |



 

¹ see reference page for restrictions.

## Component and Template Types

The HLSL intrinsic function declarations use component types and template types for input parameter arguments and return values. The available types are listed in the following table.



| These Template Types | Description                                           | Support These Data Types                                        |
|----------------------|-------------------------------------------------------|-----------------------------------------------------------------|
| matrix               | up to 16 components depending on the declaration      | [Basic HLSL Types](dx-graphics-hlsl-data-types.md)             |
| object               | sampler object                                        | *sampler*, *sampler1D*, *sampler2D*, *sampler3D*, *samplerCUBE* |
| scalar               | 1 component                                           | [Basic HLSL Types](dx-graphics-hlsl-data-types.md)             |
| vector               | 1 component minimum, 4 components maximum (inclusive) | [Basic HLSL Types](dx-graphics-hlsl-data-types.md)             |



 

## See also

<dl> <dt>

[Reference for HLSL](dx-graphics-hlsl-reference.md)
</dt> </dl>

 

 