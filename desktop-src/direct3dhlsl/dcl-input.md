---
title: dcl_input (sm4 - asm)
description: dcl\_input (sm4 - asm)
ms.assetid: 13456f2a-ee6c-42da-a9fe-670ab0fcbddf
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_input (sm4 - asm)

Declares a shader-input register.



| dcl\_input v*N\[.mask\]\[, interpolationMode\]* |
|-------------------------------------------------|



 




| Item | Description | 
|------|-------------|
| <span id="vN_.mask_"></span><span id="vn_.mask_"></span><span id="VN_.MASK_"></span>v<em>N[.mask]</em><br /> | [in] A vertex data register. <br /><ul><li><em>N</em> is an integer that identifies the register number.</li><li><em>[.mask]</em> is an optional component mask (.xyzw) that specifies which of the register components to use.</li></ul> | 
| <span id="interpolationMode"></span><span id="interpolationmode"></span><span id="INTERPOLATIONMODE"></span><em>interpolationMode</em><br /> | [in] Optional. The interpolation mode, which is only honored on pixel shader input registers. It can be one of the following values: <br /><ul><li>constant - do not interpolate between register values.</li><li>linear - interpolate linearly between register values.</li><li>linearCentroid - same as linear but centroid clamped when multisampling.</li><li>linearNoperspective - same as linear but with no perspective correction.</li><li>linearNoperspectiveCentroid - same as linear, centroid clamped when multisampling, no perspective correction.</li></ul> | 




 

### Interpolation Notes

By default, vertex attributes are interpolated from a pixel center when performing multisample antialiasing. If a pixel center is not covered, an attribute is extrapolated to a pixel center before interpolation.

For a pixel that is not fully covered or an attribute that does not cover a pixel center, you can specify centroid sampling which forces sampling to occur somewhere within the covered area of the pixel. Because a sample mask (if used) is applied before the centroid is computed, any sample location masked out by the sample mask cannot be chosen as a centroid location.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

To identify the input as a system value, use [dcl\_input\_sv (sm4 - asm)](dcl-input-sv.md).

This instruction is included to aid in debugging a shader in assembly; you cannot author a shader in assembly language using Shader Model 4.

## Example

Here are some examples.


```
dcl_input v3.xyz

dcl_input v0.x, linearCentroid
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

 

 





