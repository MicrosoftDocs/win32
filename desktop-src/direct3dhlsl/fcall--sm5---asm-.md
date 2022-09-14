---
title: fcall (sm5 - asm)
description: Interface function call.
ms.assetid: C21784A0-D2F4-4DDE-9AC4-4F21351BCA6E
ms.topic: reference
ms.date: 05/31/2018
---

# fcall (sm5 - asm)

Interface function call.



| fcall fp\#\[arrayIndex\]\[callSite\] |
|--------------------------------------|



 



| Item                                                                                                           | Description                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="fp_"></span><span id="FP_"></span>*fp\#*<br/>                                                  | \[in\] The function pointer.<br/>                                                                                                                                                                                                                                                                    |
| <span id="arrayIndex"></span><span id="arrayindex"></span><span id="ARRAYINDEX"></span>*arrayIndex*<br/> | \[in\] Optional. Specifies an offset into the function pointer array. This parameter must be a literal unsigned integer if fp\# was not declared as indexable. Otherwise, arrayIndex may be of the form literal base + offset from a shader register. For example, fcall fp1\[r1.w + 0\]\[0\] .<br/> |
| <span id="_callSite"></span><span id="_callsite"></span><span id="_CALLSITE"></span> *callSite*<br/>     | \[in\] Optional. A literal unsigned integer offset into the selected function table, selecting a function body fb\# to execute. <br/>                                                                                                                                                                |



 

## Remarks

*fp\#*\[*arrayIndex*\]\[\] resolves to a particular function table, selected from the API outside the shader from the function table choices listed in the declaration of *fp\#*.

The sum of \# in *fp\#* and *arrayIndex* select the function table. For example, if an interface is declared as fp4\[4\]\[3\] (array size of 4), the following **fcall**s are equivalent: fcall fp4\[2\]\[3\] and fp5\[1\]\[3\], because 4+2 = 5+1.

### Restrictions

-   If *arrayIndex* uses dynamic indexing, behavior is undefined if *arrayIndex* diverges on adjacent shader invocations, which could be executing in lockstep. The HLSL compiler will attempt to disallow this case.

    Adjacent invocations can be inactive due to flow control, because it doesn t break lockstep execution.

-   If *fp\#* + *arrayIndex* specifies an out of bounds index, behavior is undefined.
-   For the undefined cases described here, it means the behavior of the current D3D device becomes undefined, including the possibility of Device Lost. However no memory outside the current D3D device will be accessed or executed as code.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

### Minimum Shader Model

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

 

 





