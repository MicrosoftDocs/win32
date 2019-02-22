---
title: HLSL Shader Model 6.4
description: Describes the machine learning intrinsics added to HLSL Shader Model 6.4.
ms.topic: article
ms.date: 02/21/2019
---

# HLSL Shader Model 6.4

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Describes the machine learning intrinsics added to HLSL Shader Model 6.4.

## Shader Model 6.0
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
