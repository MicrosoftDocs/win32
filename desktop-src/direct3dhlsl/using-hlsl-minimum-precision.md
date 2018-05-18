---
title: Using HLSL minimum precision
description: Starting with Windows 8, graphics drivers can implement minimum precision HLSL scalar data types by using any precision greater than or equal to their specified bit precision.
ms.assetid: '422B0C45-5CEB-4235-AD05-62D36C36CFC6'
---

# Using HLSL minimum precision

Starting with Windows 8, graphics drivers can implement minimum precision [HLSL scalar data types](dx-graphics-hlsl-scalar.md) by using any precision greater than or equal to their specified bit precision. When your HLSL minimum precision shader code is used on hardware that implements HLSL minimum precision, you use less memory bandwidth and as a result you also use less system power.

You can query for the minimum precision support that the graphics driver provides by calling [**ID3D11Device::CheckFeatureSupport**](https://msdn.microsoft.com/library/windows/desktop/ff476497) with the [**D3D11\_FEATURE\_SHADER\_MIN\_PRECISION\_SUPPORT**](https://msdn.microsoft.com/library/windows/desktop/ff476124#d3d11-feature-shader-min-precision-support) value. For more info, see [HLSL minimum precision support](https://msdn.microsoft.com/library/windows/desktop/hh404562#min-precision).

-   [Declare variables with minimum precision data types](#declare-variables-with-minimum-precision-data-types)
-   [Testing your minimum precision shader code](#testing-your-minimum-precision-shader-code)
-   [Related topics](#related-topics)

## Declare variables with minimum precision data types

To use minimum precision in HLSL shader code, declare individual variables with types like **min16float** (**min16float4** for a vector), **min16int**, **min10float**, and so on. With these variables, your shader code indicates that it doesn’t require more precision than what the variables indicate. But hardware can ignore the minimum precision indicators and run at full 32-bit precision. When your shader code is used on hardware that takes advantage of minimum precision, you use less memory bandwidth and as a result you also use less system power as long as your shader code doesn’t expect more precision than it specified.

You don't need to author multiple shaders that do and don't use minimum precision. Instead, create shaders with minimum precision, and the minimum precision variables behave at full 32-bit precision if the graphics driver reports that it doesn't support any minimum precision. HLSL minimum precision shaders don't work on operating systems earlier than Windows 8 so if you plan to target earlier operating systems, you'll need to author multiple shaders, some that do and others that don't use minimum precision.

> [!Note]  
> Don't make data switches between different precision levels within a shader because these types of conversions are wasteful and reduce performance. The exception is that shader constants are still always 32 bit, but vendors can design graphics hardware that can freely down-convert to whatever lower precision the HLSL instruction reading might use.

 

By using minimum precision, you can control the precision of computations in various parts of your shader code.

The rules for HLSL minimum precision are similar to C/C++, where the types in an expression determine the precision of the operation, not the type being eventually written to.

## Testing your minimum precision shader code

The reference rasterizer ([**D3D\_DRIVER\_TYPE\_REFERENCE**](https://msdn.microsoft.com/library/windows/desktop/ff476328#d3d-driver-type-reference)) gives you a rough idea of how minimum precision in your HLSL shader code behaves by quantizing each HLSL instruction to the specified precision. This helps you discover code that might accidentally rely on more than the minimum precision. The reference rasterizer doesn’t run any faster when your HLSL shader code uses minimum precision, but you can use it to verify the correctness of your code. [WARP](https://msdn.microsoft.com/library/windows/desktop/ff476871) ([**D3D\_DRIVER\_TYPE\_WARP**](https://msdn.microsoft.com/library/windows/desktop/ff476328#d3d-driver-type-warp)) doesn’t support using minimum precision in HLSL shader code; WARP just runs at full 32-bit precision.

## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

 




