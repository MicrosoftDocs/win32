---
title: dcl_input_sv (sm4 - asm)
description: dcl\_input\_sv (sm4 - asm)
ms.assetid: 59270148-e2eb-4525-a888-ad7e843d62a5
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_input\_sv (sm4 - asm)

Declares a shader-input register that expects a [system-value](dx-graphics-hlsl-semantics.md) to be provided from a preceding stage.



| dcl\_input\_sv v*N\[.mask\]*, *systemValueName\[, interpolationMode\]* |
|------------------------------------------------------------------------|



 




| Item | Description | 
|------|-------------|
| <span id="vN_.mask_"></span><span id="vn_.mask_"></span><span id="VN_.MASK_"></span>v<em>N[.mask]</em><br /> | [in] A vertex data register. <br /><ul><li><em>N</em> is an integer that identifies the register number.</li><li><em>[.mask]</em> is an optional component mask (.xyzw) that specifies which of the register components to use.</li></ul> | 
| <span id="systemValueName"></span><span id="systemvaluename"></span><span id="SYSTEMVALUENAME"></span><em>systemValueName</em><br /> | [in] The system-value name which is a string (see <a href="dx-graphics-hlsl-semantics.md">system-value semantics</a>) without the "SV_" prefix.<br /> | 
| <span id="interpolationMode"></span><span id="interpolationmode"></span><span id="INTERPOLATIONMODE"></span><em>interpolationMode</em><br /> | [in] Optional. The interpolation mode which affects how values are calculated during rasterization; the mode is only used by a pixel shader. It can be one of the following values: <br /><ul><li>constant - do not interpolate between register values.</li><li>linear - interpolate linearly between register values.</li><li>linearCentroid - same as linear but centroid clamped when multisampling.</li><li>linearNoperspective - same as linear but with no perspective correction.</li><li>linearNoperspectiveCentroid - same as linear but with no perspective correction and centroid clamped when multisampling.</li></ul> | 




 

A component mask for a system-value declaration can be any appropriate subset of \[xyzw\]; declarations may not overlap (each declaration must follow the sequence xyzw). When declaring scalar system values (clip distance and cull distance for example), you can declare multiple system values in a single register. If you do so, make sure other modifiers like the interpolation modes match.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

Here are some examples:


```
// valid
dcl_input v0.y, linear
dcl_input_sv v0.w, clipDistance
dcl_input_sv v0.z, cullDistance
```




```
// invalid declarations
dcl_input v0.y, linear
dcl_input_sv v0.x, clipDistance  // the y component was previously declared, this declaration must use 
                                 // either the z or w component

dcl_input v0.y, linearNoPerspective                  // the interpolation mode is linear-no-perspective
dcl_input_sv v0.z, renderTargetArrayIndex, constant  // the interpolation modes is constant
                                                     // the interpolation modes must match
```



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

 

 





