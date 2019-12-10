---
Description: This topic describes optimization considerations and strategies with the DirectXMath Library.
ms.assetid: bcbf8ae1-ed49-fdf7-812d-b2089537ab28
title: Code Optimization with the DirectXMath Library
ms.topic: article
ms.date: 05/31/2018
---

# Code Optimization with the DirectXMath Library

This topic describes optimization considerations and strategies with the DirectXMath Library.

-   [Use accessors sparingly](#use-accessors-sparingly)
-   [Use correct compilation settings](#use-correct-compilation-settings)
-   [Use Est functions when appropriate](#use-est-functions-when-appropriate)
-   [Use Aligned Data Types and Operations](#use-aligned-data-types-and-operations)
-   [Properly Align Allocations](#properly-align-allocations)
-   [Avoid Operator Overloads When Possible](#avoid-operator-overloads-when-possible)
-   [Denormals](#denormals)
-   [Take Advantage of the Integer Floating Point Duality](#take-advantage-of-the-integer-floating-point-duality)
-   [Prefer Template Forms](#prefer-template-forms)
-   [Using DirectXMath with Direct3D](#using-directxmath-with-direct3d)
-   [Related topics](#related-topics)

## Use accessors sparingly

Vector-based operations use the SIMD instruction sets and these make use of special registers. Accessing individual components requires moving from the SIMD registers to the scalar ones and back again.

When possible, it is more efficient to initialize all of the components of an [**XMVECTOR**](xmvector-data-type.md) at one time, instead of using a series of individual vector accessors.

## Use correct compilation settings

For Windows x86 targets, enable /arch:SSE2. For all Windows targets, enable /fp:fast.

By default, compilation against the DirectXMath Library for Window x86 targets is done with \_XM\_SSE\_INTRINSICS\_ defined. This means that all DirectXMath functionality will make use of SSE2 instructions. However, the same is not true for other code.

Code outside of DirectXMath is handled using compiler defaults. Without this switch, the generated code may often use the less efficient x87 code.

We highly recommend that you always use the latest available version of the compiler.

## Use Est functions when appropriate

Many functions have an equivalent estimation function ending in Est. These functions trade some accuracy for improved performance. Est functions are appropriate for non-critical calculations where accuracy can be sacrificed for speed. The exact amount of lost accuracy and speed increase are platform dependent.

For example, the [**XMVector3AngleBetweenNormalsEst**](https://msdn.microsoft.com/library/Ee420801(v=VS.85).aspx) function could be used in place of the [**XMVector3AngleBetweenNormals**](https://msdn.microsoft.com/library/Ee420800(v=VS.85).aspx) function.

## Use Aligned Data Types and Operations

The SIMD instruction sets on versions of windows supporting SSE2 typically have aligned and unaligned versions of memory operations. The use of the aligned operations is faster, and should be preferred wherever possible.

The DirectXMath Library provides access aligned and unaligned functionality through variant vector types, structure, and functions. These variants are indicated by an "A" at the end of the name.

For example, there are an unaligned [**XMFLOAT4X4**](https://msdn.microsoft.com/library/Ee419621(v=VS.85).aspx) structure and an aligned [**XMFLOAT4X4A**](https://msdn.microsoft.com/library/Ee419623(v=VS.85).aspx) structure, which are used by the [**XMStoreFloat4**](https://msdn.microsoft.com/library/Ee420343(v=VS.85).aspx) and [**XMStoreFloat4A**](https://msdn.microsoft.com/library/Ee420344(v=VS.85).aspx) functions respectively.

## Properly Align Allocations

The aligned versions of the [SSE](https://docs.microsoft.com/previous-versions/visualstudio/visual-studio-2010/t467de55(v=vs.100)) intrinsics underlying the DirectXMath Library are faster than the unaligned.

For this reason, DirectXMath operations using [**XMVECTOR**](xmvector-data-type.md) and [**XMMATRIX**](https://msdn.microsoft.com/library/Ee419959(v=VS.85).aspx) objects assume those objects are 16-byte aligned. This is automatic for stack based allocations, if code is compiled against the DirectXMath Library using the recommended Windows (see [Use Correct Compilation Settings](#use-correct-compilation-settings)) compiler settings. However, it is important to ensure that heap-allocation containing **XMVECTOR** and **XMMATRIX** objects, or casts to these types, meet these alignment requirements.

While 64-bit Windows memory allocations are 16-byte aligned, by default on 32 bit versions of Windows memory allocated is only 8-byte aligned. For information on controlling memory alignment, see [\_aligned\_malloc](https://msdn.microsoft.com/library/8z34s9c6(VS.80).aspx).

When using aligned DirectXMath types with the Standard Template Library (STL), you will need to provide a custom allocator that ensures the 16-byte alignment. See the Visual C++ Team [blog](https://devblogs.microsoft.com/cppblog/the-mallocator/) for an example of writing a custom allocator (instead of malloc/free you'll want to use \_aligned\_malloc and \_aligned\_free in your implementation).

> [!Note]  
> Some STL templates modify the provided type's alignment. For example, [make\_shared<>](https://docs.microsoft.com/cpp/standard-library/memory-functions?view=vs-2017) adds some internal tracking information which may or may not respect the alignment of the provided user type, resulting in unaligned data members. In this case, you need to use unaligned types instead of aligned types. If you derive from existing classes, including many Windows Runtime objects, you can also modify the alignment of a class or structure.

 

## Avoid Operator Overloads When Possible

As a convenience feature, a number of types such as [**XMVECTOR**](xmvector-data-type.md) and [**XMMATRIX**](https://msdn.microsoft.com/library/Ee419959(v=VS.85).aspx) have operator overloads for common arithmetic operations. Such operator overloads tend to create numerous temporary objects. We recommend that you avoid these operator overloads in performance sensitive code.

## Denormals

To support computations close to 0, the IEEE 754 float-point standard includes support for gradual underflow. Gradual underflow is implemented through the use of denormalized values, and many hardware implementations are slow when handling denormals. An optimization to consider is to disable the handling of denormals for the vector operations used by DirectXMath.

Changing the handling of denormals is done by using the [\_controlfp\_s](https://docs.microsoft.com/cpp/c-runtime-library/reference/controlfp-s) routine on a pre-thread basis, and can result in performance improvements. Use this code to change the handling of denormals:


```
  #include <float.h>;
    unsigned int control_word;
    _controlfp_s( &control_word, _DN_FLUSH, _MCW_DN );
```



> [!Note]  
> On 64-bit versions of Windows, [SSE](https://docs.microsoft.com/previous-versions/visualstudio/visual-studio-2010/t467de55(v=vs.100)) instructions are used for all computations, not just the vector operations. Changing the denormal handling affects all floating-point computations in your program, not just the vector operations used by DirectXMath.

 

## Take Advantage of the Integer Floating Point Duality

DirectXMath supports vectors of 4 single-precision floating-point or four 32-bit (signed or unsigned) values.

Because the instruction sets used to implement the DirectXMath Library have the ability to treat the same data as multiple different types-for example, treat the same vector as floating-point and integer data-certain optimizations can be achieved. You can get these optimizations by using the integer vector initialization routines and bit-wise operators to manipulate floating-point values.

The binary format of single-precision floating-point numbers used by the DirectXMath Library completely conforms to the IEEE 764 standard:

``` syntax
     SIGN    EXPONENT   MANTISSA
     X       XXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXX
     1 bit   8 bits     23 bits
```

When working with the IEEE 764 single precision floating-point number, it is important to keep in mind, that some representations have special meaning (that is, they do not conform to the preceding description). Examples include:

-   Positive zero is 0
-   Negative zero is 0x80000000
-   Q\_NAN is 07FC0000
-   +INF is 0x7F800000
-   -INF is 0xFF800000

## Prefer Template Forms

Template form exists for [**XMVectorSwizzle**](https://msdn.microsoft.com/library/Hh404826(v=VS.85).aspx), [**XMVectorPermute**](https://msdn.microsoft.com/library/Hh855956(v=VS.85).aspx), [**XMVectorInsert**](https://msdn.microsoft.com/library/Hh404801(v=VS.85).aspx), [**XMVectorShiftLeft**](https://msdn.microsoft.com/library/Hh404823(v=VS.85).aspx), [**XMVectorRotateLeft**](https://msdn.microsoft.com/library/Hh404806(v=VS.85).aspx), and [**XMVectorRotateRight**](https://msdn.microsoft.com/library/Hh404807(v=VS.85).aspx). Using these instead of the general function form allows the compiler to create much more efficent implementations. For [SSE](https://docs.microsoft.com/previous-versions/visualstudio/visual-studio-2010/t467de55(v=vs.100)), this often collapses down to one or two \_mm\_shuffle\_ps values. For ARM-NEON, the **XMVectorSwizzle** template can utilize a number of special cases rather than the more general VTBL swizzle/permute.

## Using DirectXMath with Direct3D

A common use for DirectXMath is to perform graphics computations for use with Direct3D. With Direct3D 10.x and Direct3D 11.x, you can use the DirectXMath library in these direct ways:

-   Use the Colors namespace [constants](ovw-xnamath-reference-constants.md) directly in the *ColorRGBA* parameter in a call to the [**ID3D11DeviceContext::ClearRenderTargetView**](https://msdn.microsoft.com/library/Ff476388(v=VS.85).aspx) or [**ID3D10Device::ClearRenderTargetView**](https://msdn.microsoft.com/library/Bb173539(v=VS.85).aspx) method. For Direct3D 9, you must convert to the [**XMCOLOR**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmcolor) type to use it as the *Color* parameter in a call to the [**IDirect3DDevice9::Clear**](https://msdn.microsoft.com/library/Bb174352(v=VS.85).aspx) method.
-   Use the [**XMFLOAT4**](https://msdn.microsoft.com/library/Ee419608(v=VS.85).aspx)/[**XMVECTOR**](xmvector-data-type.md) and [**XMFLOAT4X4**](https://msdn.microsoft.com/library/Ee419621(v=VS.85).aspx)/[**XMMATRIX**](https://msdn.microsoft.com/library/Ee419959(v=VS.85).aspx) types to setup constant buffer structures for reference by HLSL [**float4**](https://msdn.microsoft.com/library/Bb509646(v=VS.85).aspx) or [**matrix**](https://msdn.microsoft.com/library/Bb509623(v=VS.85).aspx)/float4x4 types.
    > [!Note]  
    > [**XMFLOAT4X4**](https://msdn.microsoft.com/library/Ee419621(v=VS.85).aspx)/[**XMMATRIX**](https://msdn.microsoft.com/library/Ee419959(v=VS.85).aspx) types are in row-major format. Therefore, if you use the /Zpr compiler switch (the [**D3DCOMPILE\_PACK\_MATRIX\_COLUMN\_MAJOR**](https://msdn.microsoft.com/library/Gg615083(v=VS.85).aspx) compile flag) or omit the row\_major [keyword](https://msdn.microsoft.com/library/Bb509568(v=VS.85).aspx) when you declare the matrix type in HLSL, you must transpose the matrix when you set it into the constant buffer.

     

-   With Direct3D 10.x and Direct3D 11.x, you can assume that the pointer returned by the Map method (for example, [**ID3D11DeviceContext::Map**](https://msdn.microsoft.com/library/Ff476457(v=VS.85).aspx)) in the **pData** member ([**D3D10\_MAPPED\_TEXTURE2D**](https://msdn.microsoft.com/library/Bb205319(v=VS.85).aspx).**pData**, [**D3D10\_MAPPED\_TEXTURE3D**](https://msdn.microsoft.com/library/Bb205320(v=VS.85).aspx).**pData**, or [**D3D11\_MAPPED\_SUBRESOURCE**](https://msdn.microsoft.com/library/Ff476182(v=VS.85).aspx).**pData**) is 16-byte aligned if you use [feature level](https://msdn.microsoft.com/library/Ff476876(v=VS.85).aspx) 10\_0 or higher or whenever you use [**D3D11\_USAGE\_STAGING**](https://msdn.microsoft.com/library/Ff476259(v=VS.85).aspx) resources.

## Related topics

<dl> <dt>

[DirectXMath Programming Guide](ovw-xnamath-progguide.md)
</dt> </dl>

 

 



