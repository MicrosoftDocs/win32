---
description: An opaque, portable type to support the use of C/C++ initializer syntax to load uint8\_t values into an instance of XMVECTOR type.
ms.assetid: ab73ac2c-f178-1bb9-910d-9eef5fc6f5df
title: XMVECTORU8 Data Type (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVECTORU8 Data Type

An opaque, portable type to support the use of C/C++ initializer syntax to load uint8\_t values into an instance of [**XMVECTOR**](xmvector-data-type.md) type.


```C++
typedef XMVECTORU8 vectoru8;
```



## Remarks

For a list of additional functionality, such as constructors and operators, available using XMVECTORU8 when programming in C++, see [XMVECTORU8 Extensions](ovw-xmvectoru8-extensions.md).

The [**XMVECTORF32**](xmvectorf32-data-type.md), [**XMVECTORU32**](xmvectoru32-data-type.md), [**XMVECTORI32**](xmvectori32-data-type.md), and **XMVECTORU8** structures are provided as a mechanism for creating [**XMVECTOR**](xmvector-data-type.md) from different constant data types (floating point, unsigned integer, integer, and byte) using initializers.

This is necessary to support [**XMVECTOR**](xmvector-data-type.md), as it does not itself support initializers, for portability and optimization reasons.

For example:

``` syntax
XMVECTOR data;
XMVECTORU8  byteVector = { (uint8_t)  1,(uint8_t) 16,(uint8_t)101,(uint8_t) 62,
                           (uint8_t)  4,(uint8_t)  0,(uint8_t)  2,(uint8_t) 99,
                           (uint8_t)  9,(uint8_t) 18,(uint8_t)  0,(uint8_t)  0,
                           (uint8_t)100,(uint8_t) 51,(uint8_t) 23,(uint8_t)117};

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

[**XMVECTOR Data Type**](xmvector-data-type.md)
</dt> <dt>

[**XMVECTORF32 Data Type**](xmvectorf32-data-type.md)
</dt> <dt>

[**XMVECTORI32 Data Type**](xmvectori32-data-type.md)
</dt> <dt>

[**XMVECTORU32 Data Type**](xmvectoru32-data-type.md)
</dt> <dt>

[XMVECTORU8 Extensions](ovw-xmvectoru8-extensions.md)
</dt> </dl>

 

 




