---
title: Registers - cs_5_0
description: The following input and output registers are implemented in the compute shader version 5\_0.
ms.assetid: A602BA9F-0934-472F-BB07-5E7A97763CAB
ms.topic: article
ms.date: 05/31/2018
---

# Registers - cs\_5\_0

The following input and output registers are implemented in the compute shader version 5\_0.

## Input Registers



| Register Type                                        | Count                                                  | R/W | Dimension                        | Indexable by r\# | Defaults | Requires DCL |
|------------------------------------------------------|--------------------------------------------------------|-----|----------------------------------|------------------|----------|--------------|
| 32-bit Temp (r\#)                                    | 4096(r\#+x\#\[n\])                                     | R/W | 4                                | No               | None     | Yes          |
| 32-bit Indexable Temp Array (x\#\[n\])               | 4096(r\#+x\#\[n\])                                     | R/W | 4                                | Yes              | None     | Yes          |
| 32-bit Thread Group Shared Memory (g\#\[n\])         | 8192 (sum of all shared memory decls for thread group) | R/W | 1 (can be declared various ways) | Yes              | None     | Yes          |
| Element in an input resource (t\#)                   | 128                                                    | R   | 1                                | No               | None     | Yes          |
| Sampler (s\#)                                        | 16                                                     | R   | 1                                | No               | None     | Yes          |
| ConstantBuffer reference (cb\#\[index\])             | 15                                                     | R   | 4                                | Yes (contents)   | None     | Yes          |
| Immediate ConstantBuffer reference (icb\[index\])    | 1                                                      | R   | 4                                | Yes(contents)    | None     | Yes          |
| ThreadID (vThreadID.xyz)                             | 1                                                      | R   | 3                                | No               | N/A      | Yes          |
| ThreadGroupID (vThreadGroupID.xyz)                   | 1                                                      | R   | 3                                | No               | N/A      | Yes          |
| ThreadIDInGroup (vThreadIDInGroup.xyz)               | 1                                                      | R   | 3                                | No               | N/A      | Yes          |
| ThreadIDInGroupFlattened (vThreadIDInGroupFlattened) | 1                                                      | R   | 1                                | No               | N/A      | Yes          |



 

## Output Registers



| Register Type                                               | Count | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|-------------------------------------------------------------|-------|-----|-----------|------------------|----------|--------------|
| NULL (discard result, useful for ops with multiple results) | N/A   | W   | N/A       | N/A              | N/A      | No           |
| Unordered Access View (u\#)                                 | 8     | R/W | 1         | No               | No       | Yes          |



 

## Related topics

<dl> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




