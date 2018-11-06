---
title: Registers - ds_5_0
description: The following input and output registers are implemented in the domain shader version 5\_0.
ms.assetid: 8AE00EC6-0BDC-4F63-B95C-FF434B98D7CE
ms.topic: article
ms.date: 05/31/2018
---

# Registers - ds\_5\_0

The following input and output registers are implemented in the domain shader version 5\_0.

## Input Registers



| Register Type                                              | Count                | R/W | Dimension                           | Indexable by r\# | Defaults | Requires DCL |
|------------------------------------------------------------|----------------------|-----|-------------------------------------|------------------|----------|--------------|
| 32-bit Temp (r\#)                                          | 4096(r\#+x\#\[n\])   | R/W | 4                                   | No               | None     | Yes          |
| 32-bit indexable Temp Array (x\#\[n\])                     | 4096(r\#+x\#\[n\])   | R/W | 4                                   | Yes              | None     | Yes          |
| 32-bit Input Control Points (vcp\[vertex\]\[element\])     | 32 See note 1 below. | R   | 4(component)\*32(element)\*32(vert) | Yes              | None     | Yes          |
| 32-bit Input Patch Constants (vpc\[vertex\])               | 32 See note 2 below. | R   | 4                                   | Yes              | None     | Yes          |
| 32-bit input location in domain (vDomain.xy, vDomain.xyz)) | 1                    | R   | 3                                   | No               | N/A      | Yes          |
| 32-bit UINT Input PrimitiveID (vPrim)                      | 1                    | R   | 1                                   | No               | N/A      | Yes          |
| Element in an input resource (t\#)                         | 128                  | R   | 128                                 | Yes              | None     | Yes          |
| Sampler (s\#)                                              | 16                   | R   | 1                                   | Yes              | None     | Yes          |
| iConstantBuffer reference (cb\#\[index\])                  | 15                   | R   | 4                                   | Yes              | None     | Yes          |
| iImmediate ConstantBuffer reference (icb\[index\])         | 1                    | R   | 4                                   | Yes(contents)    | None     | Yes          |



 

**Note 1:** The domain shader sees the hull shader outputs in 2 separate sets of registers. The vcp registers can see all of the hull shader’s output Control Points. The vpc registers can see all of the hull shader’s Patch Constant output data.

**Note 2:** Because code for hull shader Patch Constant Fork or Join Phases output TessFactors using names such as SV\_TessFactor, the domain shader must match those declarations on the equivalent vpc input if it wishes to see those values.

## Output Registers



| Register Type                           | Count | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|-----------------------------------------|-------|-----|-----------|------------------|----------|--------------|
| 32-bit output Vertex Data Element (o\#) | 32    | W   | 4         | Yes              | None     | Yes          |



 

## Related topics

<dl> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




