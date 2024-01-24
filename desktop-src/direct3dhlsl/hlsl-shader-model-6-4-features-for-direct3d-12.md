---
title: HLSL Shader Model 6.4
description: Describes the machine learning intrinsics added to HLSL Shader Model 6.4.
ms.topic: article
ms.date: 02/21/2019
---

# HLSL Shader Model 6.4

Describes the machine learning intrinsics added to HLSL Shader Model 6.4.

## Shader Model 6.4
These intrinsics are a required/supported feature of Shader model 6.4. Consequently, no separate capability bit check is required, beyond assuring the use of Shader Model 6.4. The minimum supported client for these routines is Windows 10, version 1903.

## Shading language intrinsics

### Unsigned Integer Dot-Product of 4 Elements and Accumulate
```syntax
uint32 dot4add_u8packed(uint32 a, uint32 b, uint32 acc); // ubyte4 a, b;
```
 
A 4-dimensional unsigned integer dot-product with add. Multiplies together each corresponding pair of unsigned 8-bit int bytes in the two input DWORDs, and sums the results into the 32-bit unsigned integer accumulator. This instruction operates within a single 32-bit wide SIMD lane. The inputs are also assumed to be 32-bit quantities.
 
### Signed Integer Dot-Product of 4 Elements and Accumulate
```syntax
int32 dot4add_i8packed(uint32 a, uint32 b, int32 acc); // signed byte4 a, b;
```

A 4-dimensional signed integer dot-product with add. Multiplies together each corresponding pair of signed 8-bit int bytes in the two input DWORDs, and sums the results into the 32-bit signed integer accumulator. This instruction operates within a single 32-bit wide SIMD lane. The inputs are also assumed to be 32-bit quantities.
 
### Single Precision Floating Point 2-Element Dot-Product and Accumulate
```syntax
float dot2add( half2 a, half2 b, float acc );
```

A 2-dimensional floating point dot-product of half2 vectors with add. Multiplies the elements of the two half-precision float input vectors together and sums the results into the 32-bit float accumulator. This instructions operates within a single 32-bit wide SIMD lane. The inputs are 16-bit quantities packed into the same lane.

This is covered under the low-precision feature bit (indicating that native half and short support are present).

### SV_ShadingRate
```syntax
uint shadingRate : SV_ShadingRate
```

An unsigned integer representing how many target pixels are written by each invocation of the pixel shader. Valid values belong to set of enumeration values [D3D12_SHADING_RATE](/windows/win32/api/d3d12/ne-d3d12-d3d12_shading_rate).

This system value is available on platforms that are [D3D12_VARIABLE_SHADING_RATE_TIER_2](/windows/win32/api/d3d12/ne-d3d12-d3d12_variable_shading_rate_tier) or higher. It can be written from at most one of vertex or geometry shader stages. It can be read from the pixel shader stage. For more information, see the [Variable-rate Shading](../direct3d12/vrs.md).