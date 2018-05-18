---
Description: 'Vertex shader caps constants. These constants are used by the VS20Caps member of D3DCAPS9.'
ms.assetid: 'c1321957-4ba5-45d0-984a-4f4267221c59'
title: D3DVS20CAPS
---

# D3DVS20CAPS

Vertex shader caps constants. These constants are used by the VS20Caps member of [**D3DCAPS9**](d3dcaps9.md).



| \#define                              | Value          | Description                                                                                                                                                                                                                                                                                                 |
|---------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DVS20CAPS\_PREDICATION              | (1 &lt;&lt; 0) | Instruction predication is supported. See [setp\_comp - vs](direct3dhlsl.setp_comp___vs).                                                                                                                                                                                                                   |
| D3DVS20\_MAX\_DYNAMICFLOWCONTROLDEPTH | 24             | The maximum level of nesting of dynamic flow control instructions ([break - vs](direct3dhlsl.break___vs), [break\_comp - vs](direct3dhlsl.break_comp___vs), [breakp - vs](direct3dhlsl.breakp___vs), [if\_comp - vs](direct3dhlsl.if_comp___vs), if\_comp - vs, [if pred - vs](direct3dhlsl.if_pred___vs)). |
| D3DVS20\_MIN\_DYNAMICFLOWCONTROLDEPTH | 0              | The minimum level of nesting of dynamic flow control instructions ([break - vs](direct3dhlsl.break___vs), [break\_comp - vs](direct3dhlsl.break_comp___vs), [breakp - vs](direct3dhlsl.breakp___vs), [if\_comp - vs](direct3dhlsl.if_comp___vs), if\_comp - vs, [if pred - vs](direct3dhlsl.if_pred___vs)). |
| D3DVS20\_MAX\_NUMTEMPS                | 32             | The maximum number of temporary registers supported.                                                                                                                                                                                                                                                        |
| D3DVS20\_MIN\_NUMTEMPS                | 12             | The minimum number of temporary registers supported.                                                                                                                                                                                                                                                        |
| D3DVS20\_MAX\_STATICFLOWCONTROLDEPTH  | 4              | The maximum depth of nesting of the [loop - vs](direct3dhlsl.loop___vs)/[rep - vs](direct3dhlsl.rep___vs) and [call - vs](direct3dhlsl.call___vs)/[callnz bool - vs](direct3dhlsl.callnz_bool___vs) instructions.                                                                                           |
| D3DVS20\_MIN\_STATICFLOWCONTROLDEPTH  | 1              | The minimum depth of nesting of the [loop - vs](direct3dhlsl.loop___vs)/[rep - vs](direct3dhlsl.rep___vs) and [call - vs](direct3dhlsl.call___vs)/[callnz bool - vs](direct3dhlsl.callnz_bool___vs) instructions.                                                                                           |



 

## Constant Information



|                          |            |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> <dt>

[**D3DVSHADERCAPS2\_0**](d3dvshadercaps2-0.md)
</dt> </dl>

 

 



