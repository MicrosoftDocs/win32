---
description: Constants describing the vertex data types supported by a device.
ms.assetid: 751d7b92-b187-40e5-882c-6fdb80e1ff5f
title: D3DDTCAPS
ms.topic: article
ms.date: 05/31/2018
---

# D3DDTCAPS

Constants describing the vertex data types supported by a device.



| \#define              | Value       | Description                                                                                                                   |
|-----------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------|
| D3DDTCAPS\_UBYTE4     | 0x00000001L | 4D unsigned byte.                                                                                                             |
| D3DDTCAPS\_UBYTE4N    | 0x00000002L | Normalized, 4D unsigned byte. Each of the four bytes is normalized by dividing to 255.0.                                      |
| D3DDTCAPS\_SHORT2N    | 0x00000004L | Normalized, 2D signed short, expanded to (first byte/32767.0, second byte/32767.0, 0, 1).                                     |
| D3DDTCAPS\_SHORT4N    | 0x00000008L | Normalized, 4D signed short, expanded to (first byte/32767.0, second byte/32767.0, third byte/32767.0, fourth byte/32767.0).  |
| D3DDTCAPS\_USHORT2N   | 0x00000010L | Normalized, 2D unsigned short, expanded to (first byte/65535.0, second byte/65535.0, 0, 1).                                   |
| D3DDTCAPS\_USHORT4N   | 0x00000020L | Normalized 4D unsigned short, expanded to (first byte/65535.0, second byte/65535.0, third byte/65535.0, fourth byte/65535.0). |
| D3DDTCAPS\_UDEC3      | 0x00000040L | 3D unsigned 10 10 10 format expanded to (value, value, value, 1).                                                             |
| D3DDTCAPS\_DEC3N      | 0x00000080L | 3D signed 10 10 10 format normalized and expanded to (v\[0\]/511.0, v\[1\]/511.0, v\[2\]/511.0, 1).                           |
| D3DDTCAPS\_FLOAT16\_2 | 0x00000100L | 2D 16-bit floating point numbers.                                                                                             |
| D3DDTCAPS\_FLOAT16\_4 | 0x00000200L | 4D 16-bit floating point numbers.                                                                                             |



 

These constants are used by the DeclTypes member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9).

## Constant Information



|                          |            |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 



