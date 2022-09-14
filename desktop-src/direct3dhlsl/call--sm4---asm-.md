---
title: call (sm4 - asm)
description: Calls a subroutine marked by where the label l\ appears in the program.
ms.assetid: D6B7C52D-2CF7-44DB-81E3-2945477EF94A
ms.topic: reference
ms.date: 05/31/2018
---

# call (sm4 - asm)

Calls a subroutine marked by where the label **l\#** appears in the program.



| call l\# |
|----------|



 



| Item                                                       | Description                                    |
|------------------------------------------------------------|------------------------------------------------|
| <span id="l_"></span><span id="L_"></span>*l\#*<br/> | \[in\] The label of the subroutine.<br/> |



 

## Remarks

When a [ret](ret--sm4---asm-.md) is encountered, return execution to the instruction after this call.

The token format contains the offset of the corresponding label in the Shader as a convenience.

The following example shows the call instruction.


```
                ...
                call l3
                ...
                ret
                label l3
                    ...
                    retc_nz r0.x
                    ...
                ret
```



### Restrictions

-   Subroutines can nest 32 deep.
-   The return address stack is managed transparently by the implementation.
-   If there are already 32 entries on the return address stack and a **call** is issued, the call is skipped over.
-   There is no automatic parameter stack. The application can use an indexable temporary register array (x\#\[\]) to manually implement a stack. However, the subroutine call return addresses are not visible and are orthogonal to any manual stack management done by the application.
-   Indexing of the *l\#* parameter is not permitted.
-   Recursion is not permitted.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | yes       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 





