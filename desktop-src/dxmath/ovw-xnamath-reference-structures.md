---
Description: Describes the DirectXMath Library types and structures.
ms.assetid: 58acb05d-e79b-8f42-4cf4-76ae57929739
title: DirectXMath Library Structures
ms.topic: reference
ms.date: 05/31/2018
---

# DirectXMath Library Structures

Describes the DirectXMath Library types and structures.

The DirectXMath Library provides a number of structures and defined types to encapsulate data to support ease of use, optimization, and portability. The following list includes structures currently part of the DirectXMath Library. They are available through DirectXMath.h.

## In this section



| Topic                                         | Description                                                                                                                                                              |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**XMBYTE2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmbyte2)<br/>         | A 2D vector where each component is a signed integer, 8-bits (1 byte) in length.<br/>                                                                              |
| [**XMBYTE4**](https://msdn.microsoft.com/library/Ee419276(v=VS.85).aspx)<br/>         | A 4D vector where each component is a signed integer, 8-bits (1 byte) in length. <br/>                                                                             |
| [**XMBYTEN2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmbyten2)<br/>       | A 2D vector for storing signed, normalized values as signed 8-bits (1 byte) integers.<br/>                                                                         |
| [**XMBYTEN4**](https://msdn.microsoft.com/library/Ee419284(v=VS.85).aspx)<br/>       | A 3D vector for storing signed, normalized values as signed 8-bits (1 byte) integers. <br/>                                                                        |
| [**XMCOLOR**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmcolor)<br/>         | A 32-bit Alpha Red Green Blue (ARGB) color vector, where each color channel is specified as an unsigned 8 bit integer.<br/>                                        |
| [**XMDEC4**](https://msdn.microsoft.com/library/Ee419431(v=VS.85).aspx)<br/>           | A 4D vector with x-,y-, and z- components represented as 10 bit signed integer values, and the w-component as a 2 bit signed integer value. <br/>                  |
| [**XMDECN4**](https://msdn.microsoft.com/library/Ee419440(v=VS.85).aspx)<br/>         | A 4D vector for storing signed, normalized values as 10 bit signed x-,y-, and z- components and a 2 bit signed w-component. <br/>                                  |
| [**XMFLOAT2**](https://msdn.microsoft.com/library/Ee419468(v=VS.85).aspx)<br/>       | A 2D vector consisting of two single-precision floating-point values.<br/>                                                                                         |
| [**XMFLOAT2A**](https://msdn.microsoft.com/library/Ee419469(v=VS.85).aspx)<br/>     | Describes an [**XMFLOAT2**](https://msdn.microsoft.com/library/Ee419468(v=VS.85).aspx) structure aligned on a 16-byte boundary.<br/>                                                                            |
| [**XMFLOAT3**](https://msdn.microsoft.com/library/Ee419475(v=VS.85).aspx)<br/>       | Describes a 3D vector consisting of three single-precision floating-point values.<br/>                                                                             |
| [**XMFLOAT3A**](https://msdn.microsoft.com/library/Ee419476(v=VS.85).aspx)<br/>     | Describes an [**XMFLOAT3**](https://msdn.microsoft.com/library/Ee419475(v=VS.85).aspx) structure aligned on a 16-byte boundary.<br/>                                                                            |
| [**XMFLOAT3PK**](https://msdn.microsoft.com/library/Ee419478(v=VS.85).aspx)<br/>   | Describes a 3D vector with X and Y components stored as 11 bit floating point number, and Z component stored as a 10 bit floating-point value. <br/>               |
| [**XMFLOAT3SE**](https://msdn.microsoft.com/library/Ee419489(v=VS.85).aspx)<br/>   | Describes a 3D vector of three floating-point components with 9 bit mantissas, each sharing the same 5-bit exponent. <br/>                                         |
| [**XMFLOAT3X3**](https://msdn.microsoft.com/library/Ee419511(v=VS.85).aspx)<br/>   | A 3\*3 floating point matrix.<br/>                                                                                                                                 |
| [**XMFLOAT4**](https://msdn.microsoft.com/library/Ee419608(v=VS.85).aspx)<br/>       | Describes a 4D vector consisting of four single-precision floating-point values. <br/>                                                                             |
| [**XMFLOAT4A**](https://msdn.microsoft.com/library/Ee419609(v=VS.85).aspx)<br/>     | Describes an [**XMFLOAT4**](https://msdn.microsoft.com/library/Ee419608(v=VS.85).aspx) structure aligned on a 16-byte boundary.<br/>                                                                            |
| [**XMFLOAT4X3**](https://msdn.microsoft.com/library/Ee419611(v=VS.85).aspx)<br/>   | A 4\*3 floating point matrix.<br/>                                                                                                                                 |
| [**XMFLOAT4X3A**](https://msdn.microsoft.com/library/Ee419612(v=VS.85).aspx)<br/> | Describes an [**XMFLOAT4X3**](https://msdn.microsoft.com/library/Ee419611(v=VS.85).aspx) structure aligned on a 16-byte boundary.<br/>                                                                        |
| [**XMFLOAT4X4**](https://msdn.microsoft.com/library/Ee419621(v=VS.85).aspx)<br/>   | A 4\*4 floating point matrix.<br/>                                                                                                                                 |
| [**XMFLOAT4X4A**](https://msdn.microsoft.com/library/Ee419623(v=VS.85).aspx)<br/> | Describes an [**XMFLOAT4X4**](https://msdn.microsoft.com/library/Ee419621(v=VS.85).aspx) structure aligned on a 16-byte boundary.<br/>                                                                        |
| [**XMHALF2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmhalf2)<br/>         | A 2D vector consisting of two half-precision (16bit) floating-point values. <br/>                                                                                  |
| [**XMHALF4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmhalf4)<br/>         | Describes a 4D vector consisting of four half-precision (16-bit) floating-point values. <br/>                                                                      |
| [**XMINT2**](https://msdn.microsoft.com/library/Hh404654(v=VS.85).aspx)<br/>           | A 2D vector where each component is a signed integer.<br/>                                                                                                         |
| [**XMINT3**](https://msdn.microsoft.com/library/Hh404659(v=VS.85).aspx)<br/>           | A 3D vector where each component is a signed integer.<br/>                                                                                                         |
| [**XMINT4**](https://msdn.microsoft.com/library/Hh404664(v=VS.85).aspx)<br/>           | A 4D vector where each component is a signed integer.<br/>                                                                                                         |
| [**XMMATRIX**](https://msdn.microsoft.com/library/Ee419959(v=VS.85).aspx)<br/>       | Describes a 4\*4 matrix aligned on a 16-byte boundary that maps to four hardware vector registers.<br/>                                                            |
| [**XMSHORT2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmshort2)<br/>       | Describes a 2D vector consisting of 16-bit signed and normalized integer components. <br/>                                                                         |
| [**XMSHORT4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmshort4)<br/>       | A 4D vector consisting of 16-bit signed integer components. <br/>                                                                                                  |
| [**XMSHORTN2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmshortn2)<br/>     | A 2D vector for storing signed, normalized values as signed 16-bit integers (type `int16_t`). <br/>                                                                |
| [**XMSHORTN4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmshortn4)<br/>     | A 4D vector for storing signed, normalized values as signed 16-bit integers, (type `int16_t`). <br/>                                                               |
| [**XMU555**](https://msdn.microsoft.com/library/Ee420402(v=VS.85).aspx)<br/>           | A 4D vector with x-,y-, and z- components represented as 5 bit unsigned integer values, and the w-component as a 1 bit integer value. <br/>                        |
| [**XMU565**](https://msdn.microsoft.com/library/Ee420413(v=VS.85).aspx)<br/>           | A 3D vector with x- and z- components represented as 5-bit unsigned integer values, and the y- component as a 6-bit unsigned integer value.<br/>                   |
| [**XMUBYTE2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmubyte2)<br/>       | Describes a 2D vector where each component is a unsigned integer, 8-bits (1 byte) in length.<br/>                                                                  |
| [**XMUBYTE4**](https://msdn.microsoft.com/library/Ee420424(v=VS.85).aspx)<br/>       | Describes a 4D vector where each component is a unsigned integer, 8-bits (1 byte) in length. <br/>                                                                 |
| [**XMUBYTEN2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmubyten2)<br/>     | A 2D vector for storing unsigned, normalized values as signed 8-bits (1 byte) integers.<br/>                                                                       |
| [**XMUBYTEN4**](https://msdn.microsoft.com/library/Ee420492(v=VS.85).aspx)<br/>     | A 3D vector for storing unsigned, normalized values as signed 8-bits (1 byte) integers. <br/>                                                                      |
| [**XMUDEC4**](https://msdn.microsoft.com/library/Ee420508(v=VS.85).aspx)<br/>         | A 4D vector with x-,y-, and z- components represented as 10 bit unsigned integer values, and the w-component as a 2 bit unsigned integer value. <br/>              |
| [**XMUDECN4**](https://msdn.microsoft.com/library/Ee420527(v=VS.85).aspx)<br/>       | A 4D vector for storing unsigned, normalized integer values as 10 bit unsigned x-, y-, and z-components and a 2-bit unsigned w-component. <br/>                    |
| [**XMUINT2**](https://msdn.microsoft.com/library/Hh404745(v=VS.85).aspx)<br/>         | A 2D vector where each component is an unsigned integer.<br/>                                                                                                      |
| [**XMUINT3**](https://msdn.microsoft.com/library/Hh404750(v=VS.85).aspx)<br/>         | A 3D vector where each component is an unsigned integer.<br/>                                                                                                      |
| [**XMUINT4**](https://msdn.microsoft.com/library/Hh404755(v=VS.85).aspx)<br/>         | A 4D vector where each component is an unsigned integer.<br/>                                                                                                      |
| [**XMUNIBBLE4**](https://msdn.microsoft.com/library/Ee420614(v=VS.85).aspx)<br/>   | A 4D vector with four unsigned 4-bit integer components. <br/>                                                                                                     |
| [**XMUSHORT2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmushort2)<br/>     | Describes a 2D vector consisting of 16-bit unsigned integer components. <br/>                                                                                      |
| [**XMUSHORT4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmushort4)<br/>     | A 4D vector consisting of 16-bit unsigned integer components. <br/>                                                                                                |
| [**XMUSHORTN2**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmushortn2)<br/>   | A 2D vector for storing unsigned, normalized values as unsigned 16-bit integers, (type `uint16_t`). <br/>                                                          |
| [**XMUSHORTN4**](/windows/desktop/api/DirectXPackedVector/ns-directxpackedvector-xmushortn4)<br/>   | A 4D vector for storing unsigned, normalized values as signed 16-bit integers (type `uint16_t`). <br/>                                                             |
| [**XMXDEC4**](https://msdn.microsoft.com/library/Ee421399(v=VS.85).aspx)<br/>         | A 4D vector with x-,y-, and z- components represented as 10 bit signed integer values, and the w-component as a 2 bit unsigned integer value. <br/>                |
| [**XMXDECN4**](https://msdn.microsoft.com/library/Ee421408(v=VS.85).aspx)<br/>       | A 4D vector for storing signed, normalized values as 10 bit signed x-,y-, and z- components and an unsigned, normalized value as 2 bit unsigned w-component. <br/> |



 

## Related topics

<dl> <dt>

[DirectXMath Programming Reference](ovw-xnamath-reference.md)
</dt> </dl>

 

 




