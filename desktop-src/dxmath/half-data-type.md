---
description: An alias to uint16\_t packed with a 16-bit floating-point number consisting of a sign bit, a 5-bit biased exponent, and a 10-bit mantissa.
ms.assetid: E84E0EBA-5C34-41AA-84DB-7A65EBDCAD15
title: HALF Data Type (DirectXPackedVector.h)
ms.topic: reference
ms.date: 05/31/2018
---

# HALF Data Type

An alias to **uint16\_t** packed with a 16-bit floating-point number consisting of a sign bit, a 5-bit biased exponent, and a 10-bit mantissa.


```C++
typedef uint16_t HALF;
```



## Remarks

The HALF data type is equivalent to the IEEE 754 binary16 format.

HALF\_MIN = 6.10352e-5f

HALF\_MAX = 65504.f

For more info about the HALF data type, see [Half-precision floating-point format](https://en.wikipedia.org/wiki/Half_precision_floating-point_format).

**Namespace**: Use DirectX::PackedVector

### Platform Requirements

Microsoft Visual Studio 2010 or Microsoft Visual Studio 2012 with the Windows SDK for Windows 8. Supported for Win32 desktop apps, Windows Store apps, and Windows Phone 8 apps.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>DirectXPackedVector.h</dt> </dl> |



## See also

<dl> <dt>

[DirectXMath Library Types](ovw-xnamath-reference-types.md)
</dt> </dl>

 

 




