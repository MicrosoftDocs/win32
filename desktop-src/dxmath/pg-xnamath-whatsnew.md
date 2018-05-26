---
Description: The DirectXMath library is based on the XNA Math C++ SIMD library version 2.04. Here we describe how DirectXMath differs from XNA Math and how DirectXMath versions differ.
ms.assetid: 105800d3-a191-c78f-316a-bf2daf7b27a6
title: Whats New
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
-   Reworked [**XMVectorPermute**](xmvectorpermute.md) for improved optimization for SSE and ARM-NEON intrinsics.
-   The [**XMMATRIX**](/windows/win32/DirectXMath/?branch=master) type is fully opaque. To access individual elements of **XMMATRIX**, use other types such as [**XMFLOAT4X4**](/windows/win32/DirectXMath/?branch=master).

## DirectXMath 3.06 differences from DirectXMath 3.03

The Windows SDK for Windows 8 shipped with DirectXMath version 3.03.

The Windows SDK for Windows 8.1 ships with DirectXMath version 3.06.

Here is how DirectXMath version 3.06 differs from DirectXMath version 3.03:

-   3.06 fixes load/store of [**XMFLOAT3SE**](/windows/win32/DirectXPackedVector/ns-directxpackedvector-xmfloat3se?branch=master) to properly match the DXGI\_FORMAT\_R9G9B9E5\_SHAREDEXP definition.
-   3.06 adds [**XMLoadUDecN4\_XR**](/windows/win32/directxpackedvector.inl/nf-directxpackedvector-xmloadudecn4_xr?branch=master) and [**XMStoreUDecN4\_XR**](/windows/win32/directxpackedvector.inl/nf-directxpackedvector-xmstoreudecn4_xr?branch=master) to match the DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM definition.
-   3.06 adds [**XMColorRGBToSRGB**](/windows/win32/DirectXMath/?branch=master) and [**XMColorSRGBToRGB**](/windows/win32/DirectXMath/?branch=master) to convert between linear RGB and sRGB.
-   3.06 adds [**XMVectorExp2**](/windows/win32/directxmathvector.inl/?branch=master), [**XMVectorLog2**](/windows/win32/directxmathvector.inl/?branch=master), [**XMVectorExpE**](/windows/win32/directxmathvector.inl/?branch=master), and [**XMVectorLogE**](/windows/win32/directxmathvector.inl/?branch=master) functions to provide base-e support in addition to the existing base-2 support.
    -   [**XMVectorExp**](xmvectorexp.md) and [**XMVectorLog**](xmvectorlog.md) are now aliases for [**XMVectorExp2**](/windows/win32/directxmathvector.inl/?branch=master) and [**XMVectorLog2**](/windows/win32/directxmathvector.inl/?branch=master) respectively.
-   3.06 uses the x86/x64 \_\_vectorcall calling-convention when available. 3.05 introduces XM\_CALLCONV, HXMVECTOR, and FXMMATRIX.
-   3.06 updates the matrix version of the **Transform** method for [**BoundingOrientedBox**](/windows/win32/DirectXCollision/ns-directxcollision-boundingorientedbox?branch=master) and [**BoundingFrustum**](/windows/win32/DirectXCollision/ns-directxcollision-boundingfrustum?branch=master) to handle scaling.
-   3.06 provides additional optimizations for **Stream** functions.
-   3.06 improves the [**XMVectorRound**](xmvectorround.md) algorithm.
-   The 3.06 implementations of the [**XMConvertHalfToFloat**](xmconverthalftofloat.md) and [**XMConvertFloatToHalf**](xmconvertfloattohalf.md) functions now use IEEE 754 standard float16 behavior for INF/QNAN.
-   3.06 fixes an issue with the [**XMVectorFloor**](xmvectorfloor.md) and [**XMVectorCeiling**](xmvectorceiling.md) functions when they are given whole odd numbers (for example, 105.0).
-   3.06 fixes potential warning C4723 when using operator/ or operator/=.
-   The 3.06 implementation of the [**XMVector3Cross**](xmvector3cross.md) function now ensures that the w component is zero on the Windows RT platform.
-   With 3.06, ARM-NEON code paths use multiply-by-scalar intrinsics when ARM-NEON intrinsics are supported.

## Related topics

<dl> <dt>

[DirectXMath Programming Guide](ovw-xnamath-progguide.md)
</dt> <dt>

[DirectXMath releases](https://github.com/Microsoft/DirectXMath/releases)
</dt> </dl>

 

 



