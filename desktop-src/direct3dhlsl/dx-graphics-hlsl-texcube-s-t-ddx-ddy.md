---
title: texCUBE
description: Samples a cube texture using a gradient to select the mip level.
ms.assetid: '5615f48b-eb0a-4de7-a441-51ec3cecf6fd'
keywords: ["texCUBE HLSL"]
topic_type:
- apiref
api_name:
- texCUBE
api_type:
- NA
---

# texCUBE

Samples a cube texture using a gradient to select the mip level.



| ret texCUBE(s, t, ddx, ddy) |
|-----------------------------|



 

## Parameters



| Item                                                         | Description                                                                  |
|--------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="s"></span><span id="S"></span>*s*<br/>       | \[in\] The sampler state.<br/>                                         |
| <span id="t"></span><span id="T"></span>*t*<br/>       | \[in\] The texture coordinate.<br/>                                    |
| <span id="ddx"></span><span id="DDX"></span>*ddx*<br/> | \[in\] Rate of change of the surface geometry in the x direction.<br/> |
| <span id="ddy"></span><span id="DDY"></span>*ddy*<br/> | \[in\] Rate of change of the surface geometry in the y direction.<br/> |



 

## Return Value

The value of the texture data.

## Type Description



| Name | In/Out | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size |
|------|--------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|------|
| s    | in     | [**object**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types) | [samplerCUBE](dx-graphics-hlsl-sampler.md)                    | 1    |
| t    | in     | [**vector**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 3    |
| ddx  | in     | [**vector**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 3    |
| ddy  | in     | [**vector**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 3    |
| ret  | out    | [**vector**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 4    |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported                |
|-----------------------------------------------------------|--------------------------|
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes (pixel shader only)  |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | yes¹ (pixel shader only) |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | yes² (pixel shader only) |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no                       |



 

1.  Significant code reordering is done to move gradient computations outside of flow control.
2.  If the D3DPSHADERCAPS2\_0 cap is set with D3DD3DPSHADERCAPS2\_0\_GRADIENTINSTRUCTIONS, the compiler maps this function to texldd.

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





