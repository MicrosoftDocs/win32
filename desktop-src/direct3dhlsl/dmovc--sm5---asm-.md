---
title: dmovc (sm5 - asm)
description: Component-wise conditional move. | dmovc (sm5 - asm)
ms.assetid: E376FE08-E251-4BE5-9F15-99B3B67A29C8
ms.topic: reference
ms.date: 05/31/2018
---

# dmovc (sm5 - asm)

Component-wise conditional move.



| dmovc\[\_sat\] dest\[.mask\], src0\[.swizzle\], \[-\]src1\[\_abs\]\[.swizzle\], \[-\]src2\[\_abs\]\[.swizzle\], |
|-----------------------------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                                                              |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The move destination.<br/> If *src0*, then *dest* = *src1* else *dest* = *src2*.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components to test the condition against.<br/>                                          |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The components to move if the condition is true.<br/>                                       |
| <span id="src2"></span><span id="SRC2"></span>*src2*<br/> | \[in\] The components to move if the condition is false.<br/>                                      |



 

## Remarks

The following example shows how to use this instruction.

``` syntax
                if(the dest mask contains .xy)
                {
                    if(the first 32-bit component of src0, post-swizzle, 
                       has any bit set)
                    {
                        copy the first double from src1 (post swizzle)
                        into dest.xy
                    }
                    else
                    {
                        copy the first double from src2 (post swizzle)
                        into dest.xy
                    }
                }
                if(the dest mask contains .zw)
                {
                    if(the second 32-bit component of src0, post-swizzle, 
                       has any bit set)
                    {
                        copy the second double from src1 (post swizzle)
                        into dest.zw
                    }
                    else
                    {
                        copy the second double from src2 (post swizzle)
                        into dest.zw
                    }
                }
```

The valid masks for dest are .xy, .zw, .xyzw.

The valid swizzles for *src0* are anything. The first two components post-swizzle are used to indentify two 32-bit condition values.

The valid swizzles for *src1* and *src2* containing doubles are .xyzw, .xyxy, .zwxy, .zwzw. are .xy, .zw, and .xyzw.

The following *src* mappings below are post-swizzle:

-   *dest* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).
-   *src0* is a 32bit/component vec2 across x and y (zw ignored).
-   *src1* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).
-   *src2* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).

The modifiers on *src1* and *src2*, other than swizzle, assume the data is double. The absence of modifiers moves data without altering bits.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

## Minimum Shader Model

This instruction is supported in the following shader models:



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





