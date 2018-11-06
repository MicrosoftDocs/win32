---
title: Registers - vs_5_0
description: The following input and output registers are implemented in the vertex shader version 5\_0.
ms.assetid: 475753C7-C055-4DB7-9DC3-6C734413A92B
ms.topic: article
ms.date: 05/31/2018
---

# Registers - vs\_5\_0

The following input and output registers are implemented in the vertex shader version 5\_0.

## Input Registers



| Register Type                                      | Count              | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|----------------------------------------------------|--------------------|-----|-----------|------------------|----------|--------------|
| 32-bit Temp (r\#)                                  | 4096(r\#+x\#\[n\]) | R/W | 4         | No               | None     | Yes          |
| 32-bit indexable Temp Array (x\#\[n\])             | 4096(r\#+x\#\[n\]) | R/W | 4         | Yes              | None     | Yes          |
| 32-bit input (v\#)                                 | 32                 | R   | 4         | Yes              | None     | Yes          |
| Element in an input resource (t\#)                 | 128                | R   | 1         | No               | None     | Yes          |
| Sampler (s\#)                                      | 16                 | R   | 1         | No               | None     | Yes          |
| ConstantBuffer reference (cb\#\[index\])           | 15                 | R   | 4         | Yes(contents)    | None     | Yes          |
| iImmediate ConstantBuffer reference (icb\[index\]) | 1                  | R   | 4         | Yes(contents)    | None     | Yes          |



 

## Output Registers



| Register Type                                                      | Count | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|--------------------------------------------------------------------|-------|-----|-----------|------------------|----------|--------------|
| NULL (discard result, useful for operations with multiple results) | N/A   | W   | N/A       | N/A              | N/A      | No           |
| 32-bit output Vertex Data Element (o\#)                            | 32    | W   | 4         | N/A              | N/A      | Yes          |



 

## Related topics

<dl> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




