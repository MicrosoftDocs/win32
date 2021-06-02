---
title: Registers - hs_5_0
description: A hull shader consists of three distinct phases control point phase, fork phase, and join phase. Each phase has its own sets of input and output registers.
ms.assetid: 82F689EF-D3F4-40B5-9A2C-1F97F4CE6501
ms.topic: article
ms.date: 05/31/2018
---

# Registers - hs\_5\_0

A hull shader consists of three distinct phases: control point phase, fork phase, and join phase. Each phase has its own sets of input and output registers.

## Control Point Phase

hs\_control\_point\_phase is a shader program with the following register model.

### Input Registers



| Register Type                                     | Count                 | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|---------------------------------------------------|-----------------------|-----|-----------|------------------|----------|--------------|
| 32-bit Temp (r\#)                                 | 4096(r\#+x\#\[n\])    | R/W | 4         | No               | None     | Yes          |
| 32-bit indexable Temp Array (x\#\[n\])            | 4096(r\#+x\#\[n\])    | R/W | 4         | Yes              | None     | Yes          |
| 32-bit Input (v\[vertex\]\[element\])             | 32(element)\*32(vert) | R   | 4         | Yes              | None     | Yes          |
| 32-bit UINT Input vOutputControlPointID(23.7)     | 1                     | R   | 1         | No               | None     | Yes          |
| 32-bit UINT Input PrimitiveID (vPrim)             | 1                     | R   | 1         | No               | N/A      | Yes          |
| Element in an input resource (t\#)                | 128                   | R   | 128       | Yes              | None     | Yes          |
| Sampler (s\#)                                     | 16                    | R   | 1         | Yes              | None     | Yes          |
| ConstantBuffer reference (cb\#\[index\])          | 15                    | R   | 4         | Yes              | None     | Yes          |
| Immediate ConstantBuffer reference (icb\[index\]) | 1                     | R   | 4         | Yes (contents)   | None     | Yes          |



 

### Output Registers



| Register Type                           | Count | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|-----------------------------------------|-------|-----|-----------|------------------|----------|--------------|
| 32-bit output Vertex Data Element (o\#) | 32    | W   | 4         | Yes              | None     | Yes          |



 

Each hull shader control point phase output register is up to a 4-vector, of which up to 32 registers can be declared. There are also from 1 to 32 output control points declared, which scales amount of storage required. Let us refer to the maximum allowable aggregate number of scalars across all hull shader control point phase output as \#cp\_output\_max.

\#cp\_output\_max = 3968 scalars.

This limit is based on a design point for certain hardware of 4096\*32-bit storage here. The amount for control point output is 3968=4096-128, which is 32(control points)\*4(components)\*32(elements) - 4(components)\*32(elements). The subtraction reserves 128 scalars (one control point) worth of space dedicated to the hull shader phase 2 and 3. The choice of reserving 128 scalars for patch constants -- rather than allowing the amount to be simply whatever of the 4096 scalars of storage is unused by output control points -- accommodates the limits of another particular hardware design. The control point phase can declare 32 output control points, but they just can’t be fully 32 elements with 4 components each, because the total storage would be too high.

## Fork Phase

The following registers are visible in the hs\_fork\_phase model.

The input resources (t\#), samplers (s\#), constant buffers (cb\#) and immediate constant buffer (icb) below are all shared state with all other hull shader phases. That is, from the API/DDI point of view, the hull shader has a single set of input resource state for all phases. This goes with the fact that from the API/DDI point of view, the hull shader is a single atomic shader; the phases within it are implementation details.

### Input Registers



| Register Type                                                                         | Count              | R/W | Dimension                           | Indexable by r\# | Defaults | Requires DCL |
|---------------------------------------------------------------------------------------|--------------------|-----|-------------------------------------|------------------|----------|--------------|
| 32-bit Temp (r\#)                                                                     | 4096(r\#+x\#\[n\]) | R/W | 4                                   | No               | None     | Yes          |
| 32-bit indexable Temp Array (x\#\[n\])                                                | 4096(r\#+x\#\[n\]) | R/W | 4                                   | Yes              | None     | Yes          |
| 32-bit Input Control Points (vicp\[vertex\]\[element\]) (pre-Control Point Phase)     | 32 See note below  | R   | 4(component)\*32(element)\*32(vert) | Yes              | None     | Yes          |
| 32-bit Output Control Points (vocp\[vertex\]\[element\]\]) (post-Control Point Phase) | 32 See note below  | R   | 4(component)\*32(element)\*32(vert) | Yes              | None     | Yes          |
| 32-bit UINT Input PrimitiveID (vPrim)                                                 | 1                  | R   | 1                                   | No               | N/A      | Yes          |
| 32-bit UINT Input ForkInstanceID(23.8) (vForkInstanceID)                              | 1                  | R   | 1                                   | No               | N/A      | Yes          |
| Element in an input resource (t\#)                                                    | 128                | R   | 128                                 | Yes              | None     | Yes          |
| Sampler (s\#)                                                                         | 16                 | R   | 1                                   | Yes              | None     | Yes          |
| ConstantBuffer reference (cb\#\[index\])                                              | 15                 | R   | 4                                   | Yes              | None     | Yes          |
| Immediate ConstantBuffer reference (icb\[index\])                                     | 1                  | R   | 4                                   | Yes (contents)   | None     | Yes          |



 

> [!Note]
> The hull shader fork phase’s input control point register (vicp) declarations must be any subset, along the \[element\] axis, of the hull shader control point input (pre-control point phase). Similarly the declarations for inputting the output control points (vocp) must be any subset, along the \[element\] axis, of the hull shader output control points (post-control point phase).
> 
> Along the \[vertex\] axis, the number of control points to be read for each of the vicp and vocp must similarly be a subset of the hull shader input control point count and hull shader output control point count, respectively. For example, if the vertex axis of the vocp registers are declared with n vertices, that makes the control point phase’s output control points \[0..n-1\] available as read only input to the fork phase.

### Output Registers



| Register                                        | Count               | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|-------------------------------------------------|---------------------|-----|-----------|------------------|----------|--------------|
| 32-bit output Patch Constant Data Element (o\#) | 32 See note 1 below | W   | 4         | Yes              | None     | Yes          |



 

> [!Note]  
> The hull shader fork and join phase outputs are a shared set of 4 4-vector registers. The outputs of each fork or join phase program cannot overlap with each other. System-interpreted values such as TessFactors come out of this space.

## Join Phase

The following registers are visible in the hs\_join\_phase model. There are three sets of input registers: control point phase input control points (vicp), vocp control point phase output control points (vocp), and patch constants (vcp). vpc are the aggregate output of all the hull shader fork phase programs. The hull shader join phase output o\# registers are in the same register space as the hulll shader fork phase outputs.

The input resources (t\#), samplers (s\#), constant buffers (cb\#) and immediate constant buffer (icb) below are all shared state with all other hull shader phases. That is, from the API/DDI point of view, the hull shader has a single set of input resource state for all phases. This goes with the fact that from the API/DDI point of view, the hull shader is a single atomic shader; the phases within it are implementation details.

### Input Registers



| Register Type                                                                       | Count               | R/W | Dimension                           | Indexable by r\# | Defaults | Requires DCL |
|-------------------------------------------------------------------------------------|---------------------|-----|-------------------------------------|------------------|----------|--------------|
| 32-bit Temp (r\#)                                                                   | 4096(r\#+x\#\[n\])  | R/W | 4                                   | No               | None     | Yes          |
| 32-bit indexable Temp Array (x\#\[n\])                                              | 4096(r\#+x\#\[n\])  | R/W | 4                                   | Yes              | None     | Yes          |
| 32-bit Input Control Points (vicp\[vertex\]\[element\]) (pre-Control Point Phase)   | 32 See Note 1 below | R   | 4(component)\*32(element)\*32(vert) | Yes              | None     | Yes          |
| 32-bit Output Control Points (vocp\[vertex\]\[element\]) (post-Control Point Phase) | 32 See Note 1 below | R   | 4(component)\*32(element)\*32(vert) | Yes              | None     | Yes          |
| 32-bit Input (vpc\[element\]) (Patch Constant Data)                                 | 32 See Note 2 below | R   | 4                                   | Yes              | None     | Yes          |
| 32-bit UINT Input PrimitiveID (vPrim)                                               | 1                   | R   | 1                                   | No               | N/A      | Yes          |
| 32-bit UINT Input JoinInstanceID (vJoinInstanceID)                                  | 1                   | R   | 1                                   | No               | N/A      | Yes          |
| Element in an input resource (t\#)                                                  | 128                 | R   | 128                                 | Yes              | None     | Yes          |
| Sampler (s\#)                                                                       | 16                  | R   | 1                                   | Yes              | None     | Yes          |
| ConstantBuffer reference (cb\#\[index\])                                            | 15                  | R   | 4                                   | Yes              | None     | Yes          |
| Immediate ConstantBuffer reference (icb\[index\])                                   | 1                   | R   | 4                                   | Yes (contents)   | None     | Yes          |



 

**Note 1:** The hull shader join phase’s input control point register (vicp) declarations must be any subset, along the \[element\] axis, of the hull shader control point input (pre-control point phase). Similarly the declarations for inputting the output control points (vocp) must be any subset, along the \[element\] axis, of the hull shader output control points (post-control point phase).

Along the \[vertex\] axis, the number of control points to be read for each of the vicp and vocp must similarly be a subset of the hull shader input control point count and hull shader output control point count, respectively. For example, if the vertex axis of the vocp registers are declared with n vertices, that makes the control point phase’s output control points \[0..n-1\] available as read only input to the join phase.

**Note 2:** In addition to control point input, the hull shader join phase also sees as input the patch constant data computed by the hull shader fork phase program(s). This shows up at the hull shader fork phase as the vpc\# registers. The hull shader join phase’s input vpc\# registers share the same register space as the hull shader fork phase output o\# registers. The declarations of the o\# registers must not overlap with any hull shader fork phase program o\# output declaration; the hull shader join phase is adding to the aggregate patch constant data output for the hull shader.

### Output Registers



| Register Type                                   | Count             | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|-------------------------------------------------|-------------------|-----|-----------|------------------|----------|--------------|
| 32-bit output Patch Constant Data Element (o\#) | 32 See note below | W   | 4         | Yes              | None     | Yes          |



 

> [!Note]  
> The hull shader fork and join phase outputs are a shared set of 4 4-vector registers. The outputs of each fork or join phase program cannot overlap with each other. System-interpreted values such as TessFactors come out of this space.

## Related topics

<dl> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




