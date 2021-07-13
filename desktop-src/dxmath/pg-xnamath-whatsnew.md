---
description: The DirectXMath library is based on the XNA Math C++ SIMD library version 2.x. Here we describe how DirectXMath differs from XNA Math and how DirectXMath versions differ.
ms.assetid: 105800d3-a191-c78f-316a-bf2daf7b27a6
title: What's New (DirectXMath)
ms.topic: article
ms.date: 05/31/2018
---

# What's New (DirectXMath)

The DirectXMath library is based on the [XNA Math C++ SIMD library version 2.04](https://walbourn.github.io/xna-math-version-2-04/). Here we describe how DirectXMath differs from XNA Math and how DirectXMath versions differ.

-   [Rlease history](#release-history)
-   [DirectXMath differences from XNA Math](#directxmath-differences-from-xna-math)
-   [Related topics](#related-topics)

## Release history

<table>
 <tr>
  <td>Windows 10 SDK (20348), version 2104</td><td>DirectXMath 3.16</td>
 </td>
 <tr>
  <td>Windows 10 May 2020 Update SDK</td><td>DirectXMath 3.14</td>
 </tr>
 <tr>
  <td>Windows 10 October 2018 Update SDK</td><td>DirectXMath 3.13</td>
 </tr>
 <tr>
  <td>Windows 10 April 2018 Update SDK<br />Windows 10 Fall Creators Update SDK</td><td>DirectXMath 3.11</td>
 </tr>
 <tr>
  <td>Windows 10 Creators Update SDK</td><td>DirectXMath 3.10</td>
 </tr>
 <tr>
  <td>Windows 10 Anniversary SDK</td><td>DirectXMath 3.09</td>
 </tr>
 <tr>
  <td>Windows 10 SDK (November 2015)</td><td>DirectXMath 3.08</td>
 </tr>
 <tr>
  <td>Windows SDK for Windows 8.1 (Spring 2015)</td><td>DirectXMath 3.07</td>
 </tr>
 <tr>
  <td>Windows SDK for Windows 8.1</td><td>DirectXMath 3.06</td>
 </tr>
 <tr>
  <td>Windows SDK for Windows 8</td><td>DirectXMath 3.03</td>
 </tr>
</table>

See [DirectXMath releases](https://github.com/Microsoft/DirectXMath/releases) for more information.

## DirectXMath differences from XNA Math

Here is how the DirectXMath library primarily differs from the XNA Math library:

-   DirectXMath is C++ only (namespaces, overloads, new templates, and so on).
-   Requires C++11 standard library support (that is, stdint.h, and so on).
-   ARM-NEON intrinsics support for the Windows RT platform.
-   New color functionality (color space conversions, .NET color constants).
-   Bounding volume types (a version of which was previously in the XNACollision header in the DirectX SDK Collision sample).
-   No Xbox 360 version is available. The Xbox 360 XDK continues to ship XNAMath v2.x; removal of Xbox 360 specific data types and function variants.
-   Reworked [**XMVectorPermute**](/windows/win32/api/directxmath/nf-directxmath-xmvectorpermute) for improved optimization for SSE and ARM-NEON intrinsics.
-   The [**XMMATRIX**](/windows/win32/api/directxmath/ns-directxmath-xmmatrix) type is fully opaque. To access individual elements of **XMMATRIX**, use other types such as [**XMFLOAT4X4**](/windows/win32/api/directxmath/ns-directxmath-xmfloat4x4).

## Related topics

<dl> <dt>

[DirectXMath Programming Guide](ovw-xnamath-progguide.md)
</dt> <dt>

[DirectXMath releases](https://github.com/Microsoft/DirectXMath/releases)
</dt> </dl>

 

 
