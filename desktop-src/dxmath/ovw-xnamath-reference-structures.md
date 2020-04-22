---
Description: Describes the DirectXMath Library types and structures.
ms.assetid: 58acb05d-e79b-8f42-4cf4-76ae57929739
title: DirectXMath Library structures
ms.topic: reference
ms.date: 05/31/2018
---

# DirectXMath Library structures

Describes the DirectXMath Library types and structures.

The DirectXMath Library provides a number of structures and defined types to encapsulate data to support ease of use, optimization, and portability. The following list includes structures currently part of the DirectXMath Library. They are available through DirectXMath.h.

## In this section

| Topic | Description |
|-|-|
| [**XMBYTE2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmbyte2) | A 2D vector where each component is a signed integer, 8-bits (1 byte) in length. |
| [**XMBYTE4**](https://msdn.microsoft.com/library/Ee419276(v=VS.85).aspx) | A 4D vector where each component is a signed integer, 8-bits (1 byte) in length.  |
| [**XMBYTEN2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmbyten2) | A 2D vector for storing signed, normalized values as signed 8-bits (1 byte) integers. |
| [**XMBYTEN4**](https://msdn.microsoft.com/library/Ee419284(v=VS.85).aspx) | A 3D vector for storing signed, normalized values as signed 8-bits (1 byte) integers.  |
| [**XMCOLOR**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmcolor) | A 32-bit Alpha Red Green Blue (ARGB) color vector, where each color channel is specified as an unsigned 8 bit integer. |
| [**XMDEC4**](https://msdn.microsoft.com/library/Ee419431(v=VS.85).aspx) | A 4D vector with x-,y-, and z- components represented as 10 bit signed integer values, and the w-component as a 2 bit signed integer value.  |
| [**XMDECN4**](https://msdn.microsoft.com/library/Ee419440(v=VS.85).aspx) | A 4D vector for storing signed, normalized values as 10 bit signed x-,y-, and z- components and a 2 bit signed w-component.  |
| [**XMFLOAT2**](https://msdn.microsoft.com/library/Ee419468(v=VS.85).aspx) | A 2D vector consisting of two single-precision floating-point values. |
| [**XMFLOAT2A**](https://msdn.microsoft.com/library/Ee419469(v=VS.85).aspx) | Describes an [**XMFLOAT2**](https://msdn.microsoft.com/library/Ee419468(v=VS.85).aspx) structure aligned on a 16-byte boundary. |
| [**XMFLOAT3**](https://msdn.microsoft.com/library/Ee419475(v=VS.85).aspx) | Describes a 3D vector consisting of three single-precision floating-point values. |
| [**XMFLOAT3A**](https://msdn.microsoft.com/library/Ee419476(v=VS.85).aspx) | Describes an [**XMFLOAT3**](https://msdn.microsoft.com/library/Ee419475(v=VS.85).aspx) structure aligned on a 16-byte boundary. |
| [**XMFLOAT3PK**](https://msdn.microsoft.com/library/Ee419478(v=VS.85).aspx) | Describes a 3D vector with X and Y components stored as 11 bit floating point number, and Z component stored as a 10 bit floating-point value.  |
| [**XMFLOAT3SE**](https://msdn.microsoft.com/library/Ee419489(v=VS.85).aspx) | Describes a 3D vector of three floating-point components with 9 bit mantissas, each sharing the same 5-bit exponent.  |
| [**XMFLOAT3X3**](/windows/win32/api/directxmath/ns-directxmath-xmfloat3x3) | A 3x3 floating point matrix. |
| [**XMFLOAT3X4**](/windows/win32/api/directxmath/ns-directxmath-xmfloat3x4) | A 3x4 column-major matrix containing 32-bit floating-point components. |
| [**XMFLOAT3X4A**](/windows/win32/api/directxmath/ns-directxmath-xmfloat3x4a) | A 3x4 column-major matrix containing 32-bit floating-point components aligned on a 16-byte boundary. |
| [**XMFLOAT4**](https://msdn.microsoft.com/library/Ee419608(v=VS.85).aspx) | Describes a 4D vector consisting of four single-precision floating-point values.  |
| [**XMFLOAT4A**](https://msdn.microsoft.com/library/Ee419609(v=VS.85).aspx) | Describes an [**XMFLOAT4**](https://msdn.microsoft.com/library/Ee419608(v=VS.85).aspx) structure aligned on a 16-byte boundary. |
| [**XMFLOAT4X3**](https://msdn.microsoft.com/library/Ee419611(v=VS.85).aspx) | A 4x3 floating point matrix. |
| [**XMFLOAT4X3A**](https://msdn.microsoft.com/library/Ee419612(v=VS.85).aspx) | Describes an [**XMFLOAT4X3**](https://msdn.microsoft.com/library/Ee419611(v=VS.85).aspx) structure aligned on a 16-byte boundary. |
| [**XMFLOAT4X4**](https://msdn.microsoft.com/library/Ee419621(v=VS.85).aspx) | A 4x4 floating point matrix. |
| [**XMFLOAT4X4A**](https://msdn.microsoft.com/library/Ee419623(v=VS.85).aspx) | Describes an [**XMFLOAT4X4**](https://msdn.microsoft.com/library/Ee419621(v=VS.85).aspx) structure aligned on a 16-byte boundary. |
| [**XMHALF2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmhalf2) | A 2D vector consisting of two half-precision (16bit) floating-point values.  |
| [**XMHALF4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmhalf4) | Describes a 4D vector consisting of four half-precision (16-bit) floating-point values.  |
| [**XMINT2**](https://msdn.microsoft.com/library/Hh404654(v=VS.85).aspx) | A 2D vector where each component is a signed integer. |
| [**XMINT3**](https://msdn.microsoft.com/library/Hh404659(v=VS.85).aspx) | A 3D vector where each component is a signed integer. |
| [**XMINT4**](https://msdn.microsoft.com/library/Hh404664(v=VS.85).aspx) | A 4D vector where each component is a signed integer. |
| [**XMMATRIX**](https://msdn.microsoft.com/library/Ee419959(v=VS.85).aspx) | Describes a 4x4 matrix aligned on a 16-byte boundary that maps to four hardware vector registers. |
| [**XMSHORT2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmshort2) | Describes a 2D vector consisting of 16-bit signed and normalized integer components.  |
| [**XMSHORT4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmshort4) | A 4D vector consisting of 16-bit signed integer components.  |
| [**XMSHORTN2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmshortn2) | A 2D vector for storing signed, normalized values as signed 16-bit integers (type `int16_t`).  |
| [**XMSHORTN4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmshortn4) | A 4D vector for storing signed, normalized values as signed 16-bit integers, (type `int16_t`).  |
| [**XMU555**](https://msdn.microsoft.com/library/Ee420402(v=VS.85).aspx) | A 4D vector with x-,y-, and z- components represented as 5 bit unsigned integer values, and the w-component as a 1 bit integer value.  |
| [**XMU565**](https://msdn.microsoft.com/library/Ee420413(v=VS.85).aspx) | A 3D vector with x- and z- components represented as 5-bit unsigned integer values, and the y- component as a 6-bit unsigned integer value. |
| [**XMUBYTE2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmubyte2) | Describes a 2D vector where each component is a unsigned integer, 8-bits (1 byte) in length. |
| [**XMUBYTE4**](https://msdn.microsoft.com/library/Ee420424(v=VS.85).aspx) | Describes a 4D vector where each component is a unsigned integer, 8-bits (1 byte) in length.  |
| [**XMUBYTEN2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmubyten2) | A 2D vector for storing unsigned, normalized values as signed 8-bits (1 byte) integers. |
| [**XMUBYTEN4**](https://msdn.microsoft.com/library/Ee420492(v=VS.85).aspx) | A 3D vector for storing unsigned, normalized values as signed 8-bits (1 byte) integers.  |
| [**XMUDEC4**](https://msdn.microsoft.com/library/Ee420508(v=VS.85).aspx) | A 4D vector with x-,y-, and z- components represented as 10 bit unsigned integer values, and the w-component as a 2 bit unsigned integer value.  |
| [**XMUDECN4**](https://msdn.microsoft.com/library/Ee420527(v=VS.85).aspx) | A 4D vector for storing unsigned, normalized integer values as 10 bit unsigned x-, y-, and z-components and a 2-bit unsigned w-component.  |
| [**XMUINT2**](https://msdn.microsoft.com/library/Hh404745(v=VS.85).aspx) | A 2D vector where each component is an unsigned integer. |
| [**XMUINT3**](https://msdn.microsoft.com/library/Hh404750(v=VS.85).aspx) | A 3D vector where each component is an unsigned integer. |
| [**XMUINT4**](https://msdn.microsoft.com/library/Hh404755(v=VS.85).aspx) | A 4D vector where each component is an unsigned integer. |
| [**XMUNIBBLE4**](https://msdn.microsoft.com/library/Ee420614(v=VS.85).aspx) | A 4D vector with four unsigned 4-bit integer components.  |
| [**XMUSHORT2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmushort2) | Describes a 2D vector consisting of 16-bit unsigned integer components.  |
| [**XMUSHORT4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmushort4) | A 4D vector consisting of 16-bit unsigned integer components.  |
| [**XMUSHORTN2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmushortn2) | A 2D vector for storing unsigned, normalized values as unsigned 16-bit integers, (type `uint16_t`).  |
| [**XMUSHORTN4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmushortn4) | A 4D vector for storing unsigned, normalized values as signed 16-bit integers (type `uint16_t`).  |
| [**XMXDEC4**](https://msdn.microsoft.com/library/Ee421399(v=VS.85).aspx) | A 4D vector with x-,y-, and z- components represented as 10 bit signed integer values, and the w-component as a 2 bit unsigned integer value.  |
| [**XMXDECN4**](https://msdn.microsoft.com/library/Ee421408(v=VS.85).aspx) | A 4D vector for storing signed, normalized values as 10 bit signed x-,y-, and z- components and an unsigned, normalized value as 2 bit unsigned w-component.  |

## Related topics

<dl> <dt>

[DirectXMath Programming Reference](ovw-xnamath-reference.md)
</dt> </dl>