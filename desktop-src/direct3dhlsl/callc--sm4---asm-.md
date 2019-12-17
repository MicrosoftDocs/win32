---
title: callc (sm4 - asm)
description: Conditionally calls a subroutine marked by where the label l\ appears in the program.
ms.assetid: 7F6E81CE-0C38-499B-B83E-FA76FA154451
ms.topic: reference
ms.date: 05/31/2018
---

# callc (sm4 - asm)

Conditionally calls a subroutine marked by where the label **l\#** appears in the program.



| callc{\_z\|\_nz} src0.select\_component, l\# |
|----------------------------------------------|



 



| Item                                                            | Description                                                     |
|-----------------------------------------------------------------|-----------------------------------------------------------------|
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The component on which to test the condition.<br/> |
| <span id="l_"></span><span id="L_"></span>*l\#*<br/>      | \[in\] The label of the subroutine.<br/>                  |



 

## Remarks

When a [ret](ret--sm4---asm-.md) is encountered, return execution to the instruction after this call.

The token format contains the offset of the corresponding label in the Shader as a convenience.

The following example shows the call instruction.


```
                ...
                callc_z  r1.y, l3 // if all bits in r0.x are 0, call l3
                callc_nz r2.z, l3 // if any bit in r0.x is nonzero, call l3
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
-   The 32-bit register supplied by *src0* is tested at a bit level. If any bit is nonzero, **callc\_nz** will perform the call. If all bits are zero, **callc\_z** will perform the call.
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

 

 





