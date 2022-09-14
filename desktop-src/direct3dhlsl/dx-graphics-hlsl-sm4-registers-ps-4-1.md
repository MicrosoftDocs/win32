---
title: Registers - ps_4_1
description: This section contains reference information for the input and output registers implemented by pixel shader version 4\_1.
ms.assetid: d3f3e264-569e-43a6-a06b-a512d36a7b53
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registers - ps\_4\_1

This section contains reference information for the input and output registers implemented by pixel shader version 4\_1.

## Input Registers



| Register      | Name | Count              | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|---------------|------|--------------------|-----|-----------|------------------|----------|--------------|
| r\#           |      | 4096(r\#+x\#\[n\]) | R/W | 4         | No               | None     | Yes          |
| x\#\[n\]      |      | 4096(r\#+x\#\[n\]) | R/W | 4         | Yes              | None     | Yes          |
| v\#           |      | 32                 | R   | 4         | Yes              | None     | Yes          |
| t\#           |      | 128                | R   | 1         | No               | None     | Yes          |
| s\#           |      | 16                 | R   | 1         | No               | None     | Yes          |
| cb\#\[index\] |      | 15                 | R   | 4         | Yes(Contents)    | None     | Yes          |
| icb\[index\]  |      | 1                  | R   | 4         | Yes(Contents)    | None     | Yes          |



 

## Output Registers



| Register | Name             | Count | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|----------|------------------|-------|-----|-----------|------------------|----------|--------------|
| NULL     | Discard Result   | N/A   | W   | N/A       | N/A              | N/A      | No           |
| o\#      | Output Register  | 8     | W   | N/A       | N/A              | 4        | No           |
| oDepth   | Output Depth     | 1     | W   | N/A       | N/A              | 1        | N/A          |
| oMask    | Output MSAA Mask | 1     | W   | N/A       | N/A              | 1        | N/A          |



 

## Related topics

<dl> <dt>

[Shader Model 4](dx-graphics-hlsl-sm4.md)
</dt> </dl>

 

 




