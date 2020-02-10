---
title: Shader Model 3
description: Shader Model 3 added additional capabilities to shader model 2.
ms.assetid: bd09f86e-946f-4281-bc48-1db5cd32b2ae
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Shader Model 3 (HLSL reference)

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
<li><a href="dx-graphics-hlsl-intrinsic-functions.md"><strong>HLSL functions</strong></a></li>
<li>Assembly instructions (see <a href="dx9-graphics-reference-asm-ps-instructions-ps-3-0.md">ps_3_0 Instructions</a>, <a href="dx9-graphics-reference-asm-vs-instructions-vs-3-0.md">Instructions - vs_3_0</a>)</li>
</ul></td>
</tr>
<tr class="odd">
<td>Register Set</td>
<td><ul>
<li>Pixel shader registers (see <a href="dx9-graphics-reference-asm-ps-registers-ps-3-0.md">ps_3_0 Registers</a>)</li>
<li>Vertex shader registers (see <a href="dx9-graphics-reference-asm-vs-registers-vs-3-0.md">Registers - vs_3_0</a>)</li>
</ul></td>
</tr>
<tr class="even">
<td>Pixel Shader Max</td>
<td>512 minimum, and up to the number of slots in D3DCAPS9.MaxPixelShader30InstructionSlots (see <a href="https://docs.microsoft.com/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dpshadercaps2_0"><strong>D3DPSHADERCAPS2_0</strong></a>).</td>
</tr>
<tr class="odd">
<td>Vertex Shader Max</td>
<td>512 minimum, and up to the number of slots in D3DCAPS9.MaxVertexShader30InstructionSlots (see <a href="https://docs.microsoft.com/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcaps9"><strong>D3DCAPS9</strong></a>).</td>
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

 

 




