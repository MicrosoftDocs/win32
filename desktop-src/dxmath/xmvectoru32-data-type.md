---
description: An opaque, portable type to support the use of C/C++ initializer syntax to load uint32\_t values into an instance of XMVECTOR type.
ms.assetid: 1ac1f48a-cd7f-7741-933f-c341fc42a21c
title: XMVECTORU32 Data Type (Directxmath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVECTORU32 Data Type

An opaque, portable type to support the use of C/C++ initializer syntax to load uint32\_t values into an instance of [**XMVECTOR**](xmvector-data-type.md) type.


```C++
typedef XMVECTOR32 vectoru32;
```



## Remarks

For a list of additional functionality, such as constructors and operators, available using XMVECTORU32 when programming in C++, see [XMVECTORU32 Extensions](ovw-xmvectoru32-extensions.md).

The [**XMVECTORF32**](xmvectorf32-data-type.md), **XMVECTORU32**, [**XMVECTORI32**](xmvectori32-data-type.md), and [**XMVECTORU8**](xmvectoru8-data-type.md) structures are provided as a mechanism for creating [**XMVECTOR**](xmvector-data-type.md) from different constant data types (floating point, unsigned integer, integer, and byte) using initializers.

This is necessary to support [**XMVECTOR**](xmvector-data-type.md), as it does not itself support initializers, for portability and optimization reasons.

For example:

``` syntax
XMVECTOR data;
XMVECTORU32 uintVector = { 0xf7000000, 0x8310000, 0x1000000, 0 };
data = uintVector;
```

**Namespace**: Use DirectX

### Platform Requirements

Microsoft Visual Studio 2010 or Microsoft Visual Studio 2012 with the Windows SDK for Windows 8. Supported for Win32 desktop apps, Windows Store apps, and Windows Phone 8 apps.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Directxmath.h</dt> </dl> |



## See also

<dl> <dt>

[DirectXMath Library Types](ovw-xnamath-reference-types.md)
</dt> <dt>

[**XMVECTORI32 Data Type**](xmvectori32-data-type.md)
</dt> <dt>

[**XMVECTORF32 Data Type**](xmvectorf32-data-type.md)
</dt> <dt>

[**XMVECTOR Data Type**](xmvector-data-type.md)
</dt> <dt>

[**XMVECTORU8 Data Type**](xmvectoru8-data-type.md)
</dt> <dt>

[XMVECTORU32 Extensions](ovw-xmvectoru32-extensions.md)
</dt> </dl>

 

 




