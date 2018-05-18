---
Description: 'Describes the DirectXMath Library types and structures.'
ms.assetid: '58acb05d-e79b-8f42-4cf4-76ae57929739'
title: DirectXMath Library Structures
---

# DirectXMath Library Structures

Describes the DirectXMath Library types and structures.

The DirectXMath Library provides a number of structures and defined types to encapsulate data to support ease of use, optimization, and portability. The following list includes structures currently part of the DirectXMath Library. They are available through DirectXMath.h.

## In this section



| Topic                                         | Description                                                                                                                                                              |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**XMBYTE2**](xmbyte2.md)<br/>         | A 2D vector where each component is a signed integer, 8-bits (1 byte) in length.<br/>                                                                              |
| [**XMBYTE4**](xmbyte4.md)<br/>         | A 4D vector where each component is a signed integer, 8-bits (1 byte) in length. <br/>                                                                             |
| [**XMBYTEN2**](xmbyten2.md)<br/>       | A 2D vector for storing signed, normalized values as signed 8-bits (1 byte) integers.<br/>                                                                         |
| [**XMBYTEN4**](xmbyten4.md)<br/>       | A 3D vector for storing signed, normalized values as signed 8-bits (1 byte) integers. <br/>                                                                        |
| [**XMCOLOR**](xmcolor.md)<br/>         | A 32-bit Alpha Red Green Blue (ARGB) color vector, where each color channel is specified as an unsigned 8 bit integer.<br/>                                        |
| [**XMDEC4**](xmdec4.md)<br/>           | A 4D vector with x-,y-, and z- components represented as 10 bit signed integer values, and the w-component as a 2 bit signed integer value. <br/>                  |
| [**XMDECN4**](xmdecn4.md)<br/>         | A 4D vector for storing signed, normalized values as 10 bit signed x-,y-, and z- components and a 2 bit signed w-component. <br/>                                  |
| [**XMFLOAT2**](xmfloat2.md)<br/>       | A 2D vector consisting of two single-precision floating-point values.<br/>                                                                                         |
| [**XMFLOAT2A**](xmfloat2a.md)<br/>     | Describes an [**XMFLOAT2**](xmfloat2.md) structure aligned on a 16-byte boundary.<br/>                                                                            |
| [**XMFLOAT3**](xmfloat3.md)<br/>       | Describes a 3D vector consisting of three single-precision floating-point values.<br/>                                                                             |
| [**XMFLOAT3A**](xmfloat3a.md)<br/>     | Describes an [**XMFLOAT3**](xmfloat3.md) structure aligned on a 16-byte boundary.<br/>                                                                            |
| [**XMFLOAT3PK**](xmfloat3pk.md)<br/>   | Describes a 3D vector with X and Y components stored as 11 bit floating point number, and Z component stored as a 10 bit floating-point value. <br/>               |
| [**XMFLOAT3SE**](xmfloat3se.md)<br/>   | Describes a 3D vector of three floating-point components with 9 bit mantissas, each sharing the same 5-bit exponent. <br/>                                         |
| [**XMFLOAT3X3**](xmfloat3x3.md)<br/>   | A 3\*3 floating point matrix.<br/>                                                                                                                                 |
| [**XMFLOAT4**](xmfloat4.md)<br/>       | Describes a 4D vector consisting of four single-precision floating-point values. <br/>                                                                             |
| [**XMFLOAT4A**](xmfloat4a.md)<br/>     | Describes an [**XMFLOAT4**](xmfloat4.md) structure aligned on a 16-byte boundary.<br/>                                                                            |
| [**XMFLOAT4X3**](xmfloat4x3.md)<br/>   | A 4\*3 floating point matrix.<br/>                                                                                                                                 |
| [**XMFLOAT4X3A**](xmfloat4x3a.md)<br/> | Describes an [**XMFLOAT4X3**](xmfloat4x3.md) structure aligned on a 16-byte boundary.<br/>                                                                        |
| [**XMFLOAT4X4**](xmfloat4x4.md)<br/>   | A 4\*4 floating point matrix.<br/>                                                                                                                                 |
| [**XMFLOAT4X4A**](xmfloat4x4a.md)<br/> | Describes an [**XMFLOAT4X4**](xmfloat4x4.md) structure aligned on a 16-byte boundary.<br/>                                                                        |
| [**XMHALF2**](xmhalf2.md)<br/>         | A 2D vector consisting of two half-precision (16bit) floating-point values. <br/>                                                                                  |
| [**XMHALF4**](xmhalf4.md)<br/>         | Describes a 4D vector consisting of four half-precision (16-bit) floating-point values. <br/>                                                                      |
| [**XMINT2**](xmint2.md)<br/>           | A 2D vector where each component is a signed integer.<br/>                                                                                                         |
| [**XMINT3**](xmint3.md)<br/>           | A 3D vector where each component is a signed integer.<br/>                                                                                                         |
| [**XMINT4**](xmint4.md)<br/>           | A 4D vector where each component is a signed integer.<br/>                                                                                                         |
| [**XMMATRIX**](xmmatrix.md)<br/>       | Describes a 4\*4 matrix aligned on a 16-byte boundary that maps to four hardware vector registers.<br/>                                                            |
| [**XMSHORT2**](xmshort2.md)<br/>       | Describes a 2D vector consisting of 16-bit signed and normalized integer components. <br/>                                                                         |
| [**XMSHORT4**](xmshort4.md)<br/>       | A 4D vector consisting of 16-bit signed integer components. <br/>                                                                                                  |
| [**XMSHORTN2**](xmshortn2.md)<br/>     | A 2D vector for storing signed, normalized values as signed 16-bit integers (type `int16_t`). <br/>                                                                |
| [**XMSHORTN4**](xmshortn4.md)<br/>     | A 4D vector for storing signed, normalized values as signed 16-bit integers, (type `int16_t`). <br/>                                                               |
| [**XMU555**](xmu555.md)<br/>           | A 4D vector with x-,y-, and z- components represented as 5 bit unsigned integer values, and the w-component as a 1 bit integer value. <br/>                        |
| [**XMU565**](xmu565.md)<br/>           | A 3D vector with x- and z- components represented as 5-bit unsigned integer values, and the y- component as a 6-bit unsigned integer value.<br/>                   |
| [**XMUBYTE2**](xmubyte2.md)<br/>       | Describes a 2D vector where each component is a unsigned integer, 8-bits (1 byte) in length.<br/>                                                                  |
| [**XMUBYTE4**](xmubyte4.md)<br/>       | Describes a 4D vector where each component is a unsigned integer, 8-bits (1 byte) in length. <br/>                                                                 |
| [**XMUBYTEN2**](xmubyten2.md)<br/>     | A 2D vector for storing unsigned, normalized values as signed 8-bits (1 byte) integers.<br/>                                                                       |
| [**XMUBYTEN4**](xmubyten4.md)<br/>     | A 3D vector for storing unsigned, normalized values as signed 8-bits (1 byte) integers. <br/>                                                                      |
| [**XMUDEC4**](xmudec4.md)<br/>         | A 4D vector with x-,y-, and z- components represented as 10 bit unsigned integer values, and the w-component as a 2 bit unsigned integer value. <br/>              |
| [**XMUDECN4**](xmudecn4.md)<br/>       | A 4D vector for storing unsigned, normalized integer values as 10 bit unsigned x-, y-, and z-components and a 2-bit unsigned w-component. <br/>                    |
| [**XMUINT2**](xmuint2.md)<br/>         | A 2D vector where each component is an unsigned integer.<br/>                                                                                                      |
| [**XMUINT3**](xmuint3.md)<br/>         | A 3D vector where each component is an unsigned integer.<br/>                                                                                                      |
| [**XMUINT4**](xmuint4.md)<br/>         | A 4D vector where each component is an unsigned integer.<br/>                                                                                                      |
| [**XMUNIBBLE4**](xmunibble4.md)<br/>   | A 4D vector with four unsigned 4-bit integer components. <br/>                                                                                                     |
| [**XMUSHORT2**](xmushort2.md)<br/>     | Describes a 2D vector consisting of 16-bit unsigned integer components. <br/>                                                                                      |
| [**XMUSHORT4**](xmushort4.md)<br/>     | A 4D vector consisting of 16-bit unsigned integer components. <br/>                                                                                                |
| [**XMUSHORTN2**](xmushortn2.md)<br/>   | A 2D vector for storing unsigned, normalized values as unsigned 16-bit integers, (type `uint16_t`). <br/>                                                          |
| [**XMUSHORTN4**](xmushortn4.md)<br/>   | A 4D vector for storing unsigned, normalized values as signed 16-bit integers (type `uint16_t`). <br/>                                                             |
| [**XMXDEC4**](xmxdec4.md)<br/>         | A 4D vector with x-,y-, and z- components represented as 10 bit signed integer values, and the w-component as a 2 bit unsigned integer value. <br/>                |
| [**XMXDECN4**](xmxdecn4.md)<br/>       | A 4D vector for storing signed, normalized values as 10 bit signed x-,y-, and z- components and an unsigned, normalized value as 2 bit unsigned w-component. <br/> |



 

## Related topics

<dl> <dt>

[DirectXMath Programming Reference](ovw-xnamath-reference.md)
</dt> </dl>

 

 




