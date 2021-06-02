---
title: Color Register
description: These vertex shader output registers contain a color value.
ms.assetid: fd36e207-7312-4c7e-b664-b2de9ba1ebcf
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Color Register

These vertex shader output registers contain a color value. 

| Register | Description              |
|----------|--------------------------|
| oD0      | diffuse color register.  |
| oD1      | specular color register. |



 

The oD0 value is interpolated and is written to the pixel shader color register 0 (v0). The oD1 value is interpolated and written to the pixel shader color register 1 (v1). For more information about pixel shader color registers, see the pixel shader [Input Color Register](dx9-graphics-reference-asm-ps-registers-input-color.md) topic.

## Remarks

Example


```
min oD0, r0, c1.x    
```



## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




