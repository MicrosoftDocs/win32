---
description: .
ms.assetid: 719954bf-0d7d-f647-2d3f-a77d87df204e
title: DirectXMath
ms.topic: article
ms.date: 05/31/2018
---

# DirectXMath

## Purpose

The DirectXMath API provides SIMD-friendly C++ types and functions for common linear algebra and graphics math operations common to DirectX applications. The library provides optimized versions for Windows 32-bit (x86), Windows 64-bit (x64), and Windows on ARM/ARM64 through SSE, AVX, and ARM-NEON intrinsics support in the Visual C++ compiler.

For developers new to DirectXMath, you may want to consider using the SimpleMath wrapper in the *DirectX Tool Kit* for [DirectX 11](https://go.microsoft.com/fwlink/?LinkId=248929) / [DirectX12](https://go.microsoft.com/fwlink/?LinkID=615561) as a starting point.

## In this section



| Topic                                                                     | Description                                                                      |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [DirectXMath Programming Guide](ovw-xnamath-progguide.md)<br/>     | DirectXMath provides a math solution optimized for Windows.<br/>           |
| [DirectXMath Programming Reference](ovw-xnamath-reference.md)<br/> | This section contains reference material for the DirectXMath Library.<br/> |



 

## Developer audience

The DirectXMath library is designed for C++ developers working on games and DirectX graphics in Windows Store apps, Xbox games, and traditional desktop apps for Windows.

## Obtaining DirectXMath
 
The DirectXMath headers ship in the Windows SDK that comes with Visual Studio 2012 or later, and as an all inline header there is no DLL or static library to link against. It is also available as a package on [NuGet](https://www.nuget.org/packages/directxmath/).

DirectXMath is open source under the [MIT license](https://opensource.org/licenses/MIT) hosted on [GitHub](https://github.com/Microsoft/DirectXMath).




