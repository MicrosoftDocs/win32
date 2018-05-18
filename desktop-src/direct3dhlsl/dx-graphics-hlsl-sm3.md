---
title: Shader Model 3
description: Shader Model 3 added additional capabilities to shader model 2.
ms.assetid: 'bd09f86e-946f-4281-bc48-1db5cd32b2ae'
---

# Shader Model 3

Shader Model 3 added additional capabilities to [shader model 2](dx-graphics-hlsl-sm2.md).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Feature</td>
<td>Capability</td>
</tr>
<tr class="even">
<td>Instruction Set</td>
<td><ul>
<li>[<strong>HLSL functions</strong>](dx-graphics-hlsl-intrinsic-functions.md)</li>
<li>Assembly instructions (see [ps_3_0 Instructions](dx9-graphics-reference-asm-ps-instructions-ps-3-0.md), [Instructions - vs_3_0](dx9-graphics-reference-asm-vs-instructions-vs-3-0.md))</li>
</ul></td>
</tr>
<tr class="odd">
<td>Register Set</td>
<td><ul>
<li>Pixel shader registers (see [ps_3_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-3-0.md))</li>
<li>Vertex shader registers (see [Registers - vs_3_0](dx9-graphics-reference-asm-vs-registers-vs-3-0.md))</li>
</ul></td>
</tr>
<tr class="even">
<td>Pixel Shader Max</td>
<td>512 minimum, and up to the number of slots in D3DCAPS9.MaxPixelShader30InstructionSlots (see [<strong>D3DPSHADERCAPS2_0</strong>](https://msdn.microsoft.com/library/windows/desktop/bb172591)).</td>
</tr>
<tr class="odd">
<td>Vertex Shader Max</td>
<td>512 minimum, and up to the number of slots in D3DCAPS9.MaxVertexShader30InstructionSlots (see [<strong>D3DCAPS9</strong>](https://msdn.microsoft.com/library/windows/desktop/bb172513)).</td>
</tr>
<tr class="even">
<td>Shader Profiles</td>
<td>ps_3_0, vs_3_0</td>
</tr>
</tbody>
</table>



 

For more details on model 3 shaders, see:

-   [Pixel Shader 3.0](dx9-graphics-reference-asm-ps-3-0.md)
-   [Vertex Shader 3.0](dx9-graphics-reference-asm-vs-3-0.md)

## Related topics

<dl> <dt>

[Shader Models vs Shader Profiles](dx-graphics-hlsl-models.md)
</dt> </dl>

 

 




