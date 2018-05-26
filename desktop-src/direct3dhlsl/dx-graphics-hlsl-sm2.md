---
title: Shader Model 2
description: Shader Model 2 added additional capabilities to shader model 1.
ms.assetid: 53c367d2-5b6a-4afa-894a-8ab9927169d5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shader Model 2

Shader Model 2 added additional capabilities to [shader model 1](dx-graphics-hlsl-sm1.md).



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
<li>Assembly instructions (see [Instructions - vs_2_0](dx9-graphics-reference-asm-vs-instructions-vs-2-0.md), [Instructions - vs_2_x](dx9-graphics-reference-asm-vs-instructions-vs-2-x.md), [ps_2_0 Instructions](dx9-graphics-reference-asm-ps-instructions-ps-2-0.md), [ps_2_x Instructions](dx9-graphics-reference-asm-ps-instructions-ps-2-x.md))</li>
</ul></td>
</tr>
<tr class="odd">
<td>Register Set</td>
<td><ul>
<li>Pixel shader registers (see [ps_2_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-2-0.md), [ps_2_x Registers](dx9-graphics-reference-asm-ps-registers-ps-2-x.md))</li>
<li>Vertex shader registers (see [Registers - vs_2_0](dx9-graphics-reference-asm-vs-registers-vs-2-0.md), [Registers - vs_2_x](dx9-graphics-reference-asm-vs-registers-vs-2-x.md))</li>
</ul></td>
</tr>
<tr class="even">
<td>Pixel Shader Max</td>
<td><ul>
<li>ps_2_0 - 32 texture + 64 arithmetic</li>
<li>ps_2_x - 96 minimum, and up to the number of slots in D3DCAPS9.D3DPSHADERCAPS2_0.NumInstructionSlots. See D3DPSHADERCAPS2_0</li>
</ul></td>
</tr>
<tr class="odd">
<td>Vertex Shader Max</td>
<td>256 instructions</td>
</tr>
<tr class="even">
<td>Shader Profiles</td>
<td>ps_2_0, ps_2_x, vs_2_0, vs_2_x</td>
</tr>
</tbody>
</table>



 

For more details on shader model 2, see:

-   [Pixel Shader 2.0](dx9-graphics-reference-asm-ps-2-0.md), [Pixel Shader 2.x](dx9-graphics-reference-asm-ps-2-x.md)
-   [Vertex Shader 2.0](dx9-graphics-reference-asm-vs-2-0.md), [Vertex Shader 2.x](dx9-graphics-reference-asm-vs-2-x.md)

## Related topics

<dl> <dt>

[Shader Models vs Shader Profiles](dx-graphics-hlsl-models.md)
</dt> </dl>

 

 




