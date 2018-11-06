---
title: Registers - gs_4_0
description: This section contains reference information for the input and output registers implemented by geometry shader version 4\_0.
ms.assetid: 1f3ebd71-19de-4e26-87f0-4fb5c8e2a343
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registers - gs\_4\_0

This section contains reference information for the input and output registers implemented by geometry shader version 4\_0.

## Input Registers



| Register                 | Name | Count              | R/W | Dimension        | Indexable by r\# | Defaults | Requires DCL |
|--------------------------|------|--------------------|-----|------------------|------------------|----------|--------------|
| r\#                      |      | 4096(r\#+x\#\[n\]) | R/W | 4                | No               | None     | Yes          |
| x\#\[n\]                 |      | 4096(r\#+x\#\[n\]) | R/W | 4                | Yes              | None     | Yes          |
| v\#\[vertex\]\[element\] |      | 32                 | R   | 4(comp)\*6(vert) | Yes              | None     | Yes          |
| vprim                    |      | 1                  | R   | 1                | No               | None     | Yes          |
| t\#                      |      | 128                | R   | 1                | No               | None     | Yes          |
| s\#                      |      | 16                 | R   | 1                | No               | None     | Yes          |
| cb\#\[index\]            |      | 15                 | R   | 4                | Yes(Contents)    | None     | Yes          |
| icb\[index\]             |      | 1                  | R   | 4                | Yes(Contents)    | None     | Yes          |



 

## Output Registers



| Register | Name            | Count | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|----------|-----------------|-------|-----|-----------|------------------|----------|--------------|
| NULL     | Discard Result  | N/A   | W   | N/A       | N/A              | N/A      | No           |
| o\#      | Output Register | 32    | W   | N/A       | N/A              | 4        | Yes          |



 

## Related topics

<dl> <dt>

[Shader Model 4](dx-graphics-hlsl-sm4.md)
</dt> </dl>

 

 




