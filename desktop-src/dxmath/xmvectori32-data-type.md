---
description: An opaque, portable type to support the use of C/C++ initializer syntax to load integer values into an instance of XMVECTOR type.
ms.assetid: 6564030e-b6e9-0c4f-4e2a-4132e4264c94
title: XMVECTORI32 Data Type (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVECTORI32 Data Type

An opaque, portable type to support the use of C/C++ initializer syntax to load integer values into an instance of [**XMVECTOR**](xmvector-data-type.md) type.


```C++
typedef XMVECTORI32 vectori32;
```



## Remarks

For a list of additional functionality, such as constructors and operators, available using `XMVECTORI32` when programming in C++, see [XMVECTORI32 Extensions](ovw-xmvectori32-extensions.md).

The [**XMVECTORF32**](xmvectorf32-data-type.md), [**XMVECTORU32**](xmvectoru32-data-type.md), **XMVECTORI32**, and [**XMVECTORU8**](xmvectoru8-data-type.md) structures are provided as a mechanism for creating [**XMVECTOR**](xmvector-data-type.md) from different constant data types (floating point, unsigned integer, integer, and byte) using initializers.

This is necessary to support [**XMVECTOR**](xmvector-data-type.md), as it does not itself support initializers, for portability and optimization reasons.

For example:


```
XMVECTOR data;
XMVECTORI32 intVector = { -1, 5, 33, 0 };
data = intVector;
```



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

[**XMVECTOR Data Type**](xmvector-data-type.md)
</dt> <dt>

[**XMVECTORF32 Data Type**](xmvectorf32-data-type.md)
</dt> <dt>

[**XMVECTORU32 Data Type**](xmvectoru32-data-type.md)
</dt> <dt>

[**XMVECTORU8 Data Type**](xmvectoru8-data-type.md)
</dt> <dt>

[**XMVECTORI32 Data Type**](xmvectori32-data-type.md)
</dt> </dl>

 

 




