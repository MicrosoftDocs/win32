---
title: endloop - ps
description: End of a loop - ps...endloop block.
ms.assetid: 8d05d0b3-88d2-44e3-a22d-54d8a8ceb5f4
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# endloop - ps

End of a [loop - ps](loop---ps.md)...endloop block.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| endloop               |      |      |      |      |      |      |       | x    | x     |



 

endloop must follow the last instruction of a [loop - ps](loop---ps.md) block.

## Example


```
loop aL, i3
    add r1, r0, c2[ aL ]
endloop
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




