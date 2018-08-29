---
title: Shader Model 2
description: Shader Model 2 added additional capabilities to shader model 1.
ms.assetid: 53c367d2-5b6a-4afa-894a-8ab9927169d5
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
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
<li><a href="dx-graphics-hlsl-intrinsic-functions"><strong>HLSL functions</strong></a></li>
<li>Assembly instructions (see <a href="dx9-graphics-reference-asm-vs-instructions-vs-2-0">Instructions - vs_2_0</a>, <a href="dx9-graphics-reference-asm-vs-instructions-vs-2-x">Instructions - vs_2_x</a>, <a href="dx9-graphics-reference-asm-ps-instructions-ps-2-0">ps_2_0 Instructions</a>, <a href="dx9-graphics-reference-asm-ps-instructions-ps-2-x">ps_2_x Instructions</a>)</li>
</ul></td>
</tr>
<tr class="odd">
<td>Register Set</td>
<td><ul>
<li>Pixel shader registers (see <a href="dx9-graphics-reference-asm-ps-registers-ps-2-0">ps_2_0 Registers</a>, <a href="dx9-graphics-reference-asm-ps-registers-ps-2-x">ps_2_x Registers</a>)</li>
<li>Vertex shader registers (see <a href="dx9-graphics-reference-asm-vs-registers-vs-2-0">Registers - vs_2_0</a>, <a href="dx9-graphics-reference-asm-vs-registers-vs-2-x">Registers - vs_2_x</a>)</li>
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

 

 




