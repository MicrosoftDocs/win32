---
description: Driver stencil capability flags.
ms.assetid: 187c758c-5e7f-48ee-97cb-b1f30b709723
title: D3DSTENCILCAPS
ms.topic: article
ms.date: 05/31/2018
---

# D3DSTENCILCAPS

Driver stencil capability flags.



| \#define                 | Value       | Description                                                                                           |
|--------------------------|-------------|-------------------------------------------------------------------------------------------------------|
| D3DSTENCILCAPS\_KEEP     | 0x00000001L | Do not update the entry in the stencil buffer. This is the default value.                             |
| D3DSTENCILCAPS\_ZERO     | 0x00000002L | Set the stencil-buffer entry to 0.                                                                    |
| D3DSTENCILCAPS\_REPLACE  | 0x00000004L | Replace the stencil-buffer entry with reference value.                                                |
| D3DSTENCILCAPS\_INCRSAT  | 0x00000008L | Increment the stencil-buffer entry, clamping to the maximum value.                                    |
| D3DSTENCILCAPS\_DECRSAT  | 0x00000010L | Decrement the stencil-buffer entry, clamping to zero.                                                 |
| D3DSTENCILCAPS\_INVERT   | 0x00000020L | Invert the bits in the stencil-buffer entry.                                                          |
| D3DSTENCILCAPS\_INCR     | 0x00000040L | Increment the stencil-buffer entry, wrapping to zero if the new value exceeds the maximum value.      |
| D3DSTENCILCAPS\_DECR     | 0x00000080L | Decrement the stencil-buffer entry, wrapping to the maximum value if the new value is less than zero. |
| D3DSTENCILCAPS\_TWOSIDED | 0x00000100L | The device supports two-sided stencil.                                                                |



 

Stencil-buffer entries are integer values ranging from 0 through 2ⁿ - 1, where n is the bit depth of the stencil buffer.

These constants are used by the StencilCaps member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9).

## Constant Information



|                          |            |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 



