---
description: Learn about math function support in D3DX. D3DX is a utility library that provides helper services. It is a layer above the Direct3D component.
ms.assetid: a44d25de-f79d-4132-a75a-0c22ccd84341
title: Math Function Support in D3DX (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Math Function Support in D3DX (Direct3D 9)

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

D3DX is a utility library that provides helper services. It is a layer above the Direct3D component.

## Math

Math support, contained in a set of functions, is provided for:

-   Color calculations
-   Planes
-   Matrix manipulation
-   Quaternions
-   2D vectors
-   3D vectors
-   4D vectors

Please note that when coupled with the C++ overloads, the support for basic 3D math types is extensive.

For more information about these functions, see [D3DX Functions](dx9-graphics-reference-d3dx-functions.md). To help find the function you need, they are broken up in several folders.

## FLOAT16

When using the FLOAT16 data type, be sure to limit values to a maximum of D3DX\_16F\_MAX. Any FLOAT16 value that exceeds this will result in undefined behavior in the pipeline. See [Other D3DX Constants](other-d3dx-constants.md).

## Related topics

<dl> <dt>

[D3DX](d3dx.md)
</dt> </dl>

 

 
