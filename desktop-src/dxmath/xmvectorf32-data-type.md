---
description: An opaque, portable type to support the use of C/C++ initializer syntax to load floating-point values into an instance of XMVECTOR type.
ms.assetid: bafaa59f-fd1b-e252-cbbd-903df796fde0
title: XMVECTORF32 Data Type (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVECTORF32 Data Type

An opaque, portable type to support the use of C/C++ initializer syntax to load floating-point values into an instance of [**XMVECTOR**](xmvector-data-type.md) type.


```C++
typedef XMVECTORF32 vectorf32;
```



## Remarks

For a list of additional functionality, such as constructors and operators, available using `XMVECTORF32` when programming in C++, see [XMVECTORF32 Extensions](ovw-xmvectorf32-extensions.md).

The **XMVECTORF32**, [**XMVECTORU32**](xmvectoru32-data-type.md), [**XMVECTORI32**](xmvectori32-data-type.md), and [**XMVECTORU8**](xmvectoru8-data-type.md) structures are provided as a mechanism for creating [**XMVECTOR**](xmvector-data-type.md) from different constant data types (floating point, unsigned integer, integer, and byte) using initializers.

This is necessary to support [**XMVECTOR**](xmvector-data-type.md), as it does not itself support initializers, for portability and optimization reasons.

For example:


```
XMVECTOR data;
XMVECTORF32 floatingVector = { 0.f, 0.f, 0.1f, 1.f };
data = floatingVector;
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

[**XMVECTORI32 Data Type**](xmvectori32-data-type.md)
</dt> <dt>

[**XMVECTOR Data Type**](xmvector-data-type.md)
</dt> <dt>

[**XMVECTORU32 Data Type**](xmvectoru32-data-type.md)
</dt> <dt>

[**XMVECTORU8 Data Type**](xmvectoru8-data-type.md)
</dt> <dt>

[**XMVECTORF32 Data Type**](xmvectorf32-data-type.md)
</dt> </dl>

 

 




