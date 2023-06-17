---
title: Getting started (DirectXMath)
description: The DirectXMath Library implements an optimal and portable interface for arithmetic and linear algebra operations on single-precision floating-point vectors (2D, 3D, and 4D) or matrices (3×3 and 4×4).
ms.assetid: 9972e382-7a0f-88a7-ad44-18521af3520d
ms.topic: article
ms.date: 05/31/2018
---

# Getting started (DirectXMath)

The DirectXMath Library implements an optimal and portable interface for arithmetic and linear algebra operations on single-precision floating-point vectors (2D, 3D, and 4D) or matrices (3×3 and 4×4). The library has some limited support for integer vector operations. These operations are used extensively in rendering and animation by graphics programs. There is no support for double-precision vectors (including longs, shorts, or bytes), and only limited integer vector operations.

The library is available on a variety of Windows platforms. Because the library provides functionality not available previously, this version supersedes the following libraries:

-   Xbox Math library provided by the Xboxmath.h header
-   D3DX 9 library provided by the D3DX 9 DLLs
-   D3DX 10 math library provided through the D3DX 10 DLLs
-   XNA Math library provided by the xnamath.h header in the DirectX SDK and Xbox 360 XDK

These sections outline the basics of getting started.

-   [Download](#download)
-   [Run-Time System Requirements](#run-time-system-requirements)
-   [Design Overview](#design-overview)
-   [Matrix convention](#matrix-convention)
-   [Basic Usage](#basic-usage)
-   [Type Usage Guidelines](#type-usage-guidelines)
-   [Creating Vectors](#creating-vectors)
    -   [CONSTANT VECTORS](#constant-vectors)
    -   [VECTORS FROM VARIABLES](#vectors-from-variables)
    -   [VECTORS FROM VECTORS](#vectors-from-vectors)
    -   [VECTORS FROM MEMORY](#vectors-from-memory)
-   [Extracting Components from Vectors](#extracting-components-from-vectors)
-   [Related topics](#related-topics)

## Download

The DirectXMath library is included in the Windows SDK. Alternatively you can download it from [GitHub/Microsoft/DirectXMath](https://github.com/Microsoft/DirectXMath). This site also contains related sample projects.

## Run-Time System Requirements

The DirectXMath Library uses specialized processor instructions for vector operations when they are available. To avoid having a program generate "unknown instruction exception" faults, check for processor support by calling [**XMVerifyCPUSupport**](/windows/win32/api/directxmath/nf-directxmath-xmverifycpusupport) before using the DirectXMath Library.

These are the basic DirectXMath Library run-time support requirements:

-   Default compilation on a Windows (x86/x64) platform requires SSE/SSE2 instruction support.
-   Default compliation on a Windows RT platform requires ARM-NEON instruction support.
-   Compilation with [**\_XM\_NO\_INTRINSICS\_**](ovw-xnamath-reference-directives.md) defined requires only standard floating-point operation support.

> [!Note]  
> When you call [**XMVerifyCPUSupport**](/windows/win32/api/directxmath/nf-directxmath-xmverifycpusupport), include <windows.h> before you include <DirectXMath.h>. This is the only function in the library that requires any content from <windows.h> so you aren't required to include <windows.h> in every module that uses <DirectXMath.h>.

 

## Design Overview

The DirectXMath Library primarily supports the C++ programming language. The library is implemented using inline routines in the header files, DirectXMath\*.inl, DirectXPackedVector.inl and DirectXCollision.inl. This implementation makes use of high-performance compiler intrinsics.

The DirectXMath Library provides:

-   An implementation using SSE/SSE2 intrinsics.
-   An implementation without intrinsics.
-   An implementation using ARM-NEON intrinsics.

Because the library is delivered using header files, use the source code to customize and optimize for your own app.

## Matrix convention

DirectXMath uses row-major matrices, row vectors, and pre-multiplication. Handedness is determined by which function version is used (RH vs. LH), otherwise the function works with either left-handed or right-handed view coordinates.

For reference, Direct3D has historically used left-handed coordinate system, row-major matrices, row vectors, and pre-multiplication. Modern Direct3D does not have a strong requirement for left vs. right-handed coordinates, and typically HLSL shaders default to consuming column-major matrices. See [HLSL Matrix Ordering](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-per-component-math) for details.

## Basic Usage

To use DirectXMath Library functions, include the DirectXMath.h, DirectXPackedVector.h, DirectXColors.h, and/or DirectXCollision.h headers. The headers are found in the Windows Software Development Kit for Windows Store apps.

## Type Usage Guidelines

The [**XMVECTOR**](xmvector-data-type.md) and [**XMMATRIX**](/windows/win32/api/directxmath/ns-directxmath-xmmatrix) types are the work horses for the DirectXMath Library. Every operation consumes or produces data of these types. Working with them is key to using the library. However, since DirectXMath makes use of the SIMD instruction sets, these data types are subject to a number of restrictions. It is critical that you understand these restrictions if you want to make good use of the DirectXMath functions.

You should think of [**XMVECTOR**](xmvector-data-type.md) as a proxy for a SIMD hardware register, and [**XMMATRIX**](/windows/win32/api/directxmath/ns-directxmath-xmmatrix) as a proxy for a logical grouping of four SIMD hardware registers. These types are annotated to indicate they require 16-byte alignment to work correctly. The compiler will automatically place them correctly on the stack when they are used as a local variable, or place them in the data segment when they are used as a global variable. With proper conventions, they can also be passed safely as parameters to a function (see [Calling Conventions](pg-xnamath-internals.md) for details).

Allocations from the heap, however, are more complicated. As such, you need to be careful whenever you use either [**XMVECTOR**](xmvector-data-type.md) or [**XMMATRIX**](/windows/win32/api/directxmath/ns-directxmath-xmmatrix) as a member of a class or structure to be allocated from the heap. On Windows x64, all heap allocations are 16-byte aligned, but for Windows x86, they are only 8-byte aligned. There are options for allocating structures from the heap with 16-byte alignment (see [Properly Align Allocations](pg-xnamath-optimizing.md)). For C++ programs, you can use operator new/delete/new\[\]/delete\[\] overloads (either globally or class-specific) to enforce optimal alignment if desired.

> [!Note]  
> As an alternative to enforcing alignment in your C++ class directly by overloading new/delete, you can use the [pImpl idiom](https://en.wikipedia.org/wiki/Opaque_pointer). If you ensure your **Impl** class is aligned via [**\_aligned\_malloc**](/cpp/c-runtime-library/reference/aligned-malloc) internally, you can then freely use aligned types within the internal implementation. This is a good option when the 'public' class is a Windows Runtime ref class or intended for use with [**std::shared\_ptr<>**](/cpp/standard-library/shared-ptr-class), which can otherwise disrupt careful alignment.

 

However, often it is easier and more compact to avoid using [**XMVECTOR**](xmvector-data-type.md) or [**XMMATRIX**](/windows/win32/api/directxmath/ns-directxmath-xmmatrix) directly in a class or structure. Instead, make use of the [**XMFLOAT3**](/windows/win32/api/directxmath/ns-directxmath-xmfloat3), [**XMFLOAT4**](/windows/win32/api/directxmath/ns-directxmath-xmfloat4), [**XMFLOAT4X3**](/windows/win32/api/directxmath/ns-directxmath-xmfloat4x3), [**XMFLOAT4X4**](/windows/win32/api/directxmath/ns-directxmath-xmfloat4x4), and so on, as members of your structure. Further, you can use the [Vector Loading](ovw-xnamath-reference-functions-load.md) and [Vector Storage](ovw-xnamath-reference-functions-storage.md) functions to move the data efficiently into **XMVECTOR** or **XMMATRIX** local variables, perform computations, and store the results. There are also streaming functions ([**XMVector3TransformStream**](/windows/win32/api/directxmath/nf-directxmath-xmvector3transformstream), [**XMVector4TransformStream**](/windows/win32/api/directxmath/nf-directxmath-xmvector4transformstream), and so on) that efficiently operate directly on arrays of these data types.

## Creating Vectors

### CONSTANT VECTORS

Many operations require the use of constants in vector computations, and there are a number of ways to load an [**XMVECTOR**](xmvector-data-type.md) with the desired values.

-   If loading a scalar constant into all elements of an [**XMVECTOR**](xmvector-data-type.md), use [**XMVectorReplicate**](/windows/win32/api/directxmath/nf-directxmath-xmvectorreplicate) or [**XMVectorReplicateInt**](/windows/win32/api/directxmath/nf-directxmath-xmvectorreplicateint).
    ```
    XMVECTOR vFive = XMVectorReplicate( 5.f );
    ```

    

-   If using a vector constant with different fixed values as an [**XMVECTOR**](xmvector-data-type.md), use the [**XMVECTORF32**](xmvectorf32-data-type.md), [**XMVECTORU32**](xmvectoru32-data-type.md), **XMVECTORI32**, or [**XMVECTORU8**](xmvectoru8-data-type.md) structures. These can be then referenced directly anywhere you would pass an **XMVECTOR** value.
    ```
    static const XMVECTORF32 vFactors = { 1.0f, 2.0f, 3.0f, 4.0f };
    ```

    

    > [!Note]  
    > Do not use initializer lists directly with [**XMVECTOR**](xmvector-data-type.md) (that is, XMVECTOR v = { 1.0f, 2.0f, 3.0f, 4.0f }). Such code is inefficient and is not portable across all platforms that are supported by DirectXMath.

     

-   DirectXMath includes a number of pre-defined global constants you can make use of in your code (g\_XMOne, g\_XMOne3, g\_XMTwo, g\_XMOneHalf, g\_XMHalfPi, g\_XMPi, and so on). Search the DirectXMath.h header for the **XMGLOBALCONST** values.
-   There are a set of vector constants for common RGB colors (Red, Green, Blue, Yellow, and so on). For more info about these vector constants, see DirectXColors.h and the DirectX::Colors namespace.

### VECTORS FROM VARIABLES

-   If creating a vector from a single scalar variable, see [**XMVectorReplicate**](/windows/win32/api/directxmath/nf-directxmath-xmvectorreplicate) and [**XMVectorReplicateInt**](/windows/win32/api/directxmath/nf-directxmath-xmvectorreplicateint).
    ```
    XMVECTOR v = XMVectorReplicate( f  );
    ```

    

-   If creating a vector from four scalar variables, see [**XMVectorSet**](/windows/win32/api/directxmath/nf-directxmath-xmvectorset) and [**XMVectorSetInt**](/windows/win32/api/directxmath/nf-directxmath-xmvectorsetint).
    ```
    XMVECTOR v = XMVectorSet( fx, fy, fz, fw );
    ```

    

### VECTORS FROM VECTORS

-   If creating a vector from another vector with a specific component set to a variable, you can consider using [Vector Accessor Functions](ovw-xnamath-reference-functions-accessors.md).
    ```
    XMVECTOR v2 = XMVectorSetW( v1, fw );
    ```

    

-   If creating a vector from another vector with a single component replicated, use [**XMVectorSplatX**](/windows/win32/api/directxmath/nf-directxmath-xmvectorsplatx), [**XMVectorSplatY**](/windows/win32/api/directxmath/nf-directxmath-xmvectorsplaty), [**XMVectorSplatZ**](/windows/win32/api/directxmath/nf-directxmath-xmvectorsplatz), and [**XMVectorSplatW**](/windows/win32/api/directxmath/nf-directxmath-xmvectorsplatw).
    ```
    XMVECTOR vz = XMVectorSplatZ( v );
    ```

    

-   If creating a vector from another vector or pair of vectors with reordered components, see [**XMVectorSwizzle**](/windows/win32/api/directxmath/nf-directxmath-xmvectorswizzle) and [**XMVectorPermute**](/windows/win32/api/directxmath/nf-directxmath-xmvectorpermute).
    ```
    XMVECTOR v2 = XMVectorSwizzle<XM_SWIZZLE_Z, XM_SWIZZLE_Y, XM_SWIZZLE_W, XM_SWIZZLE_X>( v1 );

    XMVECTOR v3 = XMVectorPermute<XM_PERMUTE_0W, XM_PERMUTE_1X, XM_PERMUTE_0X, XM_PERMUTE_1Z>( v1, v2 );
    ```

    

### VECTORS FROM MEMORY

-   For loading a single float value from memory, see [**XMVectorReplicatePtr**](/windows/win32/api/directxmath/nf-directxmath-xmvectorreplicateptr), [**XMVectorReplicateIntPtr**](/windows/win32/api/directxmath/nf-directxmath-xmvectorreplicateintptr), [**XMLoadFloat**](/windows/win32/api/directxmath/nf-directxmath-xmloadfloat), and [**XMLoadInt**](/windows/win32/api/directxmath/nf-directxmath-xmloadint).
-   Common ways to load float arrays are: [**XMLoadFloat2**](/windows/win32/api/directxmath/nf-directxmath-xmloadfloat2), [**XMLoadFloat3**](/windows/win32/api/directxmath/nf-directxmath-xmloadfloat3), [**XMLoadFloat4**](/windows/win32/api/directxmath/nf-directxmath-xmloadfloat4), [**XMLoadFloat3x3**](/windows/win32/api/directxmath/nf-directxmath-xmloadfloat3x3), [**XMLoadFloat4x3**](/windows/win32/api/directxmath/nf-directxmath-xmloadfloat4x3), and [**XMLoadFloat4x4**](/windows/win32/api/directxmath/nf-directxmath-xmloadfloat4x4).
-   DirectXMath includes a rich set of types and related loads and stores for handling various data-structures and common GPU formats. See [Vector Load](ovw-xnamath-reference-functions-load.md) and [Vector Store](ovw-xnamath-reference-functions-storage.md).

## Extracting Components from Vectors

SIMD processing is most efficient when data is loaded into the SIMD registers and fully processed before extracting the results. Conversion between scalar and vector forms is inefficient, so we recommend that you do it only when required. For this reason, functions in the DirectXMath library that produce a scalar value are returned in a vector form where the scalar result is replicated across the resulting vector (that is, [**XMVector2Dot**](/windows/win32/api/directxmath/nf-directxmath-xmvector2dot), [**XMVector3Length**](/windows/win32/api/directxmath/nf-directxmath-xmvector3length), and so on). However, when you need scalar values, here are a few choices on how to go about it:

-   If a single scalar answer is computed, use of the [Vector Accessor Functions](ovw-xnamath-reference-functions-accessors.md) is appropriate:
    ```
    float f = XMVectorGetX( v );
    ```

    

-   If multiple components of the vector are required to be extracted, consider storing the vector in a memory structure and reading it back. For example:
    ```
    XMFLOAT4A t;
    XMStoreFloat4A( &t, v );
    // t.x, t.y, t.z, and t.w can be individually accessed now
    ```

    

-   The most efficient form of vector processing is to use memory-to-memory streaming where the input data is loaded from memory (using [Vector Load Functions](ovw-xnamath-reference-functions-load.md)), processed fully in SIMD form, and then written to memory (using [Vector Store Functions](ovw-xnamath-reference-functions-storage.md)).

## Related topics

<dl> <dt>

[DirectXMath Programming Guide](ovw-xnamath-progguide.md)
</dt> </dl>

 

 
