---
title: rep - ps
description: Start a rep...endrep - ps block.
ms.assetid: e87ba73d-e912-4b6b-8ca0-2977b9edc1da
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# rep - ps

Start a rep...[endrep - ps](endrep---ps.md) block.

## Syntax



| rep i\# |
|---------|



 

where i\# is an integer register that specifies the repeat count in the .x component. See [Constant Integer Register](dx9-graphics-reference-asm-ps-registers-constant-integer.md).

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| rep                   |      |      |      |      |      | x    | x     | x    | x     |



 

-   i\#.x specifies the iteration count. The legal range is \[0, 255\]. Note that this instruction does not increment or decrement the value of i\#.x.
-   i\#.yzw are not used by the repeat block.
-   Repeat blocks may be nested. See [Flow Control Limitations](dx9-graphics-reference-asm-ps-instructions-flow-control.md).
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

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




