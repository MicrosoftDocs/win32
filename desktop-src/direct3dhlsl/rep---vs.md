---
title: rep - vs
description: Start a rep...endrep block.
ms.assetid: 'vs|directx_sdk|~\rep___vs.htm'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# rep - vs

Start a rep...[endrep](endrep---vs.md) block.

## Syntax



| rep i\# |
|---------|



 

where i\# is an integer register that specifies the repeat count in the .x component. See [Constant Integer Register](dx9-graphics-reference-asm-vs-registers-constant-integer.md).

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| rep                    |      | x    | x    | x     | x    | x     |



 

-   i\#.x specifies the iteration count. The legal range is \[0, 255\]. Note that this instruction does not increment or decrement the value of i\#.x.
-   i\#.yzw are not used by the repeat block.
-   Repeat blocks may be nested. See [Flow Control Nesting Limits](dx9-graphics-reference-asm-vs-instructions-flow-control.md).
-   Repeat blocks are allowed to be either completely inside an if\* block or completely surrounding it. No straddling is allowed.
-   Using the same i\# for different or nested rep instructions is fine - each loop will iterate based on the specified count.

## Example


```
rep i2
    add r0, r0, c0
endrep  
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




