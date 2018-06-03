---
Description: The DirectXMath library is based on the XNA Math C++ SIMD library version 2.04. Here we describe how DirectXMath differs from XNA Math and how DirectXMath versions differ.
ms.assetid: 105800d3-a191-c78f-316a-bf2daf7b27a6
title: What's New
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New

The DirectXMath library is based on the [XNA Math C++ SIMD library version 2.04](http://blogs.msdn.com/b/chuckw/archive/2011/02/23/xna-math-version-2-04.aspx). Here we describe how DirectXMath differs from XNA Math and how DirectXMath versions differ.

-   [New releases](#new-releases)
-   [DirectXMath differences from XNA Math](#directxmath-differences-from-xna-math)
-   [DirectXMath 3.06 differences from DirectXMath 3.03](#directxmath-306-differences-from-directxmath-303)
-   [Related topics](#related-topics)

## New releases

-   The Windows 10 Fall Creators Update SDK shipped with DirectXMath 3.11.
-   The Windows 10 Creators Update SDK shipped with DirectXMath 3.10.
-   The Windows 10 Anniversary SDK shipped with DirectXMath 3.09.
-   The Windows 10 SDK (November 2015) shipped with DirectXMath 3.08.
-   The Windows SDK for Windows 8.1 (Spring 2015) shipped with DirectXMath 3.07.

See [DirectXMath releases](https://github.com/Microsoft/DirectXMath/releases) for more information.

## DirectXMath differences from XNA Math

Here is how the DirectXMath library primarily differs from the XNA Math library:

-   DirectXMath is C++ only (namespaces, overloads, new templates, and so on).
-   Requires C++11 standard library support (that is, stdint.h, and so on).
-   ARM-NEON intrinsics support for the Windows RT platform.
-   New color functionality (color space conversions, .NET color constants).
-   Bounding volume types (a version of which was previously in the XNACollision header in the DirectX SDK Collision sample).
-   No Xbox 360 version is available. The Xbox 360 XDK continues to ship XNAMath v2.x; removal of Xbox 360 specific data types and function variants.
-   Reworked [**XMVectorPermute**](https://www.bing.com/search?q=**XMVectorPermute**) for improved optimization for SSE and ARM-NEON intrinsics.
-   The [**XMMATRIX**](/windows/desktop/api/DirectXMath/) type is fully opaque. To access individual elements of **XMMATRIX**, use other types such as [**XMFLOAT4X4**](/windows/desktop/api/DirectXMath/).

## DirectXMath 3.06 differences from DirectXMath 3.03

The Windows SDK for Windows 8 shipped with DirectXMath version 3.03.

The Windows SDK for Windows 8.1 ships with DirectXMath version 3.06.

Here is how DirectXMath version 3.06 differs from DirectXMath version 3.03:

-   3.06 fixes load/store of [**XMFLOAT3SE**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmfloat3se) to properly match the DXGI\_FORMAT\_R9G9B9E5\_SHAREDEXP definition.
-   3.06 adds [**XMLoadUDecN4\_XR**](/windows/desktop/api/directxpackedvector.inl/nf-directxpackedvector-xmloadudecn4_xr) and [**XMStoreUDecN4\_XR**](/windows/desktop/api/directxpackedvector.inl/nf-directxpackedvector-xmstoreudecn4_xr) to match the DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM definition.
-   3.06 adds [**XMColorRGBToSRGB**](/windows/desktop/api/DirectXMath/) and [**XMColorSRGBToRGB**](/windows/desktop/api/DirectXMath/) to convert between linear RGB and sRGB.
-   3.06 adds [**XMVectorExp2**](/windows/desktop/api/directxmathvector.inl/), [**XMVectorLog2**](/windows/desktop/api/directxmathvector.inl/), [**XMVectorExpE**](/windows/desktop/api/directxmathvector.inl/), and [**XMVectorLogE**](/windows/desktop/api/directxmathvector.inl/) functions to provide base-e support in addition to the existing base-2 support.
    -   [**XMVectorExp**](https://www.bing.com/search?q=**XMVectorExp**) and [**XMVectorLog**](https://www.bing.com/search?q=**XMVectorLog**) are now aliases for [**XMVectorExp2**](/windows/desktop/api/directxmathvector.inl/) and [**XMVectorLog2**](/windows/desktop/api/directxmathvector.inl/) respectively.
-   3.06 uses the x86/x64 \_\_vectorcall calling-convention when available. 3.05 introduces XM\_CALLCONV, HXMVECTOR, and FXMMATRIX.
-   3.06 updates the matrix version of the **Transform** method for [**BoundingOrientedBox**](/windows/desktop/api/DirectXCollision/ns-directxcollision-boundingorientedbox) and [**BoundingFrustum**](/windows/desktop/api/DirectXCollision/ns-directxcollision-boundingfrustum) to handle scaling.
-   3.06 provides additional optimizations for **Stream** functions.
-   3.06 improves the [**XMVectorRound**](https://www.bing.com/search?q=**XMVectorRound**) algorithm.
-   The 3.06 implementations of the [**XMConvertHalfToFloat**](https://www.bing.com/search?q=**XMConvertHalfToFloat**) and [**XMConvertFloatToHalf**](https://www.bing.com/search?q=**XMConvertFloatToHalf**) functions now use IEEE 754 standard float16 behavior for INF/QNAN.
-   3.06 fixes an issue with the [**XMVectorFloor**](https://www.bing.com/search?q=**XMVectorFloor**) and [**XMVectorCeiling**](https://www.bing.com/search?q=**XMVectorCeiling**) functions when they are given whole odd numbers (for example, 105.0).
-   3.06 fixes potential warning C4723 when using operator/ or operator/=.
-   The 3.06 implementation of the [**XMVector3Cross**](https://www.bing.com/search?q=**XMVector3Cross**) function now ensures that the w component is zero on the Windows RT platform.
-   With 3.06, ARM-NEON code paths use multiply-by-scalar intrinsics when ARM-NEON intrinsics are supported.

## Related topics

<dl> <dt>

[DirectXMath Programming Guide](ovw-xnamath-progguide.md)
</dt> <dt>

[DirectXMath releases](https://github.com/Microsoft/DirectXMath/releases)
</dt> </dl>

 

 



