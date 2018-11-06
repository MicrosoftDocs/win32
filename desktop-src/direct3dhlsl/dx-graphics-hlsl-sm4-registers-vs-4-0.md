---
title: Registers - vs_4_0
description: This section contains reference information for the input and output registers implemented by vertex shader version 4\_0.
ms.assetid: f471df6a-06f6-4783-ba8f-cf0a3b43727f
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registers - vs\_4\_0

This section contains reference information for the input and output registers implemented by vertex shader version 4\_0.

## Input Registers



| Register      | Name | Count              | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|---------------|------|--------------------|-----|-----------|------------------|----------|--------------|
| r\#           |      | 4096(r\#+x\#\[n\]) | R/W | 4         | No               | None     | Yes          |
| x\#\[n\]      |      | 4096(r\#+x\#\[n\]) | R/W | 4         | Yes              | None     | Yes          |
| v\#           |      | 16                 | R   | 4         | Yes              | None     | Yes          |
| t\#           |      | 128                | R   | 1         | No               | None     | Yes          |
| s\#           |      | 16                 | R   | 1         | No               | None     | Yes          |
| cb\#\[index\] |      | 15                 | R   | 4         | Yes(Contents)    | None     | Yes          |
| icb\[index\]  |      | 1                  | R   | 4         | Yes(Contents)    | None     | Yes          |



 

## Output Registers



| Register | Name            | Count | R/W | Dimension | Indexable by r\# | Defaults | Requires DCL |
|----------|-----------------|-------|-----|-----------|------------------|----------|--------------|
| NULL     | Discard Result  | N/A   | W   | N/A       | N/A              | N/A      | No           |
| o\#      | Output Register | 16    | W   | N/A       | N/A              | 4        | Yes          |



 

## Related topics

<dl> <dt>

[Shader Model 4](dx-graphics-hlsl-sm4.md)
</dt> </dl>

 

 




