---
title: Registers - ps_5_0
description: The following input and output registers are implemented in the pixel shader version 5\_0.
ms.assetid: F16E5CB8-E1DB-48CD-8C20-DBF1DF971110
ms.topic: article
ms.date: 05/31/2018
---

# Registers - ps\_5\_0

The following input and output registers are implemented in the pixel shader version 5\_0.

## Input Registers



| Register Type                                     | Count              | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|---------------------------------------------------|--------------------|-----|-----------|------------------|----------|--------------|
| 32-bit Temp (r\#)                                 | 4096(r\#+x\#\[n\]) | R/W | 4         | No               | None     | Yes          |
| 32-bit Indexable Temp Array (x\#\[n\])            | 4096(r\#+x\#\[n\]) | R/W | 4         | Yes              | None     | Yes          |
| 32-bit Input Attribute (v\#)                      | 32                 | R   | 4         | Yes              | None     | Yes          |
| Element in an input resource (t\#)                | 128                | R   | 1         | No               | None     | Yes          |
| Sampler (s\#)                                     | 16                 | R   | 1         | No               | None     | Yes          |
| ConstantBuffer reference (cb\#\[index\])          | 15                 | R   | 4         | Yes(contents)    | None     | Yes          |
| Immediate ConstantBuffer reference (icb\[index\]) | 1                  | R   | 4         | Yes(contents)    | None     | Yes          |



 

## Output Registers



| Register Type                                                      | Count                   | R/W | Dimension                                | Indexable by r\# | Defaults | Requires DCL |
|--------------------------------------------------------------------|-------------------------|-----|------------------------------------------|------------------|----------|--------------|
| NULL (discard result, useful for operations with multiple results) | N/A                     | W   | N/A                                      | N/A              | N/A      | No           |
| 32-bit output Element (o\#)                                        | 8                       | W   | 4                                        | N/A              | N/A      | No           |
| Unordered Access View (u\#)                                        | 8 - \# of rendertargets | R/W | D3D11\_PS\_CS\_UAV\_REGISTER\_COMPONENTS | No               | No       | Yes          |
| 32-bit \[0.0f..1.0f\] float output depth (oDepth)                  | 1                       | W   | 1                                        | N/A              | N/A      | Yes          |
| 32-bit UINT output sample mask (oMask)                             | 1                       | W   | 1                                        | N/A              | N/A      | Yes          |



 

## Related topics

<dl> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




