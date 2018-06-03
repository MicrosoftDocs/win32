---
title: tex1D
description: Samples a 1D texture using a gradient to select the mip level.
ms.assetid: 1fa01f39-1c01-4a2e-9f7d-ca8e887b00bb
keywords:
- tex1D HLSL
topic_type:
- apiref
api_name:
- tex1D
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# tex1D

Samples a 1D texture using a gradient to select the mip level.



| ret tex1D(s, t, ddx, ddy) |
|---------------------------|



 

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
| s    | in     | [**object**](https://www.bing.com/search?q=**object**) | [sampler1D](dx-graphics-hlsl-sampler.md)                      | 1    |
| t    | in     | [**vector**](https://www.bing.com/search?q=**vector**) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 1    |
| ddx  | in     | [**vector**](https://www.bing.com/search?q=**vector**) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 1    |
| ddy  | in     | [**vector**](https://www.bing.com/search?q=**vector**) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 1    |
| ret  | out    | [**vector**](https://www.bing.com/search?q=**vector**) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                        | 4    |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported                |
|-----------------------------------------------------------|--------------------------|
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes (pixel shader only)  |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | yes  (pixel shader only) |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | yes  (pixel shader only) |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no                       |



 

1.  Significant code reordering is done to move gradient computations outside of flow control.
2.  If the D3DPSHADERCAPS2\_0 cap is set with D3DD3DPSHADERCAPS2\_0\_GRADIENTINSTRUCTIONS, the compiler maps this function to texldd.

## Remarks

When flow control is present in a shader, the result of a gradient calculation requested inside a given branch path is ambiguous when adjacent pixels may go down separate flow control paths. Therefore, it is deemed illegal to use any pixel shader operation that requests a gradient calculation to occur at a location that is inside a flow control construct which could vary across pixels for a given primitive being rasterized. If either side of an **if** statement with the branch attribute uses a gradient function a compiler error may be generated. See [if Statement (DirectX HLSL)](dx-graphics-hlsl-if.md).

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





