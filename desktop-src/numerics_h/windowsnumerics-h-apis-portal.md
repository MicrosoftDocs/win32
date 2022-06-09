---
title: windowsnumerics.h APIs
description: The windowsnumerics.h header file defines C++ vector and matrix types in the Windows.Foundation.Numerics namespace. It extends the structs from Windows.Foundation.Numerics with a range of mathematical operators and functions.
ms.assetid: 7aa15f80-c440-4dcb-a9a6-f1000a3a95da
ms.topic: article
ms.date: 05/31/2018
---

# windowsnumerics.h APIs

The windowsnumerics.h header file defines C++ vector and matrix types in the [**Windows.Foundation.Numerics**](/uwp/api/Windows.Foundation.Numerics) namespace. It extends the structs from **Windows.Foundation.Numerics** with a range of mathematical operators and functions.

This namespace is available only in C++. Its .NET equivalent is [System.Numerics](/dotnet/api/system.numerics).

## In this section

| Topic | Description |
|-|-|
| [**float2 structure**](float2-structure.md) | A vector with two components. |
| [**float3 structure**](float3-structure.md) | A vector with three components. |
| [**float3x2 structure**](float3x2-structure.md) | A 3x2 matrix, used for 2D transforms. |
| [**float4 structure**](float4-structure.md) | A vector with four components. |
| [**float4x4 structure**](float4x4-structure.md) | A 4x4 matrix, used for 3D transforms. |
| [**plane structure**](plane-structure.md) | This structure represents a plane using a 3D vector normal and a distance value. |
| [**quaternion structure**](quaternion-structure.md) | A four dimensional vector, used to represent a rotation. |
| [**Windows numerics and DirectXMath interop APIs**](windows-numerics-and-directxmath-interop-apis.md) | These functions convert [**Windows.Foundation.Numerics**](/uwp/api/Windows.Foundation.Numerics) types to and from the DirectXMath SIMD types [XMVECTOR](../dxmath/xmvector-data-type.md) and [XMMATRIX](/windows/win32/api/directxmath/ns-directxmath-xmmatrix). |