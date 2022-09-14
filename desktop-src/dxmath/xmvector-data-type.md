---
description: A portable type used to represent a vector of four 32-bit floating-point or integer components, each aligned optimally and mapped to a hardware vector register.
ms.assetid: 1a044094-444d-e787-fa6a-76e88531aef1
title: XMVECTOR Data Type (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVECTOR Data Type

A portable type used to represent a vector of four 32-bit floating-point or integer components, each aligned optimally and mapped to a hardware vector register.

## Remarks

For a list of additional functionality, such as constructors and operators, available using `XMVECTOR` when programming in C++, see [XMVECTOR Extensions](ovw-xmvector-extensions.md).

In the DirectXMath Library, to fully support portability and optimization, `XMVECTOR` is, by design, an opaque type. The actual implementation of `XMVECTOR` is platform dependent.

In general, code should not rely on the specifics of any given platform specific implementation of `XMVECTOR`. Platform-specific implementations have these characteristics:

-   They are not portable.
-   They may change between releases.
-   Injudicious use of implementation details may be suboptimal.

Developers should use DirectXMath Library's [accessor](ovw-xnamath-reference-functions-accessors.md), [load](ovw-xnamath-reference-functions-load.md), and [store](ovw-xnamath-reference-functions-storage.md) functions to get and set the vectors, and the [DirectXMath Library 4D Vector Functions](ovw-xnamath-reference-functions-vector4.md) to manipulate them.

For projects that need detailed information about how to implement `XMVECTOR` on different platforms, see [Library Internals](pg-xnamath-internals.md).

### Compiler Aliases

The DirectXMath.h header file uses aliases to the `XMVECTOR` object, specifically **CXMVECTOR** and **FXMVECTOR**. The header uses these aliases to comply with the optimal in-line calling conventions of different compilers. For most projects that use DirectXMath it is sufficient to treat these types as an exact alias to `XMVECTOR`.

For example:


```
[CDATA[
typedef const XMVECTOR FXMVECTOR;
typedef const XMVECTOR CXMVECTOR;
]]
```



For projects that need detailed information about how different platforms handle their calling conventions, see [Library Internals](pg-xnamath-internals.md).

For XNAMATH 2.x, the `XMVECTOR` data type has .x, .y, .z, .and .w element members, which generally cause poor performance. The use of the XM\_STRICT\_VECTOR4 type provides an opt-in of the DirectXMath definition of an opaque data type.

**Namespace**: Use DirectX

### Platform Requirements

Microsoft Visual Studio 2010 or Microsoft Visual Studio 2012 with the Windows SDK for Windows 8. Supported for Win32 desktop apps, Windows Store apps, and Windows Phone 8 apps.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>DirectXMath.h</dt> </dl> |



## See also

<dl> <dt>

[DirectXMath Library Types](ovw-xnamath-reference-types.md)
</dt> <dt>

[**XMVECTORI32 Data Type**](xmvectori32-data-type.md)
</dt> <dt>

[**XMVECTORF32 Data Type**](xmvectorf32-data-type.md)
</dt> <dt>

[**XMVECTORU32 Data Type**](xmvectoru32-data-type.md)
</dt> <dt>

[**XMVECTORU8 Data Type**](xmvectoru8-data-type.md)
</dt> <dt>

[**XMVECTOR Data Type**](xmvector-data-type.md)
</dt> </dl>

 

 




