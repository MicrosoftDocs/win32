---
title: vs_3_0
description: Learn about vs_3_0, a programmable vertex shader, which is made up of a set of instructions that operate on vertex data.
ms.assetid: 0f40f946-3525-4203-bfe2-1cd941d8e2ec
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# vs\_3\_0

A programmable vertex shader is made up of a set of instructions that operate on vertex data. Registers transfer data in and out of the ALU. Additional control can be applied to modify the instruction, the results, or what data gets written out.

Vertex shader version vs\_3\_0 extends the feature set supported by vs\_2\_x. Each of the features in vs\_2\_X that requires a cap to be set, is available in vs\_3\_0 without requiring the cap.

-   [Instructions - vs\_3\_0](dx9-graphics-reference-asm-vs-instructions-vs-3-0.md) contains a list of the available instructions.
-   [Registers - vs\_3\_0](dx9-graphics-reference-asm-vs-registers-vs-3-0.md) lists the different types of registers used by the vertex shader ALU.
-   [Vertex Shader Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers.md) are used to modify the way an instruction works.
-   [Vertex Shader Source Register Modifiers](dx9-graphics-reference-asm-vs-registers-modifiers-source.md) alter the source register data before the instruction runs.
-   [Source Register Swizzling](dx9-graphics-reference-asm-vs-registers-modifiers-source-swizzling.md) gives additional control over which register components are read, copied, or written.
-   [Destination Register Masking](dx9-graphics-reference-asm-vs-registers-modifiers-masking.md) determines what components of the destination register get written.

## New Features

New features of vertex shader version vs\_3\_0 are listed in the following sections.

### Indexing Registers

In the earlier shader models, only the constant register bank could be indexed. In this model, the following register banks can be indexed, using the loop counter register (aL):

-   Input register (v\#)
-   Output register (o\#)

### Vertex Textures

This shader model supports texture lookup in the vertex shader using texldl. The vertex engine has four texture sampler stages (distinct from the displacement map sampler and the texture samplers in the pixel engine) that can be used to sample textures set at those stages. See [Vertex Textures in vs\_3\_0 (DirectX HLSL)](/windows/desktop/direct3d9/vertex-textures-in-vs-3-0).

### Vertex Stream Frequency

This feature allows a subset of the input registers to be initialized at a rate different from once per vertex. See [Drawing Non-Indexed Geometry](/windows/desktop/direct3d9/efficiently-drawing-multiple-instances-of-geometry).

### Shader Output

Similar to vs\_2\_0, the output of the shader can vary with static flow control. Be careful with dynamic branching as this can cause shader outputs to vary per vertex. This will produce unpredictable results on different hardware.

### Dynamic flow control

All dynamic flow control instructions are supported. The maximum nesting depth value allowed is 24. (See [Flow Control Nesting Limits](dx9-graphics-reference-asm-vs-instructions-flow-control.md) for details.)

### Temporary Registers

A total of 32 temporary registers (r\#) is supported.

### Static Flow Control

The maximum nesting depth for [loop - vs](loop---vs.md)/[rep - vs](rep---vs.md) is 4. The maximum nesting depth for [call - vs](call---vs.md)/[callnz bool - vs](callnz-bool---vs.md)/[callnz pred - vs](callnz-pred---vs.md) is 4. For [if bool - vs](if-bool---vs.md), the maximum nesting depth value allowed is 24. (See [Flow Control Nesting Limits](dx9-graphics-reference-asm-vs-instructions-flow-control.md) for details.)

### Predication

Instruction predication is supported. Use [setp\_comp - vs](setp-comp---vs.md) to set the predicate register.

### Instruction Count

Each vertex shader is allowed anywhere from 512 up to the number of slots in MaxVertexShader30InstructionSlots in [**D3DCAPS9**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcaps9). The number of instructions run can be much higher because of the loop/rep support; however, this is capped by MaxVShaderInstructionsExecuted in D3DCAPS9 which should be at least 0xFFFF.

### Device Caps

If Vertex Shader 3\_0 is supported, the following caps are supported in hardware (at a minimum):



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Cap</th>
<th>Capability</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Shader caps</td>
<td><ul>
<li>DynamicFlowControlDepth is 24</li>
<li>NumTemps is 32</li>
<li>StaticFlowControlDepth is 4</li>
<li>Predication is supported.</li>
</ul></td>
</tr>
<tr class="even">
<td>GuardBandLeft, GuardBandTop, GuardBandRight, GuardBandBottom</td>
<td>8K</td>
</tr>
<tr class="odd">
<td>VertexShaderVersion</td>
<td>3_0</td>
</tr>
<tr class="even">
<td>MaxVertexShaderConst</td>
<td>256</td>
</tr>
<tr class="odd">
<td>MaxVertexShader30InstructionSlots</td>
<td>512</td>
</tr>
<tr class="even">
<td>Fog support</td>
<td>D3DPRASTERCAPS_FOGVERTEX</td>
</tr>
<tr class="odd">
<td>VertexTextureFilterCaps</td>
<td><ul>
<li><a href="/windows/desktop/direct3d9/d3dptfiltercaps">D3DPTFILTERCAPS_MINFPOINT</a></li>
<li><a href="/windows/desktop/direct3d9/d3dptfiltercaps">D3DPTFILTERCAPS_MAGFPOINT</a></li>
</ul></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/direct3d9/d3ddevcaps2">D3DDEVCAPS2_VERTEXELEMENTSCANSHARESTREAMOFFSET</a></td>
<td>Vertex elements in a vertex declaration can share the same stream offset.</td>
</tr>
<tr class="odd">
<td>Vertex formats</td>
<td><ul>
<li>D3DDECLTYPE_UBYTE4</li>
<li>D3DDECLTYPE_UBYTE4N</li>
<li>D3DDECLTYPE_SHORT2N</li>
<li>D3DDECLTYPE_SHORT4N</li>
<li>D3DDECLTYPE_FLOAT16_2</li>
<li>D3DDECLTYPE_FLOAT16_4</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Vertex Shaders](dx9-graphics-reference-asm-vs.md)
</dt> </dl>

 

 