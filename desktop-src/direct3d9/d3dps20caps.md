---
Description: Pixel shader capability flags.
ms.assetid: 41a8939f-eba5-47ca-8628-94b606b6f43d
title: D3DD3DPSHADERCAPS2\_0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DD3DPSHADERCAPS2\_0

Pixel shader capability flags.



|                                              |                |                                                                                                                                                                                                                   |
|----------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \#define                                     | Value          | Description                                                                                                                                                                                                       |
| D3DD3DPSHADERCAPS2\_0\_ARBITRARYSWIZZLE      | (1 &lt;&lt; 0) | Arbitrary swizzling is supported.                                                                                                                                                                                 |
| D3DD3DPSHADERCAPS2\_0\_GRADIENTINSTRUCTIONS  | (1 &lt;&lt; 1) | Gradient instructions are supported.                                                                                                                                                                              |
| D3DD3DPSHADERCAPS2\_0\_PREDICATION           | (1 &lt;&lt; 2) | Instruction predication is supported. See [setp\_comp - ps](https://msdn.microsoft.com/windows/desktop/a9acb685-f9aa-41f1-8ef1-6d104cb76a09).                                                                                                                         |
| D3DD3DPSHADERCAPS2\_0\_NODEPENDENTREADLIMIT  | (1 &lt;&lt; 3) | There is no limit on the number of dependent reads per instruction.                                                                                                                                               |
| D3DD3DPSHADERCAPS2\_0\_NOTEXINSTRUCTIONLIMIT | (1 &lt;&lt; 4) | There is no limit on the number of tex instructions.                                                                                                                                                              |
| D3DPS20\_MAX\_DYNAMICFLOWCONTROLDEPTH        | 24             | The maximum level of nesting of dynamic flow control instructions (break, breakc, ifc).                                                                                                                           |
| D3DPS20\_MIN\_DYNAMICFLOWCONTROLDEPTH        | 0              | The minimum level of nesting of dynamic flow control instructions (break, breakc, ifc).                                                                                                                           |
| D3DPS20\_MAX\_NUMTEMPS                       | 32             | The driver will support at most this many temporary register.                                                                                                                                                     |
| D3DPS20\_MIN\_NUMTEMPS                       | 12             | The driver will support at least this many temporary register.                                                                                                                                                    |
| D3DPS20\_MAX\_STATICFLOWCONTROLDEPTH         | 4              | The maximum depth of nesting of the [loop - vs](https://msdn.microsoft.com/windows/desktop/1d587559-ef4b-40a5-bce5-49354d11ff91)/[rep - vs](https://msdn.microsoft.com/windows/desktop/0f795557-b5b0-45e6-8134-9558619f80fc) and [call - vs](https://msdn.microsoft.com/windows/desktop/3c1ec529-1ee4-40d9-8ce5-f8e7a61fde9c)/[callnz bool - vs](https://msdn.microsoft.com/windows/desktop/9be030b9-fa21-459f-bd6c-f34ad6f177fc) instructions. |
| D3DPS20\_MIN\_STATICFLOWCONTROLDEPTH         | 1              | The minimum depth of nesting of the [loop - vs](https://msdn.microsoft.com/windows/desktop/1d587559-ef4b-40a5-bce5-49354d11ff91)/[rep - vs](https://msdn.microsoft.com/windows/desktop/0f795557-b5b0-45e6-8134-9558619f80fc) and [call - vs](https://msdn.microsoft.com/windows/desktop/3c1ec529-1ee4-40d9-8ce5-f8e7a61fde9c)/[callnz bool - vs](https://msdn.microsoft.com/windows/desktop/9be030b9-fa21-459f-bd6c-f34ad6f177fc) instructions. |
| D3DPS20\_MAX\_NUMINSTRUCTIONSLOTS            | 512            | The driver will support at most this many instructions.                                                                                                                                                           |
| D3DPS20\_MIN\_NUMINSTRUCTIONSLOTS            | 96             | The driver will support at least this many instructions.                                                                                                                                                          |



 

These constants are used by the D3DPSHADERCAPS2\_0 member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-_d3dcaps9).

## Constant Information



|                          |            |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> <dt>

[**D3DPSHADERCAPS2\_0**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-_d3dpshadercaps2_0)
</dt> </dl>

 

 



