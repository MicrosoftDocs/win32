---
Description: Vertex shader caps constants. These constants are used by the VS20Caps member of D3DCAPS9.
ms.assetid: c1321957-4ba5-45d0-984a-4f4267221c59
title: D3DVS20CAPS
ms.topic: article
ms.date: 05/31/2018
---

# D3DVS20CAPS

Vertex shader caps constants. These constants are used by the VS20Caps member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9).



| \#define                              | Value          | Description                                                                                                                                                                                                                                                                                                 |
|---------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DVS20CAPS\_PREDICATION              | (1 << 0) | Instruction predication is supported. See [setp\_comp - vs](https://msdn.microsoft.com/en-us/library/Bb147357(v=VS.85).aspx).                                                                                                                                                                                                                   |
| D3DVS20\_MAX\_DYNAMICFLOWCONTROLDEPTH | 24             | The maximum level of nesting of dynamic flow control instructions ([break - vs](https://msdn.microsoft.com/en-us/library/Bb172369(v=VS.85).aspx), [break\_comp - vs](https://msdn.microsoft.com/en-us/library/Bb172366(v=VS.85).aspx), [breakp - vs](https://msdn.microsoft.com/en-us/library/Bb172364(v=VS.85).aspx), [if\_comp - vs](https://msdn.microsoft.com/en-us/library/Bb174583(v=VS.85).aspx), if\_comp - vs, [if pred - vs](https://msdn.microsoft.com/en-us/library/Bb174585(v=VS.85).aspx)). |
| D3DVS20\_MIN\_DYNAMICFLOWCONTROLDEPTH | 0              | The minimum level of nesting of dynamic flow control instructions ([break - vs](https://msdn.microsoft.com/en-us/library/Bb172369(v=VS.85).aspx), [break\_comp - vs](https://msdn.microsoft.com/en-us/library/Bb172366(v=VS.85).aspx), [breakp - vs](https://msdn.microsoft.com/en-us/library/Bb172364(v=VS.85).aspx), [if\_comp - vs](https://msdn.microsoft.com/en-us/library/Bb174583(v=VS.85).aspx), if\_comp - vs, [if pred - vs](https://msdn.microsoft.com/en-us/library/Bb174585(v=VS.85).aspx)). |
| D3DVS20\_MAX\_NUMTEMPS                | 32             | The maximum number of temporary registers supported.                                                                                                                                                                                                                                                        |
| D3DVS20\_MIN\_NUMTEMPS                | 12             | The minimum number of temporary registers supported.                                                                                                                                                                                                                                                        |
| D3DVS20\_MAX\_STATICFLOWCONTROLDEPTH  | 4              | The maximum depth of nesting of the [loop - vs](https://msdn.microsoft.com/en-us/library/Bb174716(v=VS.85).aspx)/[rep - vs](https://msdn.microsoft.com/en-us/library/Bb147331(v=VS.85).aspx) and [call - vs](https://msdn.microsoft.com/en-us/library/Bb172389(v=VS.85).aspx)/[callnz bool - vs](https://msdn.microsoft.com/en-us/library/Bb172385(v=VS.85).aspx) instructions.                                                                                           |
| D3DVS20\_MIN\_STATICFLOWCONTROLDEPTH  | 1              | The minimum depth of nesting of the [loop - vs](https://msdn.microsoft.com/en-us/library/Bb174716(v=VS.85).aspx)/[rep - vs](https://msdn.microsoft.com/en-us/library/Bb147331(v=VS.85).aspx) and [call - vs](https://msdn.microsoft.com/en-us/library/Bb172389(v=VS.85).aspx)/[callnz bool - vs](https://msdn.microsoft.com/en-us/library/Bb172385(v=VS.85).aspx) instructions.                                                                                           |



 

## Constant Information



|                          |            |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> <dt>

[**D3DVSHADERCAPS2\_0**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dvshadercaps2_0)
</dt> </dl>

 

 



