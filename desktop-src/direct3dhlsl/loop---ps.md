---
title: loop - ps
description: Starts a loop...endloop - ps block.
ms.assetid: 'vs|directx_sdk|~\loop___ps.htm'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# loop - ps

Starts a loop...[endloop - ps](endloop---ps.md) block.

## Syntax



| loop aL, i\# |
|--------------|



 

Where:

-   aL is the [Loop Counter Register](dx9-graphics-reference-asm-ps-registers-loop-counter.md) holding the current loop count.
-   i\# is a [Constant Integer Register](dx9-graphics-reference-asm-ps-registers-constant-integer.md). See remarks.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| loop                  |      |      |      |      |      |      |       | x    | x     |



 

-   The [Loop Counter Register](dx9-graphics-reference-asm-ps-registers-loop-counter.md) (aL) holds the current loop count and can be used for relative addressing into [Input Color Register](dx9-graphics-reference-asm-ps-registers-input-color.md) (v\#) inside the loop block.
-   i\#.x specifies the iteration count. The legal range is \[0, 255\]. Note that this instruction does not increment or decrement the value of i\#.x.
-   i\#.y specifies the initial value of the [Loop Counter Register](dx9-graphics-reference-asm-ps-registers-loop-counter.md) (aL) register. The legal range is \[0, 255\]. Note that this instruction does not increment or decrement the value of i\#.y.
-   i\#.z specifies the step/stride size. The legal range is \[-128, 127\].
-   i\#.w is not used by the loop block and has to be 0.
-   Loop blocks may be nested. See [Flow Control Limitations](dx9-graphics-reference-asm-ps-instructions-flow-control.md).
-   When nested, the value of the [Loop Counter Register](dx9-graphics-reference-asm-ps-registers-loop-counter.md) (aL) refers to the immediate enclosing loop block.
-   Loop blocks are allowed to be either completely inside an if\* block or completely surrounding it. No straddling is allowed.

## Example


```
loop aL, i3
    add r1, r0, v2[ aL ]
endloop
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




