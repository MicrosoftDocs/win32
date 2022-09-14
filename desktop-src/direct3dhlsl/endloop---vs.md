---
title: endloop - vs
description: End of a loop...endloop block.
ms.assetid: fd7df120-a927-4a66-b152-6ce5247446e4
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# endloop - vs

End of a [loop](loop---vs.md)...endloop block.

## Syntax



| endloop |
|---------|



 

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| endloop                |      | x    | x    | x     | x    | x     |



 

This instruction works as shown here.


```
LoopCounter += LoopStep;
LoopInterationCount = LoopIterationCount - 1;
if (LoopIterationCount > 0)
    Continue execution at the StartLoopOffset
```



endloop must follow the last instruction of a [loop - vs](loop---vs.md) block.

## Example


```
loop aL, i3
    add r1, r0, c2[ aL ]
endloop
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




