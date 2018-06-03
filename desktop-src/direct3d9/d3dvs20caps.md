---
Description: Vertex shader caps constants. These constants are used by the VS20Caps member of D3DCAPS9.
ms.assetid: c1321957-4ba5-45d0-984a-4f4267221c59
title: D3DVS20CAPS
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DVS20CAPS

Vertex shader caps constants. These constants are used by the VS20Caps member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-_d3dcaps9).



| \#define                              | Value          | Description                                                                                                                                                                                                                                                                                                 |
|---------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DVS20CAPS\_PREDICATION              | (1 &lt;&lt; 0) | Instruction predication is supported. See [setp\_comp - vs](https://msdn.microsoft.com/windows/desktop/bfead3f8-f7fe-4fc1-939f-8e5fbc3e0adf).                                                                                                                                                                                                                   |
| D3DVS20\_MAX\_DYNAMICFLOWCONTROLDEPTH | 24             | The maximum level of nesting of dynamic flow control instructions ([break - vs](https://msdn.microsoft.com/windows/desktop/d46a5ecd-8142-4134-b4c8-121a644a85c2), [break\_comp - vs](https://msdn.microsoft.com/windows/desktop/01745e03-874a-4594-b6ab-12db22d0cb4a), [breakp - vs](https://msdn.microsoft.com/windows/desktop/940252a0-6f6a-45d8-9d2f-315cc97686ca), [if\_comp - vs](https://msdn.microsoft.com/windows/desktop/a3fe93c6-be26-4216-a601-3be52a74be06), if\_comp - vs, [if pred - vs](https://msdn.microsoft.com/windows/desktop/03f60ca3-cda0-4653-8582-74d1a75e0aee)). |
| D3DVS20\_MIN\_DYNAMICFLOWCONTROLDEPTH | 0              | The minimum level of nesting of dynamic flow control instructions ([break - vs](https://msdn.microsoft.com/windows/desktop/d46a5ecd-8142-4134-b4c8-121a644a85c2), [break\_comp - vs](https://msdn.microsoft.com/windows/desktop/01745e03-874a-4594-b6ab-12db22d0cb4a), [breakp - vs](https://msdn.microsoft.com/windows/desktop/940252a0-6f6a-45d8-9d2f-315cc97686ca), [if\_comp - vs](https://msdn.microsoft.com/windows/desktop/a3fe93c6-be26-4216-a601-3be52a74be06), if\_comp - vs, [if pred - vs](https://msdn.microsoft.com/windows/desktop/03f60ca3-cda0-4653-8582-74d1a75e0aee)). |
| D3DVS20\_MAX\_NUMTEMPS                | 32             | The maximum number of temporary registers supported.                                                                                                                                                                                                                                                        |
| D3DVS20\_MIN\_NUMTEMPS                | 12             | The minimum number of temporary registers supported.                                                                                                                                                                                                                                                        |
| D3DVS20\_MAX\_STATICFLOWCONTROLDEPTH  | 4              | The maximum depth of nesting of the [loop - vs](https://msdn.microsoft.com/windows/desktop/1d587559-ef4b-40a5-bce5-49354d11ff91)/[rep - vs](https://msdn.microsoft.com/windows/desktop/0f795557-b5b0-45e6-8134-9558619f80fc) and [call - vs](https://msdn.microsoft.com/windows/desktop/3c1ec529-1ee4-40d9-8ce5-f8e7a61fde9c)/[callnz bool - vs](https://msdn.microsoft.com/windows/desktop/9be030b9-fa21-459f-bd6c-f34ad6f177fc) instructions.                                                                                           |
| D3DVS20\_MIN\_STATICFLOWCONTROLDEPTH  | 1              | The minimum depth of nesting of the [loop - vs](https://msdn.microsoft.com/windows/desktop/1d587559-ef4b-40a5-bce5-49354d11ff91)/[rep - vs](https://msdn.microsoft.com/windows/desktop/0f795557-b5b0-45e6-8134-9558619f80fc) and [call - vs](https://msdn.microsoft.com/windows/desktop/3c1ec529-1ee4-40d9-8ce5-f8e7a61fde9c)/[callnz bool - vs](https://msdn.microsoft.com/windows/desktop/9be030b9-fa21-459f-bd6c-f34ad6f177fc) instructions.                                                                                           |



 

## Constant Information



|                          |            |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> <dt>

[**D3DVSHADERCAPS2\_0**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-_d3dvshadercaps2_0)
</dt> </dl>

 

 



